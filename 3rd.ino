#include <Wire.h>
#include <LiquidCrystal_I2C.h>

int l1, l2;
LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  lcd.init();
  lcd.backlight();
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    sscanf(input.c_str(), "%d,%d", &l1, &l2);
    lcd.setCursor(0, 0);
    lcd.clear();

    if (l1 > l2) {
      lcd.print("L1 is congested      ");
    }
    else if (l2 > l1) {
      lcd.print("L2 is congested      ");
    }
    else {
      lcd.print("L1 L2 equal  ");
    }
  }
}
