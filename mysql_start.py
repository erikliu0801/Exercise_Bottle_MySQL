#!/usr/bin/python3

import pymysql
import requests
import json

HTTP_WaterLevel = 'http://odata.wra.gov.tw/v4/RealtimeWaterLevel?$skip=0&$top=1000'
# [即時水位資料](https://data.gov.tw/dataset/25768)

# def HTTP_GET(HTTP):
#     r = requests.get(HTTP)
#     _dict = json.loads(r.text)
#     if r.status_code == 200:
#         return 1, _dict
#     else:
#         return 0, _dict

# get data in json type
r = requests.get(HTTP_WaterLevel)
_dict = json.loads(r.text)
print(r.status_code)
value_dict=_dict['value']
   
# db need to create first
# $ mysql -u root -p
# mysql/ create database opendata
db = pymysql.connect(host='localhost',port=3306,user='root',password='1234',db='opendata',charset='utf8')

# Drop table if exists
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS waterlevel")
sql = """CREATE TABLE waterlevel (
         id int,
         StationIdentifier char(20),
         RecordTime char(50),
         WaterLevel float)"""
cursor.execute(sql)

# Insert data
cursor = db.cursor()
for _id, fields in enumerate(value_dict):
    _StationIdentifier = fields['StationIdentifier']
    _RecordTime = fields['RecordTime']
    _WaterLevel = fields['WaterLevel']
    sql = "INSERT INTO waterlevel(id, StationIdentifier, RecordTime, WaterLevel)             VALUES('%d','%s','%s','%e')" % (_id,_StationIdentifier,_RecordTime,_WaterLevel)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
db.close()