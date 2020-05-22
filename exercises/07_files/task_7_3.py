# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
# tmp = '{:<8} {1} {2:>8}'

# with open('CAM_table.txt', 'r') as mtab:
#     for string in mtab:
#         if 'DYNAMIC' in string:
#             string = string.split()
#             print(tmp.format(string[0],string[1],string[3]))
#         else:
#             continue

# f = open('CAM_table.txt', 'r')
# for L1 in f:
#     list = L1.rstrip().split()
#     if (L1 in L1[0].isdigit()):
#         print(L1.rstrip())
# f.close()

t1 = '{0:<8}  {1} {2:>8}'

with open('CAM_table.txt','r') as mac_table:
    for string in mac_table:
        if 'DYNAMIC' in string:
            string = string.split()
            print(t1.format(string[0],string[1],string[3]))



        else:
            continue