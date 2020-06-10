// โปรแกรม Slave อย่างง่าย (ไม่มีการระบุ Address ของ Slave)
//
// คำสั่งจาก Master
//  0 = อ่านค่า Sensor จาก Plant Simulation แล้วส่งค่าดังกล่าวไปยัง Master
//  1 = ส่งคำสั่งเพื่อควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Deactive
//  2 = ส่งคำสั่งเพื่อควบคุม Actuator ใน Plant Simulation ให้ Linear Actuator มีสถานะ Active

// ตัวแปรสำหรับเก็บค่าที่อ่านได้จาก Serial Port
char read_serial  = 0;
int sensor_value  = 0;

void setup()
{

  // ใช้งาน Serial Port เชื่อมต่อไปยัง Master
  Serial.begin(115200);

  // กำหนด I/O สำหรับ Proximitry (pin 8) และ Actuator (pin 6)
  pinMode(8, INPUT);
  pinMode(6, OUTPUT);

}

void loop()
{

  // ตรวจสอบ Buffer ข้อมูลที่ส่งมาจาก Master
  if (Serial.available() > 0)
  {
    // อ่านค่าจาก Serial Port
    read_serial = Serial.read();

    // ตรวจสอบคำสั่งที่ได้จาก Master
    if (read_serial == 48)  // 48 = 0 (DEC => CHAR)
    {
      // อ่านค่า Sensor จาก Plant Simulation
      sensor_value = digitalRead(8);
      // ส่งค่าที่อ่านได้กลับไปยัง Master
      Serial.print(sensor_value);
    }
    else if (read_serial == 49) // 49 = 1 (DEC => CHAR)
    {
      // ควบคุม Actuator ใน Plant Simulation
      digitalWrite(6, LOW);
    }
    else if (read_serial == 50) // 50 = 2 (DEC => CHAR)
    {
      // ควบคุม Actuator ใน Plant Simulation
      digitalWrite(6, HIGH);
    }
  }

  delay(10);

}
