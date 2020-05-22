# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
t1 = argv[1]
ignore = ['duplex', 'alias', 'Current configuration']
with open(t1, 'r') as t1:
    for line in t1:
        if line.startswith("!"): #and (not any([word in line for word in ignore])):
          continue
        else:
           for match in ignore:
             if match in string:
               break
            else:
                print(line.strip('\n'))