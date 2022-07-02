title = '''
=========================================
关于
-----------------------------------------
RingtoneSystemforClass (RSC)
由某位学生无私制作
版本 正式版 v 1.3:
     本体程序 v 3.1.0.220629
     其他文件 v 1.1.1.220629
     单文件版 Potplayer v 1.7.17105
=========================================
Tips:
    若电脑上有杀毒软件, 请在运行本软件前
    先在杀毒软件白名单上添加本目录下的 
    Program/Potplayer.exe (真的不是病毒), 
    否则会造成本程序无法正常运行!
=========================================
'''


#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#                 ( 虽说是屎山代码hhh )



import wave
from contextlib import closing
from ctypes import windll
from logging import *
from os import path, system
from sys import argv, executable, version_info
from time import localtime, sleep

import easygui as eg
import psutil

try:
    import eyed3
    from pyautogui import hotkey
    
except:
    system('color 47')
    system('title RingtoneSystemforClass [ 遇到错误 ]')
    critical('错误码 1, 程序将退出...')
    sleep(5)
    exitNotWithinTheProgram = False
    exit()

system('mode con cols=100')

try:
    f = open('Settings/yNPrintDebugLog.txt','r')
    yNPrintDebugLog = eval(f.read())
    f.close()
    if bool(yNPrintDebugLog):
        basicConfig(
        level=DEBUG,
        format='[%(asctime)s] %(filename)s (line %(lineno)s) | %(levelname)s > %(message)s'
        )
    
    else:
        basicConfig(
        level=INFO,
        format='[%(asctime)s] %(filename)s (line %(lineno)s) | %(levelname)s > %(message)s'
        )

except:
    pass

system('title RingtoneSystemforClass [ 正在启动 ]')
print(title)

def Play(playMediaFile,audioLength,programOpenTime):
    info('已下课/到自定义时间/手动打铃.')
    system('title RingtoneSystemforClass [ 检测到事件 ]')

    programPath = path.split(path.realpath( argv[0] ))[0]
    if playMediaFile == None:
        playMediaFile = 'D:\Python\RingtoneSystemForClass\Media\Class.mp3'
    playProgram  = programPath + '\Program\Potplayer.exe ' # 生成代码
    code = 'start ' + playProgram + playMediaFile + ' /autoplay'

    debug('播放文件 [{0}]'.format(playMediaFile))
    debug('程序路径:[{0}]'.format(programPath))
    debug('播放代码: [{0}]'.format(code))
    info('正在播放铃声... 程序启动可能较慢, 请勿触碰键盘鼠标.')

    system(code)

    if audioLength == None:
        if playMediaFile.split(".")[1] == 'wav':
            with closing(wave.open(playMediaFile, 'r')) as f:
                audioLength = f.getnframes() / float(f.getframerate())

        elif playMediaFile.split(".")[1] == 'mp3':
            audioLength = eyed3.load(playMediaFile).info.time_secs

    sleep(audioLength + programOpenTime)
    hotkey('alt','f4')
    system('title RingtoneSystemforClass')
    info('铃声播放完毕.')

def isAdmin():
    try:
        return windll.shell32.IsUserAnAdmin()

    except:
        return False

def manualMode():
    f = open('Settings/programOpenTime.txt','r')
    programOpenTime = int(f.read())
    debug('正在读取设置文件 : programOpenTime.txt')

    userChoice_1 = eg.buttonbox(
        msg='点击"打铃"将手动打铃.\n点击"退出"将退出程序.',
        title='RingtoneSystemforClass',
        choices=['退出','打铃'],
        default_choice='打铃',
        cancel_choice='退出'
    )

    if userChoice_1 == '打铃':
        Play(None,None,programOpenTime)

    else:
        return True

def procExist(process_name):
    for pid in psutil.pids():
        if psutil.Process(pid).name() == process_name:
            return pid

if isinstance(procExist('pythonw.exe'),int):
    warning('程序检测到你可能是在 IDLE 环境下运行的, 继续可能会使程序工作异常, 是否继续? ( 是(在新弹出的窗口)按下任意键, 否关闭 IDLE 窗口, 你可能需要再确定一次)')
    system('pause >nul')

else:
    pass

if isAdmin(): # 代码
    f = open('Settings/operatingParameter.txt','r')
    yNManualMode = f.read()
    f.close()

    if int(yNManualMode):
        system('title RingtoneSystemforClass [ 手动打铃模式 ]')
        while 1:
            if manualMode():
                exitNotWithinTheProgram = False
                exit()

    info('正在读取设置...')
    try:
        f = open('Settings/breakTime_1.txt','r')
        breakTime_1 = eval(f.read())
        debug('正在读取设置文件 : breakTime_1.txt')

        f = open('Settings/breakTime.txt','r')
        breakTime = eval(f.read())
        debug('正在读取设置文件 : breakTime.txt')

        f = open('Settings/customTime.txt','r')
        customTime = eval(f.read())
        debug('正在读取设置文件 : customTime.txt')

        f = open('Settings/programOpenTime.txt','r')
        programOpenTime = int(f.read())
        debug('正在读取设置文件 : programOpenTime.txt')

        f = open('Settings/whenToUse.txt','r')
        whenToUse = eval(f.read())
        debug('正在读取设置文件 : whenToUse.txt')
        f.close()

    except:
        system('color 47')
        system('title RingtoneSystemforClass [ 遇到错误 ]')
        critical('错误码 2, 程序将退出...')
        sleep(5)
        exitNotWithinTheProgram = False
        exit()

    try:
        exitNotWithinTheProgram = True
        system('color 07')
        system('title RingtoneSystemforClass')

        if version_info[0] < 3:
            system('color 47')
            system('title RingtoneSystemforClass [ 遇到错误 ]')
            critical('错误码 3, 程序将退出...')
            sleep(5)
            exitNotWithinTheProgram = False
            exit()

        info('正在检测设置变量类型...')
        # 检测变量是否为初始类型
        if str(type(breakTime)) == "<class 'list'>" and str(type(breakTime_1)) == "<class 'list'>" and str(type(customTime)) == "<class 'dict'>" and  str(type(programOpenTime)) == "<class 'int'>":
            timeAdd = str(localtime()[3]) + ',' + str(localtime()[4]) + ',' + str(localtime()[5])
            playMediaFile = customTime.get(timeAdd)
            if playMediaFile != None:
                if playMediaFile.split(".")[1] == 'mp3' or playMediaFile.split(".")[1] == 'wav':
                    if len(playMediaFile.split('|')) == 1:
                        system('color 47')
                        system('title RingtoneSystemforClass [ 遇到错误 ]')
                        critical('错误码 4, 程序将退出...')
                        sleep(5)
                        exitNotWithinTheProgram = False
                        exit()
                        
            info('正在运行...')
            item = 0
            while 1:
                system('title RingtoneSystemforClass [ 自动打铃模式 ] [当前时间 : {0}]'.format(str(localtime()[3]) + ':' + str(localtime()[4]) + ':' + str(localtime()[5])))
                timeAdd = str(localtime()[3]) + ',' + str(localtime()[4]) + ',' + str(localtime()[5])
                if whenToUse.get(localtime()[6]) == 'use':  # 检测要用哪一个课表
                    breakTime1 = breakTime_1[item]
                    whereToGet = 0

                else:
                    breakTime1 = breakTime[item]
                    whereToGet = 1

                if breakTime1 == 'End':  # 检测是否放学
                    system('title RingtoneSystemforClass [ 检测到事件 ]')
                    info('当前已放学. 程序将退出...')
                    sleep(5)
                    exitNotWithinTheProgram = False
                    exit()

                elif int(breakTime1.split(',')[0]) < localtime()[3]:
                    item += 1
                    info('正在跳过已超出时间的课表时间... 已跳过: ' + str(item))

                elif timeAdd == breakTime1 or customTime.get(timeAdd) != None:  # 检测是否达到上下课时间
                    if customTime.get(timeAdd) == None:  # 是否有自定义音乐
                        playMediaFile = 'D:\Python\RingtoneSystemForClass\Media\Class.mp3'

                    else:
                        playMediaFile = customTime.get(timeAdd)

                    if playMediaFile.split(".")[1] == 'mp3' or playMediaFile.split(".")[1] == 'wav':
                        audioLenngth = None

                    else:
                        audioLenngth = int(playMediaFile.split('|')[1])

                    Play(playMediaFile,audioLenngth,programOpenTime)
                    item += 1

        else:
            system('color 47')
            system('title RingtoneSystemforClass [ 遇到错误 ]')
            critical('错误码 5, 程序将退出...')
            sleep(5)
            exitNotWithinTheProgram = False
            exit()

    except:
        if exitNotWithinTheProgram:
            system('color 47')
            system('title RingtoneSystemforClass [ 遇到错误 ]')
            error('错误码 6, 是否重启程序?')
            yNrestart = system('choice /n /c yN /t 30 /d N /m "(30s) [y/N] >"')
            if yNrestart == 1:
                system('title RingtoneSystemforClass [ 正在重启 ]')
                info('正在重新启动 ...')
                exit(system('start Main.py'))

else:
    info('正在获取管理员权限, 请稍后...')
    windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
