import tkinter.messagebox
from os import system

errorInformation = {
    1:'错误: 模块 pyautogui 或 eyed3 安装错误\n可能的原因: 1.上述模块安装失败\n                 2.Python 安装错误\n解决方法: 1.重新运行 Install.cmd',
    2:'错误: 程序无法读取设置.\n可能的原因: 1.更改了设置文件夹名称\n                 2.设置文件夹里的内容损坏或被删除\n                 3.无设置文件夹\n解决方法: 1.重新安装 RingtoneSystemforClass',
    3:'错误: Python 版本错误. \n可能的原因: 1.Python 版本低于 3.\n解决方法: 1.安装 Python 3 或以上版本.',
    4:'错误: customeTime 填写错误.\n可能的原因: 1.customeTime 填写错误.\n解决方法: 1.正确填写 customeTime.',
    5:'错误: 变量填写错误.\n可能的原因: 变量填写错误.\n解决方法: 正确填写变量',
    6:'错误: 未知.\n可能的原因: 1.强制退出程序.\n                 2.程序代码出现错误.\n解决方法: 1.重新安装 RingtoneSystemforClass',
    7:'错误: 模块 easygui 安装错误\n可能的原因: 1.上述模块安装失败\n                 2.Python 安装错误\n解决方法: 1.重新运行 Install.cmd',
    8:'错误: 数值填写不正确.\n可能的原因: 数值填写不正确.\n解决方法: 正确填写数值.',
    9:'错误: 只能通过另一个程序来运行此程序.\n可能的原因: 只能通过另一个程序来运行此程序.\n解决方法: 1.通过另一个程序来运行此程序.',
    10:'错误: 输入的错误码不正确.\n可能的原因: 1.输入的错误码不正确.\n解决方法: 1.正确填写错误码.',
    11:'错误:  输入的错误码不是数字.\n可能的原因:  输入的错误码不是数字.\n解决方法: 正确输入错误码.',
}

system('title RingtoneSystemforClass 错误排查中心')
try:
    import easygui as eg

except:
    print(errorInformation.get(7))
    exit()

while 1:
    errorCode = eg.enterbox(msg='请输入你遇到的错误码.', title='RingtoneSystemforClass 错误排查中心')

    if errorCode == None:
        break

    try:
        errorCode = int(errorCode)
        if errorCode > 0 and errorCode < 12:
            tkinter.messagebox.showinfo('RingtoneSystemforClass 错误排查中心', '错误码: ' + str(errorCode) + '\n' + errorInformation.get(errorCode))

        else:
            tkinter.messagebox.showerror('RingtoneSystemforClass 错误排查中心','错误码 10.')

    except:
        tkinter.messagebox.showerror('RingtoneSystemforClass 错误排查中心','错误码 11.')