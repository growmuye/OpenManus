import tkinter as tk
from tkinter import filedialog


def select_txt_file():
    # 创建一个 Tkinter 窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()

    # 打开文件选择对话框，限制只能选择 .txt 文件
    file_path = filedialog.askopenfilename(
        title="选择一个 .txt 文件",
        filetypes=[("Text files", "*.txt")]
    )

    # 如果用户选择了文件，返回文件路径
    if file_path:
        print(f"选择的文件路径是: {file_path}")
        return file_path
    else:
        print("用户取消了选择")
        return None


# 调用函数
selected_file = select_txt_file()