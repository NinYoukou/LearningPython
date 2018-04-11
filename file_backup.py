# 用户输入需要备份的文件，判断文件是否存在之后，对文件进行备份操作
#
# 导入os模块
import os

# 获取当前文件路径
file_path = os.getcwd()

# 根据文件路径获取当前路径下文件列表
filename_list = os.listdir(file_path)

# 提示用户输入需要备份的文件（文件需带拓展名如：old_filename.mp3）
print("请输入需要备份的文件文件需带拓展名如：old_filename.mp3）")
old_filename = input("> ")

# 判断用户输入的文件是否存在
if old_filename not in filename_list:
    print("您输入的文件不存在！")
else:
    # 对输入的文件名进行切割
    dot_position = old_filename.rfind(".") # "."位置定位
    new_filename = old_filename[:dot_position] + "_backup" + old_filename[dot_position:]

    # 对文件进行读写操作
    old_file = open(old_filename, "rb")
    data = old_file.read()
    new_file = open(new_filename, "wb")
    new_file.write(data)

    # 操作结束关闭文件
    new_file.close()
    old_file.close()
    print("文件备份成功！")
