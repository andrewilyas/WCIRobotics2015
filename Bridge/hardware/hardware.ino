// Request and response sizes
const int MAX_ARGUMENT_SIZE = 5;
const int MAX_RESPONSE_SIZE = 5;
// Commands
const int SOFTWARE_CONNECT = 255;
const int HARDWARE_ACKNOWLEDGE = 254;
const int TOGGLE_LED = 3;
const int MOVE_CAMERA = 4; // Args -> Position (Up -> 0, Down -> 1)
const int TURN = 5; // Args -> Mode (left -> 0, right -> 1), Degrees (int)
const int DRIVE = 6; // Args -> Mode (forward -> 0, back -> 1), Speed (int)
const int STOP = 7; // Nothing
const int READ_ULTRASONIC = 8; // Nothing
// Other vars
bool isConnected = false;
// Method signatures
void handleCommand(int command, int data[], int (*results)[MAX_RESPONSE_SIZE]);
void setArgument(int (*results)[MAX_RESPONSE_SIZE], int index, int val);
void init(int (*results)[MAX_RESPONSE_SIZE], int val);
void initArgs(int (*results)[MAX_ARGUMENT_SIZE], int val);

// How to use this bridge:
// For each command, you must handle it. You can do so by using
//   if (command == THE_COMMAND_HERE)
// If you expect incoming data, you can fetch it by doing this
//   int pin = data[0];
// If you need to return data, you can do this
//   setArgument(results, INDEX_OF_ARRAY_HERE, RESULT_HERE);
// That's it!
//
// YOU MAY EDIT BELOW THIS LINE
// ----------------------------
#include "Servo.h"
#include "Ultrasonic.h"
Ultrasonic myultrasonic(2, 3);
Servo turningservo;
Servo drivemotor;
Servo cameraservo;
int input = 0;
int Ultra_distance= 0;
int pos = 0;
const int angleUp = 40;
const int angleDown = 120;

void initialize() {
  turningservo.attach(9);
  drivemotor.attach(12);
  cameraservo.attach(11);
}
void motor(int val) {
  drivemotor.write(val + 90);
}
void turnright() {
  turningservo.write(120);
  //delay(100);
}
void turnleft() {
  turningservo.write(60);
  //delay(100);
}
void movecar(int p) {
  motor(p);
  //delay(t);
}
void carstop() {
  motor(0);
  //delay(50);
}
void cameraup() {
  cameraservo.write(angleUp);
  //delay(100);
}
void cameradown() {
  cameraservo.write(angleDown);
  //delay(100);
}

void handleCommand(int command, int data[], int (*results)[MAX_RESPONSE_SIZE]) {
    switch (command){
      case DRIVE:
        movecar(data[0]);
        break;
      case STOP:
        carstop();
        break;
      //case MOVE_CAMERA:
       // if ();
       // break;
    }
   
  //  if (command == TOGGLE_LED) {
//    if (state[data[0]]) {
//      digitalWrite(data[0], LOW);
//      state[data[0]] = false;
//    } else {
//      digitalWrite(data[0], HIGH);
//      state[data[0]] = true;
//    }
  //  setArgument(results, 0, 3);//the first index returnes is 3
  //  setArgument(results, 1, 4);
  //}
}

// DO NOT TOUCH BELOW THIS LINE
// ----------------------------

void setup() {
  Serial.begin(28800);
  initialize();
  //Serial.write(WAITING);
}

void loop() {
  if (Serial.available() > 0) {
    int input = Serial.read();
    if (input == SOFTWARE_CONNECT) {
      if (!isConnected) {
        isConnected = true;
        Serial.write(HARDWARE_ACKNOWLEDGE);
        digitalWrite(8, HIGH);
      }
    } else {
      while (Serial.available() < 2);
      int amountRequired = Serial.read();
      if (amountRequired == 0) {
        int results[MAX_RESPONSE_SIZE];
        init(&results, 255);
        handleCommand(input, {}, &results);
        Serial.write(input);
        int len = 0;
        for (int i = 0; i < 10; i++) {
          if (results[i] != 255) {
            len++;
          }
        }
        Serial.write(len);
        for (int i = 0; i < len; i++) {
          if (results[i] != 255) {
            Serial.write(results[i]);
          }
        }
        Serial.write(255);
      } else {
        while (Serial.available() < amountRequired);
        int data[MAX_ARGUMENT_SIZE] = {};
        initArgs(&data, -1);
        for (int i = 0; i < amountRequired; i++) {
          data[i] = Serial.read();
        }
        Serial.write(input);
        int results[MAX_RESPONSE_SIZE];
        init(&results, 255);
        handleCommand(input, data, &results);
        int len = 0;
        for (int i = 0; i < MAX_RESPONSE_SIZE; i++) {
          if (results[i] != 255) {
            len++;
          }
        }
        Serial.write(len);
        for (int i = 0; i < len; i++) {
          if (results[i] != 255) {
            Serial.write(results[i]);
          }
        }
        Serial.write(255);
      }
    }
  }
}

void setArgument(int (*results)[MAX_RESPONSE_SIZE], int index, int val) {
  (*results)[index] = val;
}

void init(int (*results)[MAX_RESPONSE_SIZE], int val) {
  for (int index = 0; index < MAX_RESPONSE_SIZE; index++) {
    (*results)[index] = val;
  }
}

void initArgs(int (*results)[MAX_ARGUMENT_SIZE], int val) {
  for (int index = 0; index < MAX_ARGUMENT_SIZE; index++) {
    (*results)[index] = val;
  }
}

