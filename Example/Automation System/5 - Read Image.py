'''
โปรแกรม Master อย่างง่าย (ไม่มีการระบุ Address ของ Slave)
    ดึงข้อมูลภาพจาก Plant Simulation ผ่าน Spout  จากนั้นแปลงภาพ Texture ของ OpenGL เป็นข้อมูลภาพของ OpenCV
'''

import argparse
import SpoutSDK
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cv2

def main():

    # window details
    # ตั้งค่าขนาดของ Window ให้ตรงกับ Resolution ของ Plant Simulation
    width = 1600
    height = 900
    display = (width, height)

    # window setup
    pygame.init()
    pygame.display.set_caption('Spout Receiver (OpenGL)')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # OpenGL init
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,width,height,0,1,-1)
    glMatrixMode(GL_MODELVIEW)
    glDisable(GL_DEPTH_TEST)
    glClearColor(0.0,0.0,0.0,0.0)
    glEnable(GL_TEXTURE_2D)

    # init spout receiver
    receiverName = "Station.Vision"
    spoutReceiverWidth = width
    spoutReceiverHeight = height
    # create spout receiver
    spoutReceiver = SpoutSDK.SpoutReceiver()

	# Its signature in c++ looks like this: bool pyCreateReceiver(const char* theName, unsigned int theWidth, unsigned int theHeight, bool bUseActive);
    spoutReceiver.pyCreateReceiver(receiverName,spoutReceiverWidth,spoutReceiverHeight, False)

    # create texture for spout receiver
    textureReceiveID = glGenTextures(1)

    # initalise receiver texture
    glBindTexture(GL_TEXTURE_2D, textureReceiveID)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    # copy data into texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, spoutReceiverWidth, spoutReceiverHeight, 0, GL_RGBA, GL_UNSIGNED_BYTE, None )
    glBindTexture(GL_TEXTURE_2D, 0)

    # loop for graph frame by frame
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spoutReceiver.ReleaseReceiver()
                pygame.quit()
                quit(0)

        # receive texture
        # Its signature in c++ looks like this: bool pyReceiveTexture(const char* theName, unsigned int theWidth, unsigned int theHeight, GLuint TextureID, GLuint TextureTarget, bool bInvert, GLuint HostFBO);
        spoutReceiver.pyReceiveTexture(receiverName, spoutReceiverWidth, spoutReceiverHeight, int(textureReceiveID), GL_TEXTURE_2D, False, 0)

        glBindTexture(GL_TEXTURE_2D, textureReceiveID)

        # copy pixel byte array from received texture - this example doesn't use it, but may be useful for those who do want pixel info
        # แปลงภาพ Texture ใน OpenGL เป็นข้อมูลภาพของ OpenCV
        img_opencv = glGetTexImage(GL_TEXTURE_2D, 0, GL_BGR, GL_UNSIGNED_BYTE, outputType=None)  #Using GL_RGB can use GL_RGBA

        # swap width and height data around due to oddness with glGetTextImage. http://permalink.gmane.org/gmane.comp.python.opengl.user/2423
        img_opencv.shape = (img_opencv.shape[1], img_opencv.shape[0], img_opencv.shape[2])

        # setup window to draw to screen
        glActiveTexture(GL_TEXTURE0)

        # clean start
        glClear(GL_COLOR_BUFFER_BIT  | GL_DEPTH_BUFFER_BIT )
        # reset drawing perspective
        glLoadIdentity()

        # draw texture on screen
        # glPushMatrix() use these lines if you want to scale your received texture
        # glScale(0.3, 0.3, 0.3)
        glBegin(GL_QUADS)

        glTexCoord(0,0)
        glVertex2f(0,0)

        glTexCoord(1,0)
        glVertex2f(spoutReceiverWidth,0)

        glTexCoord(1,1)
        glVertex2f(spoutReceiverWidth,spoutReceiverHeight)

        glTexCoord(0,1)
        glVertex2f(0,spoutReceiverHeight)

        glEnd()
        # glPopMatrix() make sure to pop your matrix if you're doing a scale
        # update window
        pygame.display.flip()


        ### เริ่มต้นประมวลผลภาพด้วย OpenCV ###

        # แสดงภาพ
        cv2.imshow("OpenCV", img_opencv)

        if (cv2.waitKey(1) == 27):
            spoutReceiver.ReleaseReceiver()
            pygame.quit()
            quit(0)

        ### เสร็จสิ้นการประมวลผลภาพด้วย OpenCV ###




if __name__ == '__main__':
    main()
