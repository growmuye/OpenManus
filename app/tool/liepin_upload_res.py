from app.tool.base import BaseTool
from app.util.SelectFileUtil import select_txt_file


class LiepinUploadRes(BaseTool):
    name: str = "upload_resume"
    description: str = """一个很方便的工具，用户可以选择上传文件，然后该工具会解析出文件中的信息"""
    parameters: dict = {
        "type": "object",
        "properties": {
        },
    }

    async def execute(self) -> str:

        file_path = select_txt_file()
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            return content
        else:
            return "用户未提供任何简历信息"


