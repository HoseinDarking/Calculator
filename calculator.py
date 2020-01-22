import os,urllib

from bs4 import *

os.system("clear")
logo = """ \033[91m

          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMyoyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMM: -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMM: -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMyyyyyy- .yyyyyyMMMMMMMMMMyyyyyyyyyyyyyyyMMMMM
          MMMMM-.....`  ......MMMMMMMMMM..............-MMMMM
          MMMMMMMMMMM: -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMM: -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMM: -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMM \033[92m Code By @Hosein_Darking" \033[91m MMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMy+yMMMMMMMMMMMMMMMMMMNmMMMMMMMmNMMMMMMM
          MMMMMMMMMMm` `mMMMMMMMMMMMMMMMMd` /mMMMm/ `dMMMMMM
          MMMMMMMMMMMNmNMMMMMMMMMMMMMMMMMMm+  /d/  /mMMMMMMM
          MMMMM-..............MMMMMMMMMMMMMMm:   :mMMMMMMMMM
          MMMMMyyyyyyyyyyyyyyyMMMMMMMMMMMMMm/  :  /mMMMMMMMM
          MMMMMMMMMMMo/oMMMMMMMMMMMMMMMMMm/  /mMm+  /mMMMMMM
          MMMMMMMMMMN. .mMMMMMMMMMMMMMMMMN+/mMMMMMm++NMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
\033[95m"""
print (logo)

while True:
    org = int(input(" [01]Jam \n [02]<Menha> \n [03]<Zarb> \n [04]<Taqsim> \n [05]<Tavan> \n [00]<Exit> \n [+] Enter a Number >>> : "))
    if org == 1:
        a = float (input("[+] Enter First Number >>> "))
        b = float (input("[+] Enter Second Number >>> "))
        print("Javab = ",a+b)
    elif org == 2:
        a = float (input("[+] Enter First Number >>> "))
        b = float (input("[+] Enter Second Number >>> "))
        print("Javab = ",a-b)
    elif org == 3:
        a = float (input("[+] Enter First Number >>> "))
        b = float (input("[+] Enter Second Number >>> "))
        print("Javab = ",a*b)
    elif org == 4:
        a = float (input("[+] Enter First Number >>> "))
        b = float (input("[+] Enter Second Number >>> "))
        print("Javab = ",a/b)

    elif org == 5:

        x = input ("[+] Enter Number >>>")

        y = input ("[+] Enter Tavan Number >>>")

        print("Javab = ",x**y)
 
    elif org == 0:
        print("Ok GoodBye")
        break
    else:
        print("Error 404 ! Please select a correct number")
        break
