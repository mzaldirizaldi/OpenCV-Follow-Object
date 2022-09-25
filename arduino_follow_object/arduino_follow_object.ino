#include<Servo.h>

Servo servoX; //Vertical Servo
Servo servoY; //Horizontal Servo

float x_mid;
float y_mid;

float width = 32, height = 24;  // total resolution of the video
float xpos = 90;
float ypos = 70;  // initial positions of both Servos

float angle = 0.6; 

void setup()
{
  Serial.begin(9600);
  servoY.attach(11); 
  servoX.attach(9); 
  
  servoY.write(ypos);
  servoX.write(xpos);
}

void Pos()  //Servo menuju koordinat
{
    if (x_mid < ((width / 2) - 3 )){
      xpos = xpos - angle;
    }
    else if (x_mid > ((width / 2) + 3 )){
      xpos = xpos + angle;
    }
    
    if (y_mid > ((height / 2) + 2)){
      ypos = ypos + angle;
    }
    else if (y_mid < ((height / 2) - 2)){
      ypos = ypos - angle;
    }


    // if the servo degree is outside its range
    if (xpos >= 140){
      xpos = 140;
    }
    if (xpos <= 40){
      xpos = 40;
    }
    
    if (ypos >= 110){
      ypos = 110;
    }
    if (ypos <= 40){
      ypos = 40;
    }

    servoX.write(xpos);
    Serial.print("X: ");
    Serial.print(xpos);
    servoY.write(ypos);
    Serial.print("Y: ");
    Serial.println(ypos);
}

void loop()
{
  if(Serial.available() > 0)
  {
    if(Serial.read() == 'X')
    {
      x_mid = Serial.parseInt();
      
      if(Serial.read() == 'Y')
      {
       y_mid = Serial.parseInt();
       Pos();
//       delay(5);
      }
    }
  }
}
