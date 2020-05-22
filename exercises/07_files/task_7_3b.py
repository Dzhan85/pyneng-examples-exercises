# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
t1 = '{0:<8}  {1} {2:>8}'
vout = {}
vlist = []

with open('CAM_table.txt','r') as mctab:
    for string in mctab:
        if 'DYNAMIC' in string:
            string = string.split()
            vout[string[0]] = string
            vlist.append(int(string[0]))
        else:
            continue 
    vlist.sort()
vlan = input('Input VLAN: ')
if vout.get(vlan) is not None:
        print(t1.format(vout[str(vlan)][0],vout[str(vlan)][1],vout[str(vlan)][3]))
else:
    print('Invalid VLAN')