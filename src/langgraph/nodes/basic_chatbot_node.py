from src.langgraph.state.state import State

class BasicChatbotNode:
    def __init__(self , model):
        self.llm = model

    def process(self,state : State) -> dict:
        # Process the input text using the LLM
        return {"messages" : self.llm.invoke(state["messages"])}