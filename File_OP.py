import os
import tkinter as tk
from tkinter import filedialog
import shutil



def open_folder_dialog():
    # 创建一个Tkinter窗口
#    root = tk.Tk()
#    root.withdraw()  # 隐藏主窗口

    # 打开文件夹选择对话框
    folder_path = filedialog.askdirectory(title="选择文件夹")

    # 打印选择的文件夹路径
    if folder_path:
        print("选择的文件夹路径:", folder_path)
        return folder_path
    else:
        print("没有选择任何文件夹")
        return 'Null'

#    root.destroy()  # 关闭Tkinter窗口


def list_files(directory):
    # 遍历指定目录下的所有文件和文件夹
    Temp_num = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            # 拼接完整的文件路径
            print(root)
            file_path = os.path.join(root, name)
            Temp_num = Temp_num + 1
            print(file_path)
    return Temp_num




def move_jpg_files(src_folder, dest_folder, jpgfile_name):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    # 构造完整的文件路径
    file_path = os.path.join(src_folder, jpgfile_name)
    # 构造目标文件路径
    dest_path = os.path.join(dest_folder, jpgfile_name)
    shutil.move(file_path, dest_path)

    print(f"文件 {jpgfile_name} 已移动到 {dest_path}")
