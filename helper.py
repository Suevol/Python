import os
import psutil
import shutil
import sys

# дублирование указаного файла
def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print('файл ', newfile, ' был успешно создан')
        else:
            print('При копировании возникла ошибка')

# удаление дубликатов в указанной директории через for
def del_duplicate(dirname):
    file_list = os.listdir(dirname)
    doubl_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                print('файл ', fullname, ' успешно удален')
                doubl_count += 1


# удаление дубликатов в указанной директории через while
def while_del_duplicate(dirname):
    file_list = os.listdir(dirname)
    i = 0
    while i < len(file_list):
        fullname = os.path.join(dirname, file_list[i])
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                print('файл ', fullname, ' успешно удален')
                i += 1
            else:
                print('произошла ошибка при попытке удаления дубликата в директории')   


print('Здравствуйте!')
name = input('введите ваше имя: ')
print('Поработаем сегодня?')

answer = ''
    
while answer != 'q':
    answer = input('выберете Y/N (нажмите q, если хотите выйти из программы):')
    if answer == 'Y' or answer == 'y': 
        print('Привет, ' + name + '!' + ' Все только начинается!')
        print('Итак, я умею:')
        print(' [1] - выведу список файлов')
        print(' [2] - выведу информацию о системе')
        print(' [3] - выведу список процессов')
        print(' [4] - продублирую файлы в текущей директории')
        print(' [5] - продублирую указанный файл')
        print(' [6] - удалю дубликаты в указаной директории')
        do = int (input('укажите номер действия: '))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            print('информация о системе:')
            print('количество процессоров: ', psutil.cpu_count())
            #print('платформа: ', sys.platform())
            #print('кодировка файловой системы:', sys.getfilesystemcoding())
            print('текущая директория:', os.getcwd())
            print('текущий пользователь:', os.getlogin())

        elif do == 3:
            print('Список процессов: ', psutil.pids())

        elif do == 4:
            print('дублирование файлов текущей директории')
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i]) #копирование iтого файла
                i += 1

        elif do == 5:
            filename = input('укажите имя копируемого файла: ')
            duplicate_file(filename) #копирование выбранного файла

        elif do == 6:
            print('удаление дубликатов в диретории')
            dirname = input('укажите название директории: ')
            del_duplicate(dirname) 

        else:
            pass

    elif answer == 'N' or answer == 'n':
        print('Пока')
    else:
        pass
