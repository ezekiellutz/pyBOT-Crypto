# pyBOT-Crypto
A BOT created in python that sends daily cryptocurrency information to an expandable email list. 

The python script is intended to be converted to an executable file (.exe) and then run on a daily basis using Windows Task Manager. The .py file can be converted to an executable file using pyinstaller. Since the .exe file is intended to be built per the BOT's email address (and this code is intended to be customized to meet the end user's needs) the .exe file has been omitted. 

Whether using the .exe file or the .py file, the contacts_file.csv must be stored in the same directory as the .exe or .py file. The format of the .csv file is very basic, the code skips over the header "email" then proceeds to go down the list of email addresses listed and send emails to each one. 

While this code specifically lists cryptocurrency pricing, it can be adapted to a wider variety of alerts based on a different API. 

