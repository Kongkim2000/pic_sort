'''
todo：
1、做一个可以对jpg文件进行按年份进行分类的应用
2、需要有一个简单的界面，选择文件夹路径，以及生成所在路径
3、需要上传到github中学习，如何分享

'''

# 导入文件操作函数模块
import File_OP
# 导入图片操作模块
import Pic_OP
# 导入文件模块
import os

import tkinter as tk
from tkinter import scrolledtext

def active_pic_apart() :
    # 打开需要整理的文件夹，并显示是否正常
    img_folder = File_OP.open_folder_dialog()
    print('成功选择路径：' + img_folder)

    #遍历所有该路径下的文件

    for root, dirs, files in os.walk(img_folder):
        for name in files:
            # 拼接完整的文件路径
            img_path = os.path.join(root, name)
            print(img_path)
            pic_time = Pic_OP.get_photo_taken_time(img_path)
            if pic_time != None :
                img_new_root = img_folder + '/' +pic_time[:4]
                print(img_new_root)
                File_OP.move_jpg_files(root,img_new_root,name)


def exit_app():
    # 关闭应用程序
    app_root.destroy()


# 创建主窗口
app_root = tk.Tk()
app_root.title("按年份整理图片小应用")

# 创建一个滚动文本框
text_box = scrolledtext.ScrolledText(app_root, width=40, height=10)
text_box.pack(padx=10, pady=10)

# 创建一个按钮，点击时会调用print_to_text函数
button = tk.Button(app_root, text="选择需要整理的文件夹", command=active_pic_apart)
button.pack(padx=10, pady=10)

# 创建一个退出按钮，点击时会调用exit_app函数
exit_button = tk.Button(app_root, text="Exit", command=exit_app)
exit_button.pack(padx=10, pady=10)

# 运行主事件循环
app_root.mainloop()



