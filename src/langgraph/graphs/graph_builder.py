from langgraph.graph import StateGraph
from src.langgraph.state.state import State
from langgraph.graph import START , END
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.tools.search_tool import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition , ToolNode
from src.langgraph.nodes.chatbot_with_web_node import ChatbotWithWebNode    

class GraphBuilder :
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        # Build the basic chatbot graph using the model and state
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot" , self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")   
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_web_build_graph(self):
        # Build the chatbot with web graph using the model and state
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        obj_chatbot_with_web_node = ChatbotWithWebNode(llm)
        chatbot_node = obj_chatbot_with_web_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)



    

    def set_up_graph(self , usecase):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot With Web":
            self.chatbot_with_web_build_graph()

        return self.graph_builder.compile()