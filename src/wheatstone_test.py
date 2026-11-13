import machine
import utime

#initialize adc's
adc0 = machine.ADC(0)
adc1 = machine.ADC(1)

U_0 = 3.3 #3V3 Spannung des Pico

while True:
    U_3 = adc0.read_u16() * U_0/65535 #Spannung U3
    U_1 = adc1.read_u16() * U_0/65535 #Spannung U1
    U_B = U_1 - U_3 #Brückenspannung
    print(U_1, "-", U_3, "=", U_B)
    utime.sleep(1)

