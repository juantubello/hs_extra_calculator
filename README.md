# hs_extra_calculator
Simple desktop app that retrieves data from excel and calculte the total of extra hours that I worked

This app was developed in Linux sistem but I am currently using it in Windows 10 S.O, so basically I compiled it and generate only the binaries for this particualry SO with 
this command on Windows VM CMD: ##pyinstaller --onefile --noconsole --hidden-import=xlrd  --hidden-import=pandas._libs.tslibs.timedelta hs_extra.py
once it builded is availible you will find the .exe on /dist folder!
