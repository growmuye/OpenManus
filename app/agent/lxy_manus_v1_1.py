from pydantic import Field

from app.agent import ToolCallAgent
from app.config import config
from app.prompt.lxy_manus import SYSTEM_PROMPT, NEXT_STEP_PROMPT
from app.tool import ToolCollection, Terminate
from app.tool.lxy_analyze_resume_database_for_recruitment import LxyAnalyzeResumeDatabaseForRecruitment


class LxyManus_v1_1(ToolCallAgent):

    name: str = "LxyManus v1.1"
    description: str = (
        "一个AI招聘助手，可以使用多种工具解决各种任务。"
    )

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 600000
    max_steps: int = 10

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            LxyAnalyzeResumeDatabaseForRecruitment(),Terminate()
        )
    )
