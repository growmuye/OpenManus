from app.tool.base import BaseTool


class LiepinAskHuman(BaseTool):
    name: str = "ask_human"
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
        user_inputs = ""
        while True:
            user_input = input("\033[94m【子流程-回访用户】用户: \033[0m")
            if user_input.lower() == 'exit':
                # print("\033[94m【子流程-回访用户】平台: 本次收集结束\033[0m")
                break
            else:
                user_inputs += user_input + "\n"
        return user_inputs.strip()
