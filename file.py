#define LEDR 19
#define LEDB 3
#define LEDG 18

#define R_channel 0
#define G_channel 1
#define B_channel 2

#define pwm_Frequency 5000 // pwm frequency  
#define pwm_resolution 8 // 8 bit resolution  

void setup() {
  
  ledcAttachPin(LEDR, R_channel);
  ledcAttachPin(LEDG, G_channel);
  ledcAttachPin(LEDB, B_channel);
  
  ledcSetup(R_channel, pwm_Frequency, pwm_resolution);
  ledcSetup(G_channel, pwm_Frequency, pwm_resolution);
  ledcSetup(B_channel, pwm_Frequency, pwm_resolution);
}

void loop() {
  RGB_Color(255, 0, 0); // RED ccolor
  delay(500);
  RGB_Color(0, 255, 0); // green color
  delay(500);
  RGB_Color(0, 0, 255); // blue color
  delay(500);
  RGB_Color(255, 255, 0); // yellow color
  delay(500);
  RGB_Color(0, 255, 255); // cyan color
  delay(500);
  RGB_Color(255, 0, 255); // magenta color
  delay(500);
  RGB_Color(255, 20, 147); // deep pink color
}

void RGB_Color(int i, int j, int k){
  ledcWrite(R_channel, i);
  ledcWrite(G_channel, j);
  ledcWrite(B_channel, k);
}