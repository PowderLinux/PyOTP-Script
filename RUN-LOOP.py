# Python script to generate and loop TOTP codes (RUN-LOOP.py)
#
# Written by p0wder: (MIT License)
# https://www.github.com/PowderLinux
# 
# PyOTP Credits: (MIT License)
# Copyright (C) 2011-2017 Mark Percival <m@mdp.im>,
# Nathan Reynolds <email@nreynolds.co.uk>, Andrey Kislyuk <kislyuk@gmail.com>,
# and PyOTP contributors
# https://github.com/pyauth/pyotp/blob/master/LICENSE

def main():
    import pyotp
    totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
    print("Current OTP:", totp.now())
	
while True:
    main()