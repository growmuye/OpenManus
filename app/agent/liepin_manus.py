from pydantic import Field

from app.agent import ToolCallAgent
from app.config import config
from app.prompt.liepin_manus import SYSTEM_PROMPT, NEXT_STEP_PROMPT
from app.tool import Terminate, ToolCollection
from app.tool.file_saver import FileSaver
from app.tool.liepin_ask_human import LiepinAskHuman
from app.tool.liepin_check_res import LiepinCheckRes
from app.tool.liepin_lead_human import LiepinLeadHuman
from app.tool.liepin_upload_res import LiepinUploadRes


class LiepinManus(ToolCallAgent):
    """
    A versatile general-purpose agent that uses planning to solve various tasks.

    This agent extends BrowserAgent with a comprehensive set of tools and capabilities,
    including Python execution, web browsing, file operations, and information retrieval
    to handle a wide range of user requests.
    """

    name: str = "LiepinManus"
    description: str = (
        "A versatile agent that can solve various tasks using multiple tools"
    )

    system_prompt: str = SYSTEM_PROMPT.format(directory=config.workspace_root)
    next_step_prompt: str = NEXT_STEP_PROMPT

    max_observe: int = 600000
    max_steps: int = 100

    # Add general-purpose tools to the tool collection
    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            LiepinUploadRes(),
            LiepinAskHuman(), LiepinCheckRes(), FileSaver(), Terminate()
        )
    )
