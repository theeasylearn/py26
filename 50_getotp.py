#import otp module

import otp

x = otp.getotp(4)
print(x)
print("otp of 6 digit",otp.getotp(6))
print("otp of 8 digit",otp.getotp(8))
print("otp of 3 digit",otp.getotp(3))
