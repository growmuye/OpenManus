from app.tool.base import BaseTool


_TERMINATE_DESCRIPTION = """当请求得到满足或助手无法继续执行任务时，终止交互。当你完成所有任务后，调用此工具来结束工作。"""


class Terminate(BaseTool):
    name: str = "terminate"
    description: str = _TERMINATE_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "status": {
                "type": "string",
                "description": "交互的完成状态。",
                "enum": ["success", "failure"],
            }
        },
        "required": ["status"],
    }

    async def execute(self, status: str) -> str:
        """Finish the current execution"""
        return f"交互完成: {status}"
