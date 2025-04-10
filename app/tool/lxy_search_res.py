import json

from app.tool.base import BaseTool
from app.util.liepin_open_client import LiepinOpenClient

_LXY_SEARCH_RES_TOOL_DESCRIPTION = "根据用户的招聘需求，分析简历库中满足需求的简历分布状况：本次搜索简历的条件、简历库中满足条件的简历总数、本次搜索到的简历样例。"

class AnalyzeResumeDatabaseForRecruitment(BaseTool):
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
            },
        },
        "required": ["keys"],
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
        condition = {"keys": keyword, "wantsalarylow": salarylow, "wantsalaryhigh": salaryhigh, "agelow": agelow,
                     "agehigh": agehigh, "titleKeys": jobTitle, "workyearslow": workyearslow,
                     "workyearshigh": workyearshigh,"keysRelation":1,
                     "wantdqsName": city, "eduLevelName": eduLevel, "wantIndustriesName": industry, "sexListName": sex}

        app_key = 'test1761356533'
        app_secret = 'testMTcyMjc1OTkyNA=='
        json_content_type = 'application/json'
        client = LiepinOpenClient(app_key, app_secret)
        response = client.send('POST',
                               'http://open-techarea-sandbox13801.sandbox.tongdao.cn/mytest/search-resumes-v3',
                               json_content_type,
                               {"compId": 11, "employeeId": 33893, "condition": condition})

        result = json.loads(response.content.decode('utf-8'))
        total_cnt = result['totalCount']
        top_res = result['list'][:3]

        conditionForLLm = {"搜索关键词": keyword, "薪资下限": salarylow, "薪资上限": salaryhigh, "年龄下限": agelow,
                           "年龄上限": agehigh, "职位名称": jobTitle, "工龄下限": workyearslow,
                           "工龄上限": workyearshigh,
                           "城市名称": city, "学历名称": eduLevel, "行业名称": industry, "性别": sex}
        return json.dumps({"本次搜索简历的条件": conditionForLLm, "简历库中满足条件的简历总数": total_cnt, "本次搜索到的简历样例": top_res},
                          ensure_ascii=False)
