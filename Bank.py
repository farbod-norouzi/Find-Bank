# Check the requirements

try:
    import os
    from os import system
    import datetime
    from colorama import Fore 
except ImportError:
   system("pip install os ")
   system("pip install colorama ")
   system("pip install datetime")
   exit("\n\nRun script Again")

# Start APP

os.system("cls")
print(Fore.RED + """ ______              _        _______ _           _             
(____  \            | |      (_______|_)         | |            
 ____)  ) ____ ____ | |  _    _____   _ ____   _ | | ____  ____ 
|  __  ( / _  |  _ \| | / )  |  ___) | |  _ \ / || |/ _  )/ ___)
| |__)  | ( | | | | | |< (   | |     | | | | ( (_| ( (/ /| |    
|______/ \_||_|_| |_|_| \_)  |_|     |_|_| |_|\____|\____)_|    
                                                                """,Fore.WHITE)
                                                                

datetime_object = datetime.datetime.now()
print(datetime_object,'\n')

sixnum = input(Fore.LIGHTBLUE_EX + "Please enter the prefix of the desired bank: > ")

if sixnum == "627353":
    print('\n',Fore.GREEN+ "Bank : Tejarat"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod",'\n')
elif sixnum == "589210":
    print('\n',Fore.GREEN+ "Bank : Sepah"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod",'\n')
elif sixnum == "603769":
    print('\n',Fore.GREEN+ "Bank : Saderat"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod",'\n')
elif sixnum == "627648":
    print('\n',Fore.GREEN+ "Bank : Tosee Saderat"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod",'\n')
elif sixnum == "610433":
    print('\n',Fore.GREEN+ "Bank : Melat"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "628157":
    print('\n',Fore.GREEN+ "Bank : Tosee Taavon"+Fore.RESET) 
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "627961":
    print('\n',Fore.GREEN+ "Bank : Sanaat o Madan"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n') 
elif sixnum == "589463":
    print('\n',Fore.GREEN+ "Bank : Refah"+Fore.RESET) 
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "621986":
    print('\n',Fore.GREEN+ "Bank : Sman"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "628023":
    print('\n',Fore.GREEN+ "Bank : Maskan"+Fore.RESET) 
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "603770":
    print('\n',Fore.GREEN+ "Bank : Keshavarzi"+Fore.RESET)   
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')  
elif sixnum == "603799":
    print('\n',Fore.GREEN+ "Bank : Meli"+Fore.RESET)     
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "627760":
    print('\n',Fore.GREEN+ "Bank : Post Bank iran"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')     
elif sixnum == "627412":
    print('\n',Fore.GREEN+ "Bank : Karafarin"+Fore.RESET)    
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n') 
elif sixnum == "622106":
    print('\n',Fore.GREEN+ "Bank : Parsian"+Fore.RESET) 
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "627412":
    print('\n',Fore.GREEN+ "Bank : Eghtesad Novin"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n') 
elif sixnum == "639347":
    print('\n',Fore.GREEN+ "Bank : Pasargad"+Fore.RESET) 
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "639607":
    print('\n',Fore.GREEN+ "Bank : Sarmaie"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "639346":
    print('\n',Fore.GREEN+ "Bank : Sina"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "502806":
    print('\n',Fore.GREEN+ "Bank : Shahr"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "621986":
    print('\n',Fore.GREEN+ "Bank : Tat"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "627381":
    print('\n',Fore.GREEN+ "Bank : Ansar"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "502938":
    print('\n',Fore.GREEN+ "Bank : Dey"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "639370":
    print('\n',Fore.GREEN+ "Bank : Mehr Eghtesad"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "507677":
    print('\n',Fore.GREEN+ "Bank : Noor"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "628157":
    print('\n',Fore.GREEN+ "Bank : Moaseseh Etebari Tosee"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "505801":
    print('\n',Fore.GREEN+ "Bank : Kosar"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "606256":
    print('\n',Fore.GREEN+ "Bank : Melal"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "606373":
    print('\n',Fore.GREEN+ "Bank : Mehr Iranian"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
elif sixnum == "639599":
    print('\n',Fore.GREEN+ "Bank :Qavamin"+Fore.RESET)
    print('\n'"Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')
else:
    print(Fore.RED+ "Bank : Unknown Bank"+Fore.RESET)
    print(Fore.YELLOW+ "Alert : Please Try Again"+Fore.RESET)
    print("Manufacturer:",Fore.MAGENTA+ "Senior.Farbod"+Fore.RESET,'\n')