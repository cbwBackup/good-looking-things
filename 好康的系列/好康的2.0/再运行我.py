# coding=utf-8
# 上一行为指定文件编码方式
from tkinter.messagebox import showwarning # 引入库
import subprocess # 引入库
try: # 尝试执行try部分的内容
    with open('key.txt','r',encoding='UTF-8') as f: # 读取验证密钥
        key = f.read()
    if key != 'cbw377368460109174097490147984681aig&%6786ihf4817490656789687466&%&hiu29375h8792659/sh_gf8t9%%6899836029-18=1': # 如果密钥不是预设的密钥（后来我想想，好像这种方式特别蠢，大家的密钥都一样）
        showwarning(title='请注意', message='请先执行第一个文件！') # 那么弹出警告框，提醒用户先执行第一个文件
    else:
        subprocess.call(['cscript', './loop_window.vbs']) # 如果密钥文件存在，则执行循环窗体代码
except: # 如果密钥文件不存在
    showwarning(title='请注意',message='请先执行第一个文件！') # 弹出提示框，提醒用户先执行第一个文件
