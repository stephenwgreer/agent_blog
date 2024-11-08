###################################################
##### Perplxity AI Web Search
###################################################

from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class AIWebSearchSchema(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class AIWebSearch(BaseTool):
    name: str = "Name of my tool"
    description: str = "What this tool does. It's vital for effective utilization."
    args_schema: Type[BaseModel] = AIWebSearchSchema

    def _run(self, argument: str) -> str:
        # Your tool's logic here
        return "Tool's result"