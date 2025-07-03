from configDatabase import databases
from time import sleep
import requests
from bs4 import BeautifulSoup
import mysql.connector
import random
from datetime import datetime
from Utils.password import generate_md5


def createDataCar():
    mydb = mysql.connector.connect(
        host=databases.get("HOST"),
        port=databases.get("PORT"),
        user=databases.get("USER"),
        password=databases.get("PASSWORD"),
        database=databases.get("DATABASES"),
    )

    mycursor = mydb.cursor()
    lines = open("data.txt","r",encoding="utf-8").readlines()
    for line in lines:
        lis = line.split(",")
        insert = "insert into car_carmodel(picture,name,price) values(%s,%s,%s)"
        tup = (lis[0],lis[1],lis[2].strip())
        mycursor.execute(insert, tup)
    mydb.commit()


createDataCar()

def createDataFavoritees():
    mydb = mysql.connector.connect(
        host=databases.get("HOST"),
        port=databases.get("PORT"),
        user=databases.get("USER"),
        password=databases.get("PASSWORD"),
        database=databases.get("DATABASES"),
    )

    mycursor = mydb.cursor()

    insert = "insert into favorites_favoritemodel(car_id,user_id) values(%s,%s)"
    for index in range(1, 100):
        tup = (random.randint(1, 261), random.randint(1, 10))
        mycursor.execute(insert, tup)
    mydb.commit()

def createDataUser():
    mydb = mysql.connector.connect(
        host=databases.get("HOST"),
        port=databases.get("PORT"),
        user=databases.get("USER"),
        password=databases.get("PASSWORD"),
        database=databases.get("DATABASES"),
    )
    mycursor = mydb.cursor()
    insert = "insert into user_usermodel(name,password,created_at,balance) values(%s,%s,%s,%s)"
    for index in range(1, 11):
        tupe = (f"xiaopan{index}", generate_md5("123456"), datetime.today(), 0.00)
        mycursor.execute(insert, tupe)
    mydb.commit()

def get_proxy():
    data = open(r"proxies.text").readlines()
    data_list = []
    for da in data:
        da = da.replace('\n', '')
        data_list.append({'http': f'http://{da}'})
    proxies = random.choice(data_list)
    return proxies

def getdata():
    lis = []
    for i in range(1,12):
        url = f"https://car.autohome.com.cn/2sc/xiangtan/a0_0msdgscncgpi1ltocsp{i}ex/"
        html = requests.get(url,proxies=get_proxy())
        soup = BeautifulSoup(html.text, 'lxml')
        ul = soup.find(class_='piclist').find_all("li")
        for li in ul:
            if li.text in "line":
                pass
            else:
                lis.append(li)
        sleep(1)
    return lis




