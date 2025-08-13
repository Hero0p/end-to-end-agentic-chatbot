from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated

class State(TypedDict):
    """
    Represents the state of the conversation.
    
    """
    messages: Annotated[list[str], add_messages]
    user: str
    context: dict[str, str]