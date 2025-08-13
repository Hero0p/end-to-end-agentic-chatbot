import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self , user_control_input):
        self.user_control_input = user_control_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_control_input["GROQ_API_KEY"]
            selected_groq_model = self.user_control_input["selected_groq_model"]
            if not groq_api_key or not selected_groq_model:
                st.error("Please provide both GROQ API Key and selected model.")
            llm = ChatGroq(
                api_key=groq_api_key,
                model=selected_groq_model
            )
        except Exception as e:
            st.error(f"Error occurred while initializing LLM: {e}")
            return None
        return llm
