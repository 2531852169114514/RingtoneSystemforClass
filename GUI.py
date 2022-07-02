about = '''RingtoneSystemforClass (RSC)
由某位学生无私制作
版本 正式版 v 1.3:
     本体程序 v 3.1.0.220629
     其他文件 v 1.1.1.220629
     单文件版 Potplayer v 1.7.17105

Tips:
    若电脑上有杀毒软件, 请在运行本软件前
    先在杀毒软件白名单上添加本目录下的 
    Program/Potplayer.exe (真的不是病毒), 
    否则会造成本程序无法正常运行!
'''

from os import system
import easygui as eg

system('title RingtoneSystemforClass')

while 1:
    userChoice_1 = eg.choicebox(
        msg='请选择.',
        title='RingtoneSystemforClass',
        choices=[
            '运行 RingtoneSystemforClass 主程序部分',
            '修改 RingtoneSystemforClass 设置',
            'RingtoneSystemforClass 错误码查询',
            '关于 RingtoneSystemforClass'
            ],
        preselect=0
        )

    if userChoice_1 == None:
        exit()

    elif userChoice_1 == '运行 RingtoneSystemforClass 主程序部分':
        while 1:
            userChoice_2 = eg.choicebox(
                msg='请选择.',
                title='RingtoneSystemforClass',
                choices=['以自动打铃方式运行','以手动打铃方式运行'],
                preselect=0
            )

            if userChoice_2 == None:
                break

            elif userChoice_2 == '以自动打铃方式运行':
                f = open('Settings/operatingParameter.txt','w')
                f.write('0')
                f.close()

            else:
                f = open('Settings/operatingParameter.txt','w')
                f.write('1')
                f.close()

            system('Main.py')
            print('\n-----------------------------------------\n程序运行结束\n-----------------------------------------')
            break

    elif userChoice_1 == '修改 RingtoneSystemforClass 设置':
        system('ChangeSettings.py')

    elif userChoice_1 == 'RingtoneSystemforClass 错误码查询':
        system('CheckError.py')

    else:
        eg.codebox('关于 RingtoneSystemforClass','RingtoneSystemforClass',about)
