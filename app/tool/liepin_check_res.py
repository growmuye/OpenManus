from langchain_core.messages import SystemMessage, HumanMessage

from app.tool.base import BaseTool
from app.util.LlmUtil import chatLlm


class LiepinCheckRes(BaseTool):
    name: str = "check_resume"
    description: str = """检查简历信息是否需要补充、检查简历是否完整"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "resumeInfo": {
                "type": "string",
                "description": "简历信息",
            }
        },
        "required": ["resumeInfo"],
    }



    async def execute(self, resumeInfo: str) -> str:
        chat_history1 = [HumanMessage(f"""检查简历内容各维度是否严格符合以下要求：
* 姓名：必须存在有效值
* 工龄：建议存在有效值
* 工作经验：建议存在有效值
* 教育经历：必须存在有效值
* 期望薪资：必须存在有效值
* 期望地点：必须存在有效值
* 作品：建议存在有效值

示例一：
姓名：郭牧野
输出：存在必须项-姓名

示例二：
姓名：不知道
输出：丢失必须项-姓名

示例三：
工龄：10年
输出：存在必须项-工龄

示例四：
工作经验：10年猎聘网
输出：存在必须项-工作经验

示例五：
教育经历：清华大学
输出：存在必须项-教育经历

示例六：
教育经历：我没上过学
输出：丢失必须项-教育经历

示例七：
教育经历：不知道
输出：丢失必须项-教育经历

示例八：
期望薪资：10-15万
输出：存在必须项-期望薪资

示例九：
期望薪资：不知道
输出：丢失必须项-期望薪资

示例十：
期望薪资：我不想说
输出：丢失必须项-期望薪资

示例十一：
期望地点：我想找份北京的工作
输出：存在必须项-期望地点

示例十二：
期望地点：不知道
输出：丢失必须项-期望地点

示例十三：
用户：期望地点：我不想说
输出：丢失必须项-期望地点


以下为简历信息：
{resumeInfo}""")]
        response = chatLlm.invoke(chat_history1)
        res = response.content
        print(f"\033[94m【子流程-检查简历】平台: {res}\033[0m")
        return res
