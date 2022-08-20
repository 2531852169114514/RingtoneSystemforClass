f = open('help/aboutThisProject.txt')
about = f.read()
f.close()

errorInformation = {
    1:'',
    2:'错误: 程序无法读取设置.\n可能的原因: 1.更改了设置文件夹名称\n                 2.设置文件夹里的内容损坏或被删除\n                 3.无设置文件夹\n解决方法: 1.重新安装 RingtoneSystemforClass',
    3:'错误: Python 版本错误. \n可能的原因: 1.Python 版本低于 3.\n解决方法: 1.安装 Python 3 或以上版本.',
    4:'错误: customeTime 填写错误.\n可能的原因: 1.customeTime 填写错误.\n解决方法: 1.正确填写 customeTime.',
    5:'',
    6:'错误: 未知.\n可能的原因: 1.强制退出程序.\n                 2.程序代码出现错误.\n解决方法: 1.重新安装 RingtoneSystemforClass',
    7:'',
    8:'错误: 数值填写不正确.\n可能的原因: 数值填写不正确.\n解决方法: 正确填写数值.',
    9:'错误: 只能通过另一个程序来运行此程序.\n可能的原因: 只能通过另一个程序来运行此程序.\n解决方法: 1.通过另一个程序来运行此程序.',
    10:'错误: 输入的错误码不正确.\n可能的原因: 1.输入的错误码不正确.\n解决方法: 1.正确填写错误码.',
    11:'错误:  输入的错误码不是数字.\n可能的原因:  输入的错误码不是数字.\n解决方法: 正确输入错误码.',
}


import tkinter.messagebox
from ctypes import windll
from os import system, path
from sys import executable, argv

try:
    import easygui as eg

except:
    system('title RingtoneSystemforClass [ 正在安装模块: 第 1 个, 共 1 个 ]')
    system('pip install easygui')

    import easygui as eg

def checkError():
    while 1:
        errorCode = eg.enterbox(msg='请输入你遇到的错误码.', title='RingtoneSystemforClass 运行中心')
        if errorCode == None:
            break

        try:
            errorCode = int(errorCode)
            if errorCode > 0 and errorCode < 12:
                tkinter.messagebox.showinfo('RingtoneSystemforClass 运行中心', '错误码: ' + str(errorCode) + '\n' + errorInformation.get(errorCode))

            else:
                tkinter.messagebox.showerror('RingtoneSystemforClass 运行中心','错误码 10.')

        except:
            tkinter.messagebox.showerror('RingtoneSystemforClass 运行中心','错误码 11.')

def isAdmin():
    if 'C:' in path.abspath(argv[0]):
        try:
            return windll.shell32.IsUserAnAdmin()

        except:
            return False

    else:
        return True


# def readSettings():
#     try:
#         with open('settings/settings.txt','r') as f:
#             originalSettings = eval(f.read())

#         originalBreakTime = originalSettings[0]
#         originalBreakTime_1 = originalSettings[1]
#         originalWhenToUse = originalSettings[2]
#         originalCustomTime = originalSettings[3]
#         originalyNPrintDebugLog = originalSettings[4]

#         return [[str(originalBreakTime),str(originalBreakTime_1),str(originalWhenToUse),str(originalCustomTime),str(originalyNPrintDebugLog)]]

#     except:
#         tkinter.messagebox.showerror('RingtoneSystemforClass 运行中心', ' [CRITICAL] 错误码 2.')
#         exit()

# def writeSettings(fieldValues):
#     try:
#         with open('settings/settings.txt','w') as f:
#             f.write(str(fieldValues))

#     except:
#         tkinter.messagebox.showerror('RingtoneSystemforClass 运行中心', ' [CRITICAL] 错误码 8.')
#         exit()  

def editSettings():
    # msg = '填写下面设置以更改 RingtoneSystemforClass 参数\n如果你不知道如何更改, 请关闭此窗口, 然后再弹出的窗口中选择 "查看更改帮助信息"\n注意: 字符串部分请使用双引号!'
    # title = "RingtoneSystemforClass 运行中心"
    # fieldNames = ["课表1", "课表2", "何时使用课表2", "自定义时间", "显示调试信息"]
    # fieldValues = readSettings()
    # fieldValues = eg.multenterbox(msg, title, fieldNames, fieldValues)
    # if tkinter.messagebox.askesno('RingtoneSystemforClass 运行中心', '确定保存吗?'):
    #     writeSettings(fieldValues)
    system('settings\settings.txt')
    if tkinter.messagebox.askyesno('RingtoneSystemforClass 运行中心', '现在运行 RingtoneSystemforClass 查看更改效果吗?'):
        userChoice_2 = eg.choicebox(
            msg='请选择.',
            title='RingtoneSystemforClass 运行中心',
            choices=['以自动打铃方式运行','以手动打铃方式运行'],
            preselect=0
        )

        if userChoice_2 == None:
            pass

        elif userChoice_2 == '以自动打铃方式运行':
            cmd = ''

        else:
            cmd = '-manualOperation'

            system('start Main.py ' + cmd)

def readHelpFile():
    f = open('/File.txt','r')
    helpFile = f.read()
    f.close()
    eg.codebox(msg='以下为更改设置所需的帮助信息.',title='RingtoneSystenforClass 运行中心',text=helpFile)

while 1:
    userChoice_1 = eg.choicebox(
        msg='请选择.',
        title='RingtoneSystemforClass 运行中心',
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
        userChoice_2 = eg.choicebox(
            msg='请选择.',
            title='RingtoneSystemforClass 运行中心',
            choices=['以自动打铃方式运行','以手动打铃方式运行'],
            preselect=0
        )

        if userChoice_2 == None:
            pass

        elif userChoice_2 == '以自动打铃方式运行':
            cmd = ''

        else:
            cmd = '-manualOperation'

        system('start Main.py ' + cmd)

    elif userChoice_1 == '修改 RingtoneSystemforClass 设置':
        if isAdmin():
            while 1:
                userChoice = eg.choicebox(msg='请选择.',title='RingtoneSystemforClass 运行中心',choices=['查看更改帮助信息','更改设置'],preselect=0)
                if userChoice == None:
                    break

                elif userChoice == '查看更改帮助信息':
                    readHelpFile()

                else:
                    editSettings()

        else:
            windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)

    elif userChoice_1 == 'RingtoneSystemforClass 错误码查询':
        checkError()

    else:
        choice = eg.buttonbox(
        msg=about,
        title='RingtoneSystemforClass 计算中心',
        choices=['检查更新','确定']
        )

        if choice == '检查更新':
            system('CheckUpdate.pyw')