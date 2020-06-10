# IIoT-System-Integration
Code สำหรับใช้ในการเรียนการสอนในโครงการ`การประยุกต์ใช้จริงของเทคโนโลยีไอโอทีสำหรับภาคอุตสาหกรรม (Industrial Internet of Things: IIoT) ร่วมกับระบบฝังตัว (Embedded System) เทคโนโลยีความจริงเสริม (Augmented Reality: AR) และคอมพิวเตอร์วิชั่น (Computer Vision)`

## ตัวอย่าง
- [Virtual Sensor](Example/Virtual%20Sensor)
- [Virtual Actuator](Example/Virtual%20Actuator)
- [Embedded Simulation](Example/Embedded%20Simulation)
- [Automation System](Example/Automation%20System)
- [Augmented Reality](Example/Augmented%20Reality)
- [Dashboard](Example/Dashboard)

# System Overview
![System Overview](Doc/System%20Overview%20-%202020-06-03%20A.jpg)

# System Requirement
- Windows 10
- Spout for Python [[link](https://github.com/spiraltechnica/Spout-for-Python)] (แนบไฟล์ `SpoutSDK.pyd` มาให้แล้ว)
- Miniconda3 Windows 64-bit [[link](https://docs.conda.io/en/latest/miniconda.html)]
  - Python 3.5 (Virtual Environment) [[link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)]
    - opencv-contrib-python
    - pyopengl
    - pygame

# Application
- [Plant Simulation 2020](https://github.com/Cluster-APX/Plant-Simulation-2020)
- Computer Vision
- Embedded Simulation

# การใช้งาน
## Plant Simulation (Unity)
- เปิดใช้งาน `FIBO Plant Simulator 2020.exe`
- ตั้งค่า Resolution `1920x1080`

## Computer Vision (Python)
- ตั้งค่า Resolution ใน Code ให้ตรงตาม Plant Simulation
- สำหรับเครื่องที่ใช้ CPU ที่มี APU ต้องทำการตั้งค่าให้ Python ใช้งาน GPU ในการ Redner ดังนี้
  - Nvidia GPU
    - เปิดโปรแกรม NVIDIA Control Panel
    - Manage 3D Setting -> Program Settings
    - `1. Select a program to customize:` = python.exe
    - `2. Select the preferred graphics processor for this program:` = High-performance NVIDIA processor
  - AMD GPU
    - ?
