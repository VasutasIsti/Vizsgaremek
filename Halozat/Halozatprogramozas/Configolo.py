from netmiko import ConnectHandler
import json
import os

#Alap csatlakozási adatok
cisco = {
    'device_type': 'cisco_ios',#telnethez cisco_ios_telnet port 23
    'host': '',
    'username':'admin',
    'password':'admin',
    'secret': 'admin',
    "port":22
}

#Csatlakozási adatok megmásítása
for i in cisco:
    x=input(f"Írd be a {i}-t ({cisco[i]})")
    if x!="":
        cisco[i]=x

#Json fájlok nevének kimentése
Fajlok=[i for i in os.listdir() if i.split('.')[-1]=="json"]

#Fájl nevének bekérése és fájl beolvasása
config = json.loads(open(input(f"Írd be a fájl nevét! {Fajlok}"),"r",encoding="utf-8").read())

#Csatlakozás az eszközhöz
#k = ConnectHandler(**cisco)

for i in config:
    if type(config[i])==list:
        if i=="ssh":
            continue
        print(config[i])
        #k.send_config_set(config[i])
    else:
        print(f"interface {i}")
        #k.send_config_set(f"interface {i}")
        for j in config[i]:
            if type(config[i][j])==list:
                print(config[i][j])
                #k.send_config_set(config[i][j])
            else:
                print(f"{j} {config[i][j]}")
                #k.send_config_set(f"{j} {config[i][j]}")