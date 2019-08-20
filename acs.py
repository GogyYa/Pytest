from netmiko import ConnectHandler
import datetime
import time as t
from datetime import datetime, timedelta
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import textfsm
import pypyodbc
import os
import time
import smtplib
from email.mime.text import MIMEText
import telebot
import urllib.request

#**************************************************************************************************************************************************************
#weather
data = YahooWeather(APP_ID="ApppID",
                        api_key="KEy",
                        api_secret="secret")


    


#end weather
#**************************************************************************************************************************************************************


bot = telebot.TeleBot('rsfgsfd')
me = 'Heorhii_Yatskovskyi@ggg.ua'
you = 'Heorhii_Yatskovskyi@ggg.ua'
cc = "Andrii_Savytskyi@ggg.ua"
smtp_server = 'smtp-gg.gg.gg'
rcpt = cc.split(",") + [you]

now = datetime.now()
current_date = str(now.strftime("'%Y-%m-%d'"))



#**************************************************************************************************************************************************************
#SQL Connection

connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=acs01\\acsbosch;'
                                  'Database=BOSCH AccessPE;'
                                  'uid=login;'
                                  'pwd=pass;')
cursor = connection.cursor()
sql = """
    SELECT 
       [CardNo]
      ,[DateTime]
      ,[PersId]
      ,[LastName]
      ,[FirstName]
     
  FROM [BOSCH AccessPE].[dbo].[Messages] (nolock)
  where CardNo = '11828' and [DateTime] >= {} """.format(current_date)

cursor.executemany(sql)
result = cursor.fetchall()
print(result)

#End SQL connection
#**************************************************************************************************************************************************************


matching = [s for s in result if "Олійник" in s]
print(matching)
while True:
        if len(matching) == 0:
                print('Юзер не найден')
                cursor = connection.cursor()
                cursor.executemany(sql)
                result = cursor.fetchall()
                t.sleep(2)
                matching = [s for s in result if "Олійник" in s]

        if len(matching) > 0:
                
                cursor.executemany(sql)
                result = cursor.fetchall()
                matching = [s for s in result if "Олійник" in s]
                urllib.request.urlopen("""
                    https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}
                """.format(
                    API_TOKEN = 'dff',
                    CHAT_ID = '-352331363',
                    TEXT = 'Kukusiki'
                ))
                urllib.request.urlopen("""
                    https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}
                """.format(
                    API_TOKEN = 'token',
                    CHAT_ID = '-352331363',
                    TEXT = 'Pora delat` rabochiy vid, parni'
                ))

                dateHome = datetime.now().strftime('%H:%M:%S')
                home = '18:00:00'
                format = '%H:%M:%S'
                time = datetime.strptime(home, format) - datetime.strptime(dateHome, format)
                
                urllib.request.urlopen("""
                    https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}
                """.format(
                    API_TOKEN = 'token',
                    CHAT_ID = '-352331363',
                    TEXT = "Do kontsa rabochego dnia ostalos` {}".format(str(time))
                ))
                data.get_yahoo_weather_by_city("Kyiv", Unit.celsius)
                urllib.request.urlopen("""
                    https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}
                """.format(
                    API_TOKEN = 'token',
                    CHAT_ID = '-352331363',
                    TEXT = "Temperatura za bortom:  {}".format(str(data.condition.temperature))
                ))
                break
connection.close()


