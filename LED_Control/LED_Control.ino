/*
 _   _  _       _  _     _____  _              _    _               _      _ 
| | | |(_)     (_)| |   |_   _|| |            | |  | |             | |    | |
| | | | _  ___  _ | |_    | |  | |__    ___   | |  | |  ___   _ __ | |  __| |
| | | || |/ __|| || __|   | |  | '_ \  / _ \  | |/\| | / _ \ | '__|| | / _` |
\ \_/ /| |\__ \| || |_    | |  | | | ||  __/  \  /\  /| (_) || |   | || (_| |
 \___/ |_||___/|_| \__|   \_/  |_| |_| \___|   \/  \/  \___/ |_|   |_| \__,_|
 
 https://github.com/LiquidGalaxyLAB/Visit-the-World
 By: Otávio Oliveira
-------------------------------------------------------------
 */
//Definition of the pins for the leds
const int redPin=9;
const int bluePin=10;
const int greenPin=11;

void setup() {

  Serial.begin(9600);
  pinMode(redPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  
  digitalWrite(redPin,LOW);
  digitalWrite(bluePin,LOW);
  digitalWrite(greenPin,LOW);
}

void loop() {
  
      char pin = Serial.read();
      
      if(pin == 'a')
       {
         digitalWrite(redPin,HIGH);
       }
        else if(pin == 'b')
             {
               digitalWrite(bluePin,HIGH);
             }
              else if(pin == 'c')
                   {
                     digitalWrite(greenPin,HIGH);
                   }
                    else if(pin == 'd')
                         {
                           digitalWrite(redPin,LOW);
                           digitalWrite(bluePin,LOW);
                           digitalWrite(greenPin,LOW);
                         }

}
