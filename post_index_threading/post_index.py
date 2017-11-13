from dbfread import DBF

#Вывести на экран всю базу
#for record in DBF('post.dbf'):
#    print(record)
#-----------------------------------------------

#Создаю переменную хранящую базу
table = DBF('post.dbf', load=True)

#Поочередно вызываю элементы базы, которые при этом являются словарем (для этого создаю цикл для обхода массива).
#У выбранных элементов, которые представляют из себя вложенный словарь, вызываю необходимое свойство по ключу.
length = len(table) - 1

a = 0
while a <= length:
    #Вызываю отдельный элемент словаря
    element = table.records[a]
    #Вызываю свойство вызванного элемента словаря по искомому ключу
    index = element['INDEX']
    if index == '':
        index = 'индекс не указан'
    #Записываю полученные данные в файл
    file = open('index.txt', 'a')
    file.write(index + '\n')
    file.close()

    region = element['REGION']
    if region == '':
        region = 'регион не указан'
    file = open('region.txt', 'a')
    file.write(region + '\n')
    file.close()

    city = element['CITY']
    if city == '':
        city = 'город не указан'
    file = open('city.txt', 'a')
    file.write(city + '\n')
    file.close()
    print(a)
    a += 1