from app.tool.base import BaseTool
from app.util.lxy_search_util import lxy_main_search

_LXY_SEARCH_RES_TOOL_DESCRIPTION = "根据用户的招聘需求，分析简历库中满足需求的简历分布状况：本次搜索简历的条件、简历库中满足条件的简历总数、本次搜索到的简历样例。"

class LxyAnalyzeResumeDatabaseForRecruitment(BaseTool):
    name: str = "analyze_resume_database_for_recruitment"
    description: str = _LXY_SEARCH_RES_TOOL_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "keyword": {
                "type": "string",
                "description": "搜索关键词，多个以空格分隔"
            },
            "salarylow": {
                "type": "integer",
                "description": "薪资下限，如：25万提取为25"
            },
            "salaryhigh": {
                "type": "integer",
                "description": "薪资上限，如：35万提取为35"
            },
            "agelow": {
                "type": "integer",
                "description": "年龄下限"
            },
            "agehigh": {
                "type": "integer",
                "description": "年龄上限"
            },
            "jobTitle": {
                "type": "string",
                "description": "职位名称，多个以空格分隔"
            },
            "workyearslow": {
                "type": "integer",
                "description": "工龄下限"
            },
            "workyearshigh": {
                "type": "integer",
                "description": "工龄上限"
            },
            "city": {
                "type": "array",
                "items": {"type": "string"},
                "description": "城市名称，如北京、北京-朝阳区、河南省-郑州市，多级使用-分割"
            },
            "eduLevel": {
                "type": "array",
                "items": {"type": "string", "enum": [
                    "本科", "硕士", "博士", "初中及以下", "高中", "中专/中技", "大专", "MBA/EMBA"
                ]},
                "description": "学历名称"
            },
            "industry": {
                "type": "array",
                "items": {"type": "string"},
                "description": "行业名称"
            },
            "sex": {
                "type": "array",
                "items": {"type": "integer", "enum": [
                    "男", "女"
                ]},
                "description": "性别"
            }
        }
    }

    async def execute(self,
                      keyword: str = None,
                      salarylow: str = None,
                      salaryhigh: str = None,
                      agelow: str = None,
                      agehigh: str = None,
                      jobTitle: str = None,
                      workyearslow: str = None,
                      workyearshigh: str = None,
                      city: list = None,
                      eduLevel: list = None,
                      industry: list = None,
                      sex: list = None) -> str:
        return lxy_main_search(keyword, salarylow, salaryhigh, agelow, agehigh, jobTitle, workyearslow, workyearshigh,
                               city, eduLevel, industry, sex)
