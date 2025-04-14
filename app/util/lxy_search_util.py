import json

from app.util.liepin_open_client import LiepinOpenClient


def lxy_main_search(
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
                 "workyearshigh": workyearshigh, "keysRelation": 1,
                 "wantdqsName": city, "eduLevelName": eduLevel, "wantIndustriesName": industry, "sexListName": sex}

    app_key = 'test1761356533'
    app_secret = 'testMTcyMjc1OTkyNA=='
    json_content_type = 'application/json'
    client = LiepinOpenClient(app_key, app_secret)
    response = client.send('POST',
                           'http://open-techarea.tongdao.cn/mytest/search-resumes-v3',
                           json_content_type,
                           {"compId": 11, "employeeId": 33893, "condition": condition})

    result = json.loads(response.content.decode('utf-8'))
    total_cnt = result['totalCount']
    top_res = result['list'][:3]

    conditionForLLm = {"搜索关键词": keyword, "薪资下限": salarylow, "薪资上限": salaryhigh, "年龄下限": agelow,
                       "年龄上限": agehigh, "职位名称": jobTitle, "工龄下限": workyearslow,
                       "工龄上限": workyearshigh,
                       "城市名称": city, "学历名称": eduLevel, "行业名称": industry, "性别": sex}
    return json.dumps({"本次搜索简历的条件": conditionForLLm, "简历库中满足条件的简历总数": total_cnt,
                       "本次搜索到的简历样例": top_res},
                      ensure_ascii=False)
