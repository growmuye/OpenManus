from app.tool.base import BaseTool

_LXY_COLLECT_CONDITIONS_DESCRIPTION = "汇总多轮搜索所的条件"


class LxyCollectConditions(BaseTool):
    name: str = "collect_conditions"
    description: str = _LXY_COLLECT_CONDITIONS_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "conditions": {
                "type": "string",
                "description": "多轮搜索条件，以搜索条件改写路线的方式呈现"
            }
        },
        "required": ["conditions"]
    }

    async def execute(self,
                      conditions: str) -> str:
        return f"交互完成: success"
