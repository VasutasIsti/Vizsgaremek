from netmiko import ConnectHandler
from datetime import datetime
eszkozok={
    "RPecel":"10.0.0.26",
    "AMiskolc":"10.0.0.18",
    "RKobanya":"192.168.104.145",
    "RCsepel":"10.0.0.30",
    "SPecel":"192.168.101.130",
    "S1Kobanya":"192.168.104.130",
    "S2Kobanya":"192.168.104.131",
    "S3Kobanya":"192.168.100.132",
    "SCsepel":"192.168.102.130",
    "SMiskolc":"192.168.103.130"

}

for i in eszkozok:
    try:
        cisco = { #ssh
            'device_type': 'cisco_ios',
            'host': eszkozok[i],
            'username':'admin',
            'password':'admin',
            'secret': 'admin',
            "port":22
        }
        k=ConnectHandler(**cisco)
    except:
        cisco = { #telnet
            'device_type': 'cisco_ios_telnet',
            'host': eszkozok[i],
            'username':'admin',
            'password':'admin',
            'secret': 'admin',
            "port":23
        }
        k=ConnectHandler(**cisco)
    k.send_config_set(["exit"])
    o=k.send_command("show ip interface brief")
    
    f=open(f"{i}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
    for j in o:
        f.write(f"{j}\n")
    f.close()