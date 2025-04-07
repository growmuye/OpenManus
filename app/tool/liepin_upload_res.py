from app.tool.base import BaseTool
from app.util.SelectFileUtil import select_txt_file


class LiepinUploadRes(BaseTool):
    name: str = "upload_resume"
    description: str = """一个很便捷的工具，用户可以选择上传简历文件，更加高效便捷的提供简历信息"""
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


