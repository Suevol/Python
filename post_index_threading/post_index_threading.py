# -*- coding: utf-8 -*-

#This script will be useful for analysts working with postal items and will help to receive for further processing
#Information about the locality and the corresponding index.

from dbfread import DBF
import threading

def post_region():
    table = DBF('post.dbf', load=True)
    length = len(table) - 1
    a = 0
    file = open('region.txt', 'a')
    while a <= length:
        element = table.records[a]
        region = element['REGION']
        if region == '':
            region = 'регион не указан'
        file.write(region + '\n')
        print('Обработан регион. Название региона: {}, номер элемента: {}'.format(region, a))
        a += 1
    file.close()

def post_city():
    table = DBF('post.dbf', load=True)
    length = len(table) - 1
    a = 0
    file = open('city.txt', 'a')
    while a <= length:
        element = table.records[a]
        city = element['CITY']
        if city == '':
            city = 'город не указан'
        file.write(city + '\n')
        print('обработан город. Название города: {}, номер элемента: {}'.format(region, a))
        a += 1
    file.close()

def post_index():
    table = DBF('post.dbf', load=True)
    length = len(table) - 1
    a = 0
    file = open('index.txt', 'a')
    while a <= length:
        element = table.records[a]
        index = element['INDEX']
        if index == '':
            index = 'город не указан'
        file.write(index + '\n')
        print('обработан город. Название города: {}, номер элемента: {}'.format(index, a))
        a += 1
    file.close()

# Вызываю функции в виде трех параллельных потоков
t1 = threading.Thread(target=post_region, args=())
t2 = threading.Thread(target=post_index, args=())
t3 = threading.Thread(target=post_city, args=()) 

t1.start()    
t2.start()    
t3.start()    








    

   


    

    
    
