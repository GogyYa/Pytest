from netmiko import ConnectHandler
import datetime
from datetime import datetime
import os
import configparser
from shutil import copyfile
import time

nowTime = datetime.strftime(datetime.now(), "_%Y_%m_%d")

newpath = r'C:\\backSW\\backup' + nowTime
if not os.path.exists(newpath):
    os.makedirs(newpath)

config = configparser.ConfigParser()
config.read('config.ini')
sw_user = config.get('sw', 'user')
sw_pass = config.get('sw', 'password')



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

aruba_35_1 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.1',
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

aruba_35_15 = {
	'device_type':'hp_procurve',
	'ip':'192.168.35.15',
	'username':sw_user,
	'password':sw_pass,
}


SW_all = [aruba_35_6, aruba_35_15, aruba_35_9, aruba_35_10, aruba_35_11, aruba_35_12, aruba_35_13, aruba_35_14, aruba_35_51, aruba_35_23, aruba_35_24, aruba_35_20, aruba_35_19, aruba_35_21, aruba_35_25, aruba_35_22, aruba_35_56, aruba_35_55, aruba_35_41, aruba_35_40, aruba_35_42, aruba_35_43, aruba_35_44, aruba_35_59, aruba_35_54, aruba_35_50, aruba_35_49, aruba_35_58, aruba_35_28, aruba_35_29, aruba_35_31, aruba_35_32, aruba_35_33, aruba_35_34, aruba_35_35, aruba_35_36, aruba_35_39, aruba_35_38, aruba_35_37]
SW_core = [aruba_35_1]
SW_Coreadm = [aruba_35_8]


for x in SW_all:

    try:
        net_connect = ConnectHandler(**x)
        swname = x['ip'] + '_#' + net_connect.find_prompt() + nowTime
        output = net_connect.send_command("copy  running-config tftp 192.168.35.89 %s" % swname)
        src = "C:\\tftp\\" + swname
        dst = newpath + '\\' + swname
        time.sleep(10)
        copyfile(src, dst)
        os.remove(src)
    except Exception:
        print('error')


for x in SW_core:
    try:
        net_connect = ConnectHandler(**x)
        swname = x['ip'] + '_#' + net_connect.find_prompt() + nowTime
        output = net_connect.send_command("copy  running-config tftp 192.168.35.89 %s" % swname)
        src = "C:\\tftp\\" + swname
        dst = newpath + '\\' + swname
        time.sleep(30)
        copyfile(src, dst)
        os.remove(src)
    except Exception:
        print('error')

for x in SW_Coreadm:
    try:
        net_connect = ConnectHandler(**x)
        swname = x['ip'] + '_#' + net_connect.find_prompt() + nowTime
        output = net_connect.send_command("copy  running-config tftp 192.168.35.89 %s" % swname)
        src = "C:\\tftp\\" + swname
        dst = newpath + '\\' + swname
        time.sleep(30)
        copyfile(src, dst)
        os.remove(src)
    except Exception:
        print('error')

