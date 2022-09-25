import random
import math
import smtplib



#OTP Section
digits = "0123456789"
OTP = ''
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP

try:
    receiver_mail = input("Enter Your Mail-Id : ")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("balu02091999@gmail.com", "titrelvdaawvarnf")
    message = "This the OTP from HDFC bank for your Netbanking "+otp
    s.sendmail("balu02091999@gmail.com", receiver_mail, message)
    s.quit()
    received_otp  = input("Enter the OTP which U received : ")
except:
    print("error in Mail section")



if OTP == received_otp:
    print("Logged in Successfully")
else:
    print("OTP was Wrong")


