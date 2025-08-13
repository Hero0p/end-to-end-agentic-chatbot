import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMS.groqllm import GroqLLM

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

        except Exception as e:
            st.error(f"Error: {e}")

        
       
