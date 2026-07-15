from huggingface_hub import InferenceClient
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

@st.cache_data(show_spinner=False)
def generate_image(prompt, negative_prompt="", width=1024, height=1024, seed=42):
    image = client.text_to_image(
        prompt=prompt,
        model="stabilityai/stable-diffusion-xl-base-1.0",
        negative_prompt=negative_prompt,
        height=height,
        width=width,
        seed=seed
    )
    return image