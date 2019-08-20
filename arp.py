from netmiko import ConnectHandler
import datetime
from datetime import datetime
import textfsm
import pypyodbc
import os
import configparser
import textfsm
import time
import smtplib
from email.mime.text import MIMEText
import os.path

me = 'Heorhii_Yatskovskyi@ggg.ggg'
you = 'Heorhii_Yatskovskyi@ggg.ggga'
smtp_server = 'smtp-mdoffice.ggg.ggg'
rcpt = [you]
now = datetime.now()
current_date = str(now.strftime("'%Y-%m-%d'"))

config = configparser.ConfigParser()
config.read('config.ini')
sw_user=config.get('sw', 'user')
sw_pass=config.get('sw', 'password')

nowTime = datetime.strftime(datetime.now(), "%Y.%m.%d ")

aruba_35_1 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.1',
	'username':'log',
	'password':'pass',
}

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

aruba_35_52 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.52',
	'username':sw_user,
	'password':sw_pass,
}

aruba_35_53 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.53',
	'username':sw_user,
	'password':sw_pass,
}

SW_all_new = [aruba_35_8, aruba_35_10, aruba_35_11, aruba_35_25, aruba_35_14,  aruba_35_51, aruba_35_23, aruba_35_19, aruba_35_21, aruba_35_25, aruba_35_22, aruba_35_55, aruba_35_41, aruba_35_40, aruba_35_42, aruba_35_44, aruba_35_59, aruba_35_50, aruba_35_49]
SW_all_old = [aruba_35_9, aruba_35_12, aruba_35_13, aruba_35_24, aruba_35_20, aruba_35_43, aruba_35_28]
SW_core = [aruba_35_1]
SW_veryNEW = [aruba_35_6, aruba_35_56, aruba_35_54, aruba_35_58, aruba_35_29, aruba_35_31, aruba_35_32, aruba_35_33, aruba_35_34, aruba_35_35, aruba_35_36, aruba_35_39, aruba_35_38, aruba_35_37, aruba_35_52, aruba_35_53]

for x in SW_core:

    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("sh arp")
        f = open('ShowARP.txt', 'a')
        f.writelines(output)
        f.close()
        bb = nowTime

        with open ('ShowARP.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('dynamic',(str(bb)))

        with open ('ShowARP.txt', 'w') as f:
          f.write(new_data)
          
    except Exception:
        print('error')
        log = open('logARP.txt', 'a')
        outlog = 'error' + ' ' + x['ip'] + '\n'
        log.writelines(outlog)
        log.close()

        
for x in SW_all_new:

    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("sh mac-address")
        name = "#" + x['ip']


        f = open('ShowMacADD.txt', 'a')
        f.writelines(output)
        f.close()
    
        zz = name, nowTime


        with open ('ShowMacADD.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('        ', '    ')

        with open ('ShowMacADD.txt', 'w') as f:
            f.write(new_data)

        with open ('ShowMacADD.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('    ',(str(zz)))

        with open ('ShowMacADD.txt', 'w') as f:
          f.write(new_data)

    except Exception:
        print('error')
        log = open('logARP.txt', 'a')
        outlog = 'error' + ' ' + x['ip'] + '\n'
        log.writelines(outlog)
        log.close()

for x in SW_all_old:

    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("sh mac-address")
        name = "#" + x['ip']


        f = open('ShowMacADD_old.txt', 'a')
        f.writelines(output)
        f.close()
    
        zz = name, nowTime

        with open ('ShowMacADD_old.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('    ',(str(zz)))

        with open ('ShowMacADD_old.txt', 'w') as f:
          f.write(new_data)

    except Exception:
        print('error')
        log = open('logARP.txt', 'a')
        outlog = 'error' + ' ' + x['ip'] + '\n'
        log.writelines(outlog)
        log.close()

        
for x in SW_veryNEW:

    try:
        net_connect = ConnectHandler(**x)
        output = net_connect.send_command("sh mac-address")
        name = "#" + x['ip']


        f = open('ShowMacADDveryNEW.txt', 'a')
        f.writelines(output)
        f.close()
    
        zz = name, nowTime

        with open ('ShowMacADDveryNEW.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('                       ', '    ')

        with open ('ShowMacADDveryNEW.txt', 'w') as f:
            f.write(new_data)

    
        with open ('ShowMacADDveryNEW.txt', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('           ',(str(zz)))

        with open ('ShowMacADDveryNEW.txt', 'w') as f:
          f.write(new_data)

    except Exception:
        print('error')
        log = open('logARP.txt', 'a')
        outlog = 'error' + ' ' + x['ip'] + '\n'
        log.writelines(outlog)
        log.close()

s = open('ShowMacADDveryNEW.txt', 'r')
RowFile = s.read()

template = open('qqMACotherNEW.txt')
fsm = textfsm.TextFSM(template)
result3 = fsm.ParseText(RowFile)
print(result3)


          
f = open('ShowMacADD_old.txt', 'r')
RowFile = f.read()

template = open('qqMAC1111.txt')
fsm = textfsm.TextFSM(template)
result1 = fsm.ParseText(RowFile)
print(result1)


d = open('ShowMacADD.txt', 'r')
RowFile = d.read()

template = open('qqMAC.txt')
fsm = textfsm.TextFSM(template)
result2 = fsm.ParseText(RowFile)
print(result2)

print('#############################')
result4 = result1 + result2 + result3
print(result4)



b = open('ShowARP.txt', 'r')
RowFile = b.read()

template = open('qqARP.txt')
fsm = textfsm.TextFSM(template)
resultARP = fsm.ParseText(RowFile)
print(resultARP)

connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=NOC01\\NOC;'
				  'Database=noc;'
				  'uid=admin;'
				  'pwd=pass;')

cursor = connection.cursor()
sql = "insert into [dbo].[Table_sw](IP_host, mac_add_Device, Date) VALUES(?, ?, ?)"
cursor.executemany(sql, resultARP)
connection.commit()
connection.close()
template.close()
b.close()


connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=NOC01\\NOC;'
				  'Database=noc;'
				  'uid=log;'
				  'pwd=pass;')

cursor = connection.cursor()
sql = "insert into [dbo].[Table_access](mac_add_Device, port_SW, Ip_sw, Date, VID) VALUES(?, ?, ?, ?, ?)"
cursor.executemany(sql, result4)
connection.commit()
connection.close()
template.close()
f.close()
d.close()
s.close()

connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=NOC01\\NOC;'
				  'Database=noc;'
				  'uid=adm;'
				  'pwd=pass;')

cursor = connection.cursor()
sql = """insert into [noc].[dbo].[Table_result] (IP_host, mac_add_Device, VID, IP_sw, PORT_sw, [Date])
SELECT  Table_sw.IP_host, Table_sw.mac_add_Device, Table_access.VID, Table_access.Ip_sw,  Table_access.port_SW,  Table_access.[Date]
  FROM [noc].[dbo].[Table_access]
 INNER JOIN Table_sw ON Table_access.mac_add_Device =
		Table_sw.mac_add_Device and Table_access.[Date] = Table_sw.[Date]"""

cursor.executemany(sql)
connection.commit()
connection.close()

connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=NOC01\\NOC;'
				  'Database=noc;'
				  'uid=adm;'
				  'pwd=pass;')

cursor = connection.cursor()
sql = """delete
  FROM [noc].[dbo].[Table_access]"""
cursor.executemany(sql)
connection.commit()
connection.close()


connection = pypyodbc.connect('Driver={SQL Server};'
				  'Server=NOC01\\NOC;'
				  'Database=noc;'
				  'uid=adm;'
				  'pwd=pass;')

cursor = connection.cursor()
sql = """delete
   FROM [noc].[dbo].[Table_sw]"""
cursor.executemany(sql)
connection.commit()
connection.close()

try:
    logFile = open('logARP.txt', 'r')
    DataFile = logFile.read()

    msg = MIMEText(DataFile)
    msg['Subject'] = 'ARP'
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP(smtp_server)
    s.sendmail(me, rcpt, msg.as_string())
    s.quit()
    logFile.close()
except IOError as e:
    print(u'не удалось открыть файл')
    
os.remove("ShowARP.txt")
os.remove("ShowMacADDveryNEW.txt")
os.remove("ShowMacADD_old.txt")
os.remove("ShowMacADD.txt")
os.remove("logARP.txt")
