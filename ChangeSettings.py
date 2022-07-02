import tkinter.messagebox
from ctypes import windll
from os import system, path
from sys import executable, argv, version_info
from time import sleep ,asctime
from logging import *

try:
    import easygui as eg

except:
    tkinter.messagebox.showerror('RingtoneSystemforClass 设置中心', ' [CRITICAL] 错误码 7.')

system('title RingtoneSystemforClass 设置中心 [ 正在启动 ]')
def isAdmin():
    if 'C:' in path.abspath(argv[0]):
        try:
            return windll.shell32.IsUserAnAdmin()

        except:
            return False

    else:
        return True


def ReadSettings():
    try:
        f = open('Settings/breakTime_1.txt','r')
        originalBreakTime_1 = f.read()

        f = open('Settings/breakTime.txt','r')
        originalBreakTime = f.read()

        f = open('Settings/customTime.txt','r')
        originalCustomTime = f.read()

        f = open('Settings/programOpenTime.txt','r')
        originalProgramOpenTime = f.read()

        f = open('Settings/whenToUse.txt','r')
        originalWhenToUse = f.read()

        f = open('Settings/yNPrintDebugLog.txt','r')
        originalyNPrintDebugLog = f.read()

        f.close()

        return [originalBreakTime,originalBreakTime_1,originalWhenToUse,originalCustomTime,originalProgramOpenTime,originalyNPrintDebugLog]

    except:
        tkinter.messagebox.showerror('RingtoneSystemforClass 设置中心', ' [CRITICAL] 错误码 2.')
        exit()

def WriteSettings(fieldValues):
    try:
        f = open('Settings/breakTime_1.txt','w')
        f.write(fieldValues[1])

        f = open('Settings/breakTime.txt','w')
        f.write(fieldValues[0])

        f = open('Settings/customTime.txt','w')
        f.write(fieldValues[3])

        f = open('Settings/programOpenTime.txt','w')
        f.write(fieldValues[4])

        f = open('Settings/whenToUse.txt','w')
        f.write(fieldValues[2])

        f = open('Settings/yNPrintDebugLog.txt','w')
        f.write(fieldValues[5])

        f.close()
    
    except:
        tkinter.messagebox.showerror('RingtoneSystemforClass 设置中心', ' [CRITICAL] 错误码 8.')
        exit()

def editSettings():
    msg = '填写下面设置以更改 RingtoneSystemforClass 参数\n如果你不知道如何更改, 请关闭此窗口, 然后再弹出的窗口中选择 "查看更改帮助信息"\n注意: 字符串部分请使用双引号!'
    title = "RingtoneSystemforClass 设置中心"
    fieldNames = ["课表1", "课表2", "何时使用课表2", "自定义时间", "程序开启时间","显示调试信息"]
    fieldValues = ReadSettings()
    fieldValues = eg.multenterbox(msg, title, fieldNames, fieldValues)
    if tkinter.messagebox.askyesno('RingtoneSystemforClass 设置中心', '确定保存吗?'):
        WriteSettings(fieldValues)
        if tkinter.messagebox.askyesno('RingtoneSystemforClass 设置中心', '需要重启 RingtoneSystemforClass 才能使更改生效, 现在重启吗?'):
            system('Reload\Reload.cmd >nul')

def readHelpFile():
    f = open('Help/helpFile.txt','r')
    helpFile = f.read()
    f.close()
    eg.codebox(msg='以下为更改设置所需的帮助信息.',title='RingtoneSystenforClass 设置中心',text=helpFile)

if version_info[0] < 3:
    system('color 47')
    system('title RingtoneSystemforClass 设置中心 [ 遇到错误 ]')
    critical('[{0}] [CRITICAL] 错误码 3. 程序将退出...'.format(asctime()))
    sleep(5)
    exit()


elif isAdmin():
    system('title RingtoneSystemforClass 设置中心')
    while 1:
        userChoice = eg.choicebox(msg='请选择一项',title='RingtoneSystemforClass 设置中心',choices=['查看更改帮助信息','更改设置'],preselect=0)
        if userChoice == None:
            break

        elif userChoice == '查看更改帮助信息':
            readHelpFile()

        else:
            editSettings()

else:
    windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
