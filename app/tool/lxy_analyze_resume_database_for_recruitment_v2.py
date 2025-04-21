import json

from app.tool.base import BaseTool
from app.util.lxy_search_util import lxy_main_search

_LXY_SEARCH_RES_TOOL_DESCRIPTION = "根据用户的招聘需求，分析简历库中满足需求的简历分布状况：本次搜索简历的条件、简历库中满足条件的简历总数、本次搜索到的简历样例。"

class LxyAnalyzeResumeDatabaseForRecruitmentV2(BaseTool):
    name: str = "analyze_resume_database_for_recruitment"
    description: str = _LXY_SEARCH_RES_TOOL_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "recruitmentRequirements": {
                "type": "string",
                "description": "招聘需求，格式示例如下：职位名称：...\n薪资范围：...\n工作年限：...\n\n职责描述：\n...\n\n任职要求：\n..."
            }
        },
        "required": ["recruitmentRequirements"],
    }

    async def execute(self,
                      recruitmentRequirements: str = None) -> str:
        # 调用llm
        return json.dumps({"简历库中满足条件的简历总数": 0,
                           "本次搜索到的简历样例": []},
                          ensure_ascii=False)
