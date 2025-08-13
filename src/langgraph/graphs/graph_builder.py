from langgraph.graphs import StateGraph
from src.langgraph.state.state import State
from langgraph.graphs import START , END
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder :
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        # Build the basic chatbot graph using the model and state
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot" , self.basic_chatbot_node.process())
        self.graph_builder.add_edge(START, "chatbot")   
        self.graph_builder.add_edge("chatbot", END)