from netmiko import ConnectHandler
import json
import os

#Alap csatlakozási adatok
cisco = {
    'device_type': 'cisco_ios',#telnethez cisco_ios_telnet port 23
    'host': '192.168.18.152',
    'username':'admin',
    'password':'Passw0rd',
    'secret': 'Passw0rd',
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
configkeres = input(f"Írd be a fájl nevét! {Fajlok}").lower()
for i in Fajlok:
    if configkeres in i.lower():
        config=json.loads(open(i,"r",encoding="utf-8").read())

#Csatlakozás az eszközhöz
k = ConnectHandler(**cisco)
k.enable()
for i in config:
    if "ssh" not in i:
        if type(config[i])==list:
            print(config[i])
            xd=k.send_config_set(config[i])
        else:
            print(f"interface {i}")
            xd=k.send_config_set(f"interface {i}")
            for j in config[i]:
                if type(config[i][j])==list:
                    print(config[i][j])
                    xd=k.send_config_set(config[i][j])
                else:
                    print(f"{j} {config[i][j]}")
                    xd=k.send_config_set(f"{j} {config[i][j]}")
        print(xd)
k.disconnect()