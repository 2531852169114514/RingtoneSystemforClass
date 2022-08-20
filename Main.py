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


# 无需安装
from os import path, system

system('mode con cols=100')
system('program\\disableX.exe')

try:
    # 无需安装
    from ctypes import POINTER, cast
    from platform import system as checkSys
    from sys import argv, version_info
    from time import localtime, sleep
    from comtypes import CLSCTX_ALL

    # 需要安装
    from logging import (DEBUG, INFO, basicConfig, critical, debug, info, warning)
    from subprocess import STDOUT, check_output
    from easygui import codebox, msgbox
    from psutil import Process, pids
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

except:
    info('正在安装程序运行必须模块...')

    system('title RingtoneSystemforClass [ 正在安装模块: 第 1 个, 共 4 个 ]')
    system('pip install logging -i https://pypi.douban.com/simple')
    print('-' * 80)
    system('title RingtoneSystemforClass [ 正在安装模块: 第 2 个, 共 4 个 ]')
    system('pip install subprocess -i https://pypi.douban.com/simple')
    print('-' * 80)
    system('title RingtoneSystemforClass [ 正在安装模块: 第 3 个, 共 4 个 ]')
    system('pip install easygui -i https://pypi.douban.com/simple')
    print('-' * 80)
    system('title RingtoneSystemforClass [ 正在安装模块: 第 4 个, 共 4 个 ]')
    system('pip install psutil -i https://pypi.douban.com/simple')
    print('-' * 80)
    system('title RingtoneSystemforClass [ 正在安装模块: 第 4 个, 共 4 个 ]')
    system('pip3 install pycaw -i https://pypi.douban.com/simple')

    system('cls')

    from logging import (DEBUG, INFO, basicConfig, critical, debug, info, warning)
    from platform import system as checkSys
    from subprocess import STDOUT, check_output
    from easygui import codebox, msgbox
    from psutil import Process, pids
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

if checkSys() != 'Windows':
    msgbox(msg='不支持的操作系统.\n\n很抱歉, RingtoneSystemforClass 暂不支持除 Windows 的其他版本, 开发者正在适配其它系统.', title='RingtoneSystemforClass', ok_button='确定')
    exit()

try:
    f = open('Settings/yNPrintDebugLog.txt','r')
    yNPrintDebugLog = eval(f.read())
    f.close()
    if bool(yNPrintDebugLog):
        basicConfig(
        level=DEBUG,
        format='[%(asctime)s] %(filename)s (line %(lineno)s) | %(levelname)s > %(message)s',
        # filename='RSC_Log.log',
        # filemode='w',
        )

except:
    basicConfig(
    level=INFO,
    format='[%(asctime)s] %(filename)s (line %(lineno)s) | %(levelname)s > %(message)s'
    )
    warning('错误码 2 ,程序无法读取设置. 不影响程序运行.')

system('title RingtoneSystemforClass [ 正在启动 ]')
with open('help/aboutThisProject.txt','r') as f:
    print(f.read() + '\n')

def Play(playMediaFile):
    info('已下课/到自定义时间/手动打铃.')
    system('title RingtoneSystemforClass [ 检测到事件 ]')
    programPath = path.split(path.realpath( argv[0] ))[0]

    if playMediaFile == None:
        playMediaFile = 'D:\Python\RingtoneSystemForClass\media\Class.mp3'

    debug('播放文件 [{0}]'.format(playMediaFile))
    debug('程序路径:[{0}]'.format(programPath))
    info('正在播放铃声...')

    secs = getDuration(playMediaFile)
    system('program\\ffplay.exe -nodisp -t {0} -autoexit -volume 60 -v quiet {1} >nul'.format(secs,playMediaFile))

    system('title RingtoneSystemforClass')
    info('铃声播放完毕.')

def manualMode():
    userChoice_1 = msgbox(
        msg='点击打铃后, 程序将以默认设置进行打铃.',
        title='RingtoneSystemforClass',
        ok_button='打铃',
    )

    if userChoice_1 == None:
        return True

    else:
        Play(None)

def procExist(processName):
    for pid in pids():
        if Process(pid).name() == processName:
            return pid

def getDuration(file):
    cmd = 'program\\ffprobe.exe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(file)
    output = check_output(
    cmd,
    shell=True,
    stderr=STDOUT
    )
    return float(output)

def criticalPrint(errorCode):
    system('color 47')
    system('title RingtoneSystemforClass [ 遇到错误 ]')
    critical('错误码 {0}, 程序将退出...'.format(str(errorCode)))
    sleep(5)

try:
    if argv[1] == '-manualOperation' or argv[1] == '/manualOperation':
        system('title RingtoneSystemforClass [ 手动打铃模式 ]')
        while 1:
            if manualMode():
                exit()

except:
    pass

info('正在读取设置...')
try:
    with open('settings/settings.txt','r') as f:
        settings = eval(eval(f.read()))

    breakTime = settings[0]
    breakTime_1 = settings[1]
    whenToUse = settings[2]
    customTime = settings[3]
    yNPrintDebugLog = settings[4]

except:
    criticalPrint(2)
    exit()

try:
    system('color 07')
    system('title RingtoneSystemforClass')

    if version_info[0] < 3:
        criticalPrint(3)
        exit()

    timeAdd = str(localtime()[3]) + ',' + str(localtime()[4]) + ',' + str(localtime()[5])
    playMediaFile = customTime.get(timeAdd)
    if playMediaFile != None:
        if playMediaFile.split(".")[1] == 'mp3' or playMediaFile.split(".")[1] == 'wav':
            if len(playMediaFile.split('|')) == 1:
                criticalPrint(4)
                exit()
                        
    info('正在运行...')
    
    # 设置解除静音
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(0, None)

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
            exit()

        elif int(breakTime1.split(',')[0]) < localtime()[3]:
            item += 1
            info('正在跳过已超出时间的课表时间... 已跳过: ' + str(item))

        elif timeAdd == breakTime1 or customTime.get(timeAdd) != None:  # 检测是否达到上下课时间
            if customTime.get(timeAdd) == None:  # 是否有自定义音乐
                playMediaFile = 'D:\Python\RingtoneSystemForClass\media\Class.mp3'

            else:
                playMediaFile = customTime.get(timeAdd)

            Play(playMediaFile)
            item += 1

except Exception as exception:
    codebox(msg= '程序遇到了严重错误, 请将下方的错误报告反馈给开发者, 开发者对此的错误表示歉意.', title= 'RingtoneSystemforClass 错误报告', text= '错误文件: {0}\n错误行数: {1}\n错误报告: {2}'.format(str(exception.__traceback__.tb_frame.f_globals["__file__"]),str(exception.__traceback__.tb_lineno),str(exception),))
