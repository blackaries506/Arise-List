import random as rand
from colorama import Fore,Style,Back
import time
import os
print(Fore.LIGHTGREEN_EX+'Hi bro am BlaCK Aries')
print(Fore.CYAN+'<<>>'*20)
print(Fore.LIGHTGREEN_EX+'you should be great account')
print(Fore.CYAN+'<<>>'*20)
code =23122006
pin=int(input(Fore.LIGHTGREEN_EX+"Enter Pass code >>>"))
if pin == code :
            print(Fore.CYAN + '<<>>' * 20)
            aaa = input(Fore.LIGHTGREEN_EX + 'Entre victam name : ')
            print(Fore.CYAN + '<<>>' * 20)
            os.system('clear')
            print(Fore.YELLOW + '       ')
            os.system('figlet Aries-list')
            print(Fore.BLUE + 'By : Black Aries')
            print(Fore.LIGHTBLUE_EX + '       ')
            print(Fore.LIGHTBLACK_EX + '-' * 29)
            file = open(aaa + '.txt', 'w')
            aa = set([])
            oio = set([])
            # iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
            kk = 1
            while True:
                b = input(Fore.LIGHTBLACK_EX + 'Entre {} : '.format(kk))
                if b == 'i am done':
                    print('\033[3;36m')
                    file.close()
                    qq = open(aaa + '.txt', 'r')
                    ll = len(qq.readlines())
                    os.system('printf "\033[3;31m"')
                    print('-' * 60)
                    print('>> {} Passwords in ---> {} '.format(ll, aaa + '.txt'))
                    print('-' * 60)
                    break;
                aa.add(b)
                for i in aa:
                    if len(i) >= 6 and i not in oio:
                        oio.add(i)
                        file.write(i)
                        file.write('\n')
                    # for o in iio:
                    #   uau='{}{}'.format(i,o)
                    #  ubu='{}{}{}'.format(o,i,o)
                    # ucu='{}{}{} '.format(i,o,i)
                    # if len(uau)>= 6:
                    # file.write(uau)
                    #  file.write('\n')
                    # if len(ubu) >= 6 and ubu != uau :
                    # file.write(ubu)
                    # file.write('\n')
                    # if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                    #  file.write(ucu)
                    #  file.write('\n')
                    c = b + i
                    d = i + b
                    if len(c) >= 6:
                        file.write(c)
                        file.write('\n')
                    if c != d and len(d) >= 6:
                        file.write(d)
                        file.write('\n')
                kk = int(kk) + 1
                print('-' * 40)
