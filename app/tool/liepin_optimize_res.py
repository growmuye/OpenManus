import os


from app.tool.base import BaseTool
from langchain_core.messages import HumanMessage, SystemMessage

from app.util.LlmUtil import chat, chatLlm


class LiepinOptimizeRes(BaseTool):
    name: str = "optimize_resume"
    description: str = """优化用户简历，从而提升简历质量"""
    parameters: dict = {
        "type": "object",
        "properties": {
            "target": {
                "type": "string",
                "description": "本次对话的目标",
            },
            "resumeInfo": {
                "type": "string",
                "description": "简历信息",
            },
        },
        "required": ["target","resumeInfo"],
    }


    async def execute(self, target:str,resumeInfo: str) -> str:
        chat_history1 = [SystemMessage(
            f"你是一个简历优化助手，目的是帮助用户优化简历。当用户输入：结束优化时，整理出一份优化后简历。下方是用户的当前简历\n{resumeInfo}")]
        print(f"\033[94m【子流程-优化简历】平台: {target}（输入'exit'结束）\033[0m")
        chat("\033[94m【子流程-优化简历】平台", "\033[0m", chatLlm, chat_history1)
        chat_history1.append(HumanMessage("输出优化后的简历"))
        response = chatLlm.invoke(chat_history1)
        res = response.content
        return res