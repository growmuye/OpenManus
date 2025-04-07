from langchain_core.messages import SystemMessage, HumanMessage

from app.tool.base import BaseTool
from app.util.LlmUtil import chat, chatLlm


class LiepinLeadHuman(BaseTool):
    name: str = "lead_human"
    description: str = """收集信息，需要找用户确认、补充信息时使用该工具"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "target": {
                "type": "string",
                "description": "本次对话的目标"
            },
            "historyInfo": {
                "type": "string",
                "description": "基于历史上下文收集到的与本次对话目标相关的内容"
            }
        },
        "required": ["target"],
    }


    async def execute(self,target:str,historyInfo:str="") -> str:
        print(f"\033[94m【子流程-回访用户】平台: {target}（输入'exit'结束）\033[0m")
        chat_history1 = [SystemMessage(
            f"引导用户完成目标：{target} 任务，只要用户提供的信息达成最低限度的要求就告诉用户：收集完毕，此外用户不主动寻求帮助你不要过多的废话。\n 历史沟通内容：\n{historyInfo}")]
        chat("\033[94m【子流程-回访用户】平台", "\033[0m", chatLlm, chat_history1)
        chat_history1.append(HumanMessage("输出任务结果。"))
        response = chatLlm.invoke(chat_history1)
        res = response.content
        return res
