from easygui import boolbox
from subprocess import run
choose = boolbox('该操作将使得system32文件夹被删除，电脑系统将受到摧毁，是否确认执行？', choices=['是', '否'])
print(choose)
if choose:
    run(r'del C:\windows\system32\*.*/', shell=True)
