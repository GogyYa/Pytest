from netmiko import ConnectHandler
import datetime
from datetime import datetime
import textfsm
import pypyodbc
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
sw_user=config.get('sw', 'user')
sw_pass=config.get('sw', 'password')

nowTime = datetime.strftime(datetime.now(), "%Y.%m.%d ")


aruba_35_6 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.6',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_8 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.8',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_9 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.9',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_10 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.10',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_11 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.11',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_12 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.12',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_13 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.13',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_14 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.14',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_51 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.51',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_23 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.23',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_24 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.24',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_20 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.20',
	'username':sw_user,
	'password':sw_pass,
}


aruba_35_19 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.19',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_21 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.21',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_25 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.25',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_22 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.22',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_56 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.56',
	'username':sw_user,
	'password':sw_pass,
}




aruba_35_55 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.55',
	'username':sw_user,
	'password':sw_pass,
}



aruba_35_41 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.41',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_40 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.40',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_42 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.42',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_43 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.43',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_44 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.44',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_59 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.59',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_54 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.54',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_50 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.50',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_49 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.49',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_58 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.58',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_28 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.28',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_29 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.29',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_31 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.31',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_32 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.32',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_33 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.33',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_34 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.34',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_35 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.35',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_36 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.36',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_39 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.39',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_38 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.38',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_37 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.37',
	'username':sw_user,
	'password':sw_pass,
}
SW_all = [aruba_35_6, aruba_35_8, aruba_35_9, aruba_35_10, aruba_35_11, aruba_35_12, aruba_35_13, aruba_35_14, aruba_35_51, aruba_35_23, aruba_35_24, aruba_35_20, aruba_35_19, aruba_35_21, aruba_35_25, aruba_35_22, aruba_35_56, aruba_35_55, aruba_35_41, aruba_35_40, aruba_35_42, aruba_35_43, aruba_35_44, aruba_35_59, aruba_35_54, aruba_35_50, aruba_35_49, aruba_35_58, aruba_35_28, aruba_35_29, aruba_35_31, aruba_35_32, aruba_35_33, aruba_35_34, aruba_35_35, aruba_35_36, aruba_35_39, aruba_35_38, aruba_35_37]

for x in SW_all:

    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("sh port-access authenticator session-counters")
        name = "#" + net_connect.find_prompt() + x['ip']

        f = open('port_access.txt', 'a')
        f.writelines(output)
        f.close()
    
        zz = name, nowTime

        with open ('port_access.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('in-progress',(str(zz)))

        with open ('port_access.txt', 'w') as f:
          f.write(new_data)

    except Exception:
        print('error')
        
f = open('port_access.txt', 'r')
RowFile = f.read()

template = open('qq.txt')
fsm = textfsm.TextFSM(template)
result = fsm.ParseText(RowFile)
connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=serv1\\NOC;'
				  'Database=noc;'
				  'uid=admin;'
				  'pwd=pass;')
cursor = connection.cursor()
sql = "insert into [dbo].[Table_802.1x](Port, IP, DeviceName, [User], Date) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(sql, result)
connection.commit()
connection.close()
template.close()
f.close()
os.remove("port_access.txt")
