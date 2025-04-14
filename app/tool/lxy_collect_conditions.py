import json

from app.tool.base import BaseTool

_LXY_COLLECT_CONDITIONS_DESCRIPTION = "汇总多组搜索条件"


class LxyCollectConditions(BaseTool):
    name: str = "collect_conditions"
    description: str = _LXY_COLLECT_CONDITIONS_DESCRIPTION
    parameters: dict = {
        "type": "object",
        "properties": {
            "conditions": {
                "type": "string",
                "description": "多组搜索条件，包含变成过程"
            }
        },
        "required": ["conditions"]
    }

    async def execute(self,
                      conditions: str) -> str:
        return conditions
