
import tkinter as tk
from tkinter import filedialog


def select_txt_file():
    # 创建一个 Tkinter 窗口
    root = tk.Tk()
    # 隐藏主窗口
    root.withdraw()

    # 打开文件选择对话框，限制只能选择 .txt 文件
    file_path = filedialog.askopenfilename(
        title="选择一个 .txt 简历文件",
        filetypes=[("Text files", "*.txt")]
    )

    # 如果用户选择了文件，返回文件路径
    if file_path:
        return file_path
    else:
        return None