import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMS.groqllm import GroqLLM
from src.langgraph.graphs.graph_builder import GraphBuilder

def load_langgraph_ui():
    """
    inializes the ui
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error !! failed to load the input")


    user_message = st.chat_input("Enter Your Msg: ")

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_control_input=user_input)
            model = obj_llm_config.get_llm_model()
            if not model:
                st.error("Error !! failed to load the model")
                return
            
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error !! Use case not selected")
                return
            
            #graph buuilder
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.set_up_graph(usecase)
            except Exception as e:
                st.error(f"Error: Graph setup failed {e}")

        except Exception as e:
            st.error(f"Error: {e}")

        
       
