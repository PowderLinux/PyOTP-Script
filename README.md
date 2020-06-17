# PyOTP-Script
Python scripts to generate TOTP based codes

There are two scripts provided.. 
RUN.py will generate your TOTP code, and then prompt you to either run again or quit.
RUN-LOOP.py will continuously generate your TOTP code untill the terminal is closed. (Ctrl+C)


To run:

Open either script with any text editor and add your OTP's secret key by changing 
the following line:
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
(Replace "JBSWY3DPEHPK3PXP" with your key)

Windows-
Right click and select "Open with" > "Python", or run in CMD.exe:
python RUN.py
python RUN-LOOP.py

Linux-
python3 RUN.py
python3 RUN-LOOP.py


Credits:

Scripts written by p0wder: (MIT License)
https://www.github.com/PowderLinux

PyOTP Credits: (MIT License)
https://github.com/pyauth/pyotp/blob/master/LICENSE
Copyright (C) 2011-2017 Mark Percival <m@mdp.im>,
Nathan Reynolds <email@nreynolds.co.uk>, Andrey Kislyuk <kislyuk@gmail.com>,
and PyOTP contributors
