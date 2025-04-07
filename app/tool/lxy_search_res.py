from app.tool.base import BaseTool
from app.util.SelectFileUtil import select_txt_file


class LxySearchRes(BaseTool):
    name: str = "search_resume"
    description: str = """搜索简历"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "keyword": {
                "type": "string",
                "description": "搜索关键词"
            },
        },
        "required": ["keyword"],
    }

    async def execute(self,keyword:str) -> str:
        print(f"正常调用搜简历{keyword}")
        return "搜到0份简历"
