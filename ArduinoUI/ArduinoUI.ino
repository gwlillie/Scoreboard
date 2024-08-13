const int button1Pin = 3;
const int button2Pin = 2;
//const int button3Pin = 4;
const int stream = 4;
const int field1 = 6;
const int field2 = 5;
bool streamActive; // add a check in pi script for stream is active
bool field = true;
String msg;
String nom;

void setup() {
  pinMode(button1Pin, INPUT_PULLUP);
  pinMode(button2Pin, INPUT_PULLUP);
  //pinMode(button3Pin, INPUT_PULLUP);
  pinMode(stream, OUTPUT);
  pinMode(field1, OUTPUT);
  pinMode(field2, OUTPUT);
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate
}


void loop() {
  if (Serial.available()) {
    readSerialPort();
    if (msg != "") {
      sendData();
      delay(100);
    
      if(msg == "True") {
        streamActive = true;
      } else if(msg == "False") {
        streamActive = false;
      } else if(msg == "Blake") {
        field = true;
      } else if("Bench"){
        field = false;
      }
      else {
        Serial.println("unrecognized");
      }
    }
  }
  if(digitalRead(button1Pin) == LOW) {
    streamActive = !streamActive;
    //digitalWrite(13, streamActive ? HIGH:LOW);
    Serial.println(1);
    delay(1000);
  }
  if(digitalRead(button2Pin) == LOW) {

    if (field) {
      Serial.println(3);
      
    } else {
      Serial.println(2);
      
    }
    
    field = !field;

    delay(1000);
  }
  //if(digitalRead(button3Pin) == LOW) {
  //  Serial.println(3);
  //  delay(1000);
  //}
  if(streamActive) {
    digitalWrite(stream, HIGH);
  } else if(!streamActive){
    digitalWrite(stream, LOW);
  }

  if(field) {
    digitalWrite(field1, HIGH);
    digitalWrite(field2, LOW);
  } else if(!field){
    digitalWrite(field2, HIGH);
    digitalWrite(field1, LOW);
  }

}


void readSerialPort() {
  msg = "";
  //if (Serial.available()) {
  delay(10);
  while (Serial.available() > 0) {
       msg += (char)Serial.read();
  }
  Serial.flush();
  //}
}

void sendData() {
  //write data
  Serial.print(nom);
  Serial.print(" received : ");
  Serial.print(msg);
}
