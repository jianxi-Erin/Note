import os

# 创建目录
os.mkdir("这是os创建的目录")
# 删除目录
os.rmdir("这是os创建的目录")
# 获取当前目录
path = os.getcwd();
print(path)
# 判断目录是否存在
ex = os.path.exists("1.File.py")
print(ex)
# 查看目录内容
print(os.listdir("C:/"))
# 切换目录
os.chdir("D:/Python/HelloPython/212/5.File")
# 重命名
# os.rename("newFile.txt", "newFile.txt")
# 删除文件
# os.remove("newFile.txt")
