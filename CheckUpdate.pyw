LASTUPDATETIME = '2022-08-20T23:59:59Z'

from asyncio import get_event_loop
from json import loads
from time import mktime, strptime
import tkinter
from tkinter.messagebox import askretrycancel, askyesno, showwarning, showinfo
from webbrowser import open as openBrowser
from os import system

try:
    from pyppeteer import launch

except:
    showwarning('RingtoneSystemforClass 更新程序', '程序缺少必要的模块, 点击"确定"安装.')
    
    system('pip install pyppeteer')
    from pyppeteer import launch

    showinfo('RingtoneSystemforClass 更新程序','安装完毕.')

async def main(url,LASTUPDATETIME):
    while 1:
        try:
            # 开启浏览器并进行基本配置
            browser = await launch()
            page = await browser.newPage()
            await page.goto(url)

            # 爬取更新时间
            projectInforMation = await page.querySelector('body > pre')
            projectInforMation = await projectInforMation.getProperty('textContent')
            projectInforMation = await projectInforMation.jsonValue()
            
            # 关闭窗口和浏览器
            await page.close()
            await browser.close()

            # 对信息进行处理
            projectInforMation = loads(projectInforMation)
            updateTime = projectInforMation.get('updated_at')

            if mktime(strptime(LASTUPDATETIME, '%Y-%m-%dT%H:%M:%SZ')) < mktime(strptime(updateTime, '%Y-%m-%dT%H:%M:%SZ')):
                result = askyesno('RingtoneSystemforClass 更新程序', '发现新版本.\n现在跳转至 Github Releases 页面吗?')
                if result:
                    openBrowser('https://github.com/2531852169114514/RingtoneSystemforClass/releases', 0)

            else:
                showinfo('无更新.')
            
            exit()
            

        except Exception as exception:
            result = askretrycancel('RingtoneSystemforClass 更新程序', '无法从 Github 获取信息.\n重新尝试吗?\n\n错误代码: ' + str(exception))
            if result == False:
                exit()

# 基本信息
loop = get_event_loop()
loop.run_until_complete(main("https://api.github.com/repos/2531852169114514/RingtoneSystemforClass",LASTUPDATETIME))
loop.close()
