// Arduino IDE:
// File -> Examples -> 04.Communication -> PhysicalPixel
// Le code se base sur l'exemple donne dans la librairie Arduino

//Association des variables
int incomingByte;        // variable stores  serial data
const int Main= 3;       // pin pour activer/désactiver la vanne Main
const int Bleed  = 4;    // pin pour activer/désactiver la vanne Bleed
const int Supply = 5;    // pin pour activer/désactiver la vanne Supply
const int triggers1 = 6; // pin pour activer/désactiver le triggers1 pour l'allumeur
const int triggers2 = 7; // pin pour activer/désactiver le triggers2 pour l'allumeur
const int Shunt = 8;     // pin pour activer/désactiver le shunt pour l'allumeur
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the  pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(Main, OUTPUT);
  pinMode(Bleed, OUTPUT);
  pinMode(Supply, OUTPUT);
  pinMode(triggers1, OUTPUT);
  pinMode(triggers2, OUTPUT);
  pinMode(Shunt, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital M , turn off all output:
    if (incomingByte == 'M') {
      digitalWrite(Shunt, LOW);
      digitalWrite(triggers1, LOW);
      digitalWrite(triggers2,LOW);
      digitalWrite(Main, LOW);
      digitalWrite(Bleed, LOW);
      digitalWrite(Supply, LOW);
    }
    // if it's a capital Q , turn ON Main pin :
    if (incomingByte == 'Q') {
      digitalWrite(Main, HIGH);
    }
    // if it's a capital W , turn OFF Main pin 
    if (incomingByte == 'W') {
      digitalWrite(Main, LOW);
    }
    // if it's a capital E , turn ON Bleed pin 
     if (incomingByte == 'E') {
      digitalWrite(Bleed, HIGH);
    }
    // if it's a capital R , turn OFF Bleed pin 
    if (incomingByte == 'R') {
      digitalWrite(Bleed, LOW);
    }
    // if it's a capital T , turn ON Supply pin 
     if (incomingByte == 'T') {
      digitalWrite(Supply, HIGH);
    }
    // if it's a capital Y , turn OFF Supply pin
    if (incomingByte == 'Y') {
      digitalWrite(Supply, LOW);
    }
   // if it's a capital U , turn ON triggers1 pin
    if (incomingByte == 'U') {
      digitalWrite(triggers1, HIGH);
    }
   // if it's a capital I , turn OFF triggers1 pin
    if (incomingByte == 'I') {
      digitalWrite(triggers1, LOW);
    }
    // if it's a capital A , turn ON triggers2 pin
     if (incomingByte == 'A') {
      digitalWrite(triggers2, HIGH);
    }
     // if it's a capital S , turn OFF triggers2 pin
    if (incomingByte == 'S') {
      digitalWrite(triggers2, LOW);
    }
    // if it's a capital D , turn ON Shunt pin
    if (incomingByte == 'D') {
      digitalWrite(Shunt, HIGH);
    }
    // if it's an F , turn OFF Shunt pin
    if (incomingByte == 'F') {
      digitalWrite(Shunt, LOW);
    }
    // if it's an Z ,turn OFF Shunt pin,turn ON triggers1 pin,turn ON triggers2 pin  wait 1s and to turn ON  Main pin
    if (incomingByte == 'Z') {
      digitalWrite(Shunt, LOW);
      digitalWrite(triggers1, HIGH);
      digitalWrite(triggers2, HIGH);
      delay(1000);
      digitalWrite(Main, HIGH);
    };
    // if it's an X , turn OFF Shunt pin,turn ON triggers1 pin,turn ON triggers2 pin  wait 2s and to turn ON  Main pin
     if (incomingByte == 'X') {
      digitalWrite(Shunt, LOW);
      digitalWrite(triggers1, HIGH);
      digitalWrite(triggers2, HIGH);
      delay(2000);
      digitalWrite(Main, HIGH);
    }
    // if it's an C, turn OFF Shunt pin,turn ON triggers1 pin,turn ON triggers2 pin  wait 3s and to turn ON  Main pin
    if (incomingByte == 'C') {
      digitalWrite(Shunt, LOW);
      digitalWrite(triggers1, HIGH);
      digitalWrite(triggers2, HIGH);          
      delay(3000);
      digitalWrite(Main, HIGH);
    };
  }
}