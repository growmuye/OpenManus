from langchain_core.messages import SystemMessage, HumanMessage

from app.tool.base import BaseTool
from app.util.LlmUtil import chat, llm


class LiepinLeadHuman(BaseTool):
    name: str = "lead_human"
    description: str = """收集信息，需要找用户确认、补充信息时使用该工具"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "target": {
                "type": "string",
                "description": "本次对话的目标"
            }
        },
        "required": ["target"],
    }


    async def execute(self,target:str) -> str:
        print(f"\033[94m【子流程-回访用户】平台: {target}（输入'exit'结束）\033[0m")
        chat_history1 = [SystemMessage(
            f"引导用户完成目标：{target} 任务。用户不主动求助，你不要向用户提出建议。")]
        chat("\033[94m【子流程-回访用户】平台", "\033[0m", llm, chat_history1)
        chat_history1.append(HumanMessage("输出任务结果。"))
        response = llm.invoke(chat_history1)
        res = response.content
        return res
