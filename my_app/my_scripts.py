#for work with json
import requests
import json 
import time 
import urllib

#for email
#поменять ключ сервиса
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#работа с инн
def my_inn(a_a):
    if len(a_a) == 10:
        my_str = 'https://api-fns.ru/api/egr?req=' + a_a + '&key=14f39eb135e66'
        my_request = requests.get(my_str)
        my_json = json.loads(my_str.text)
        return str(my_json["items"]["ЮЛ"]["НаимСокрЮЛ"])
    else: 
        my_str = 'https://api-fns.ru/api/egr?req=' + a_a + '&key=14f39eb135e66'
        my_request = requests.get(my_str)
        my_json = json.loads(my_str.text)
        return str(my_json["items"]["ИП"]["ФИОПолн"])

#работа с почтой
#поменять почту и пароль
def my_mail(m_login, m_password):
    msg = MIMEMultipart()
    to_email = login
    
    message = 'Логин: ' + m_login + ', пароль: ' + m_password
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    mail_for_latter = ''
    password_for_letter = ''
    server.login(mail_for_latter, password_for_letter)
    server.sendmail(mail_for_latter, m_login, msg.as_string())
    server.quit()



#smsc ru - сервис для отправки смс 
def mysms(a_a):
    #заполните
    login = ''       
    password = ''     
    sender = ''
    total_price

    url = "http://smsc.ru/sys/send.php?login=%s&psw=%s&phones=%s&mes=%s&cost=%d&sender=%s&fmt=3" % (login, password, a_a, 'заказ отменен', total_price, sender)
    urllib.urlopen(url)
    











