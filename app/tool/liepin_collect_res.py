from app.tool.base import BaseTool


class LiepinCollectRes(BaseTool):
    name: str = "collect_res"
    description: str = """收集简历信息"""
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
        print(f"\033[94m【AskHuman】平台: {target}（输入'exit'结束）\033[0m")
        user_inputs = ""
        while True:
            user_input = input("\033[94m【AskHuman】用户: \033[0m")
            if user_input.lower() == 'exit':
                print("\033[94m【AskHuman】平台: 本次收集结束\033[0m")
                break
            else:
                user_inputs += user_input + "\n"
        return user_inputs.strip()
