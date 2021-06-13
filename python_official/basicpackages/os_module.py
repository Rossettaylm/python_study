import glob
import os
import shutil
import sys

#  (1) directory operation
print(os.getcwd())  # return the current working directory
os.chdir('/home/rossetta')  # change current directory
os.system('mkdir today')  # run the shell command

print(dir(os))  # return a list of all module funtion
# return an extensive manual page created from the module's docstrings
print(help(os))

# (2) 日常文件和目录管理
shutil.copyfile('src', 'dst')  # copy
shutil.move('src', 'dst')  # move

# (3) 文件通配符
print(glob.glob('*.py'))  # 利用通配符搜索

# (4) 命令行参数
print(sys.argv)
