import streamlit as st
import os
from src.langgraph.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=self.config.get_page_title(),
            layout="wide"
        )
        st.header(self.config.get_page_title())

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls['selected LLM'] = st.selectbox(
                "Select LLM",
                options=llm_options,
            )
            if self.user_controls['selected LLM'] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls['selected Groq Model'] = st.selectbox(
                    "Select Groq Model",
                    options=groq_model_options,
                )
                self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.text_input("API KEY", type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys")

            self.user_controls['selected_usecase'] = st.selectbox("Select UseCase" , options=usecase_options)

        return self.user_controls