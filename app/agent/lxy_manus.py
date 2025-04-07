from pydantic import Field

from app.agent import ToolCallAgent
from app.config import config
from app.prompt.manus import SYSTEM_PROMPT, NEXT_STEP_PROMPT
from app.tool import Terminate, ToolCollection, StrReplaceEditor


class LiepinManus(ToolCallAgent):
    """
    A versatile general-purpose agent that uses planning to solve various tasks.

    This agent extends BrowserAgent with a comprehensive set of tools and capabilities,
    including Python execution, web browsing, file operations, and information retrieval
    to handle a wide range of user requests.
    """

    name: str = "LxyManus"
    description: str = (
        "一个多功能代理，可以使用多种工具解决各种任务。"
    )

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 600000
    max_steps: int = 50

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            LiepinUploadRes(),  StrReplaceEditor(),Terminate()
        )
    )
