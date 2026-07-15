import streamlit as st
import os
from dotenv import load_dotenv
from image_gen import generate_image
from utils import STYLE_MODIFIERS, IMAGE_SIZES
from PIL import Image
from io import BytesIO

load_dotenv()

TEST_MODE = os.getenv("TEST_MODE", "False") == "True"

# ---- Streamlit App ----

st.set_page_config(page_title="AI Image Generator", layout="wide", initial_sidebar_state="collapsed")

st.title("AI Image Generator")
st.caption("Generate beautiful AI images using natural language.")

with st.container(border=True):
    prompt = st.text_area(label="Image Prompt", placeholder="Enter prompt here...")

    col1, col2 = st.columns(2)
    
    with col1:
        style = st.radio("Style", options=list(STYLE_MODIFIERS.keys()))

    with col2:
        image_size = st.selectbox(label="Image Size", options=list(IMAGE_SIZES.keys()))  
        num_images = st.selectbox(label="Images to generate", options=[1,2,3,4])  
    
    negative_prompt = st.text_area(label="Negative Prompt", placeholder="Enter negative prompt here...")

    gen_button = st.button("Generate Image")

if "history" not in st.session_state:
    st.session_state.history = []

if "generated_images" not in st.session_state:
    st.session_state.generated_images = []

if gen_button:
    if not (prompt.strip() and style):
        st.warning("Please enter a prompt and pick a style!")
        st.stop()

    generated_images = []
    final_prompt = f"{prompt}, {STYLE_MODIFIERS[style]}"

    with st.spinner("Generating image..."):
        for i in range(num_images):
            if TEST_MODE:
                generated_images.append(Image.open("test_image.jpg"))
            else:
                try:
                    if num_images == 1:
                        generated_images.append(
                            generate_image(
                                final_prompt, 
                                negative_prompt, 
                                *IMAGE_SIZES[image_size]
                            )
                        )
                    else:
                        generated_images.append(
                            generate_image(
                                final_prompt, 
                                negative_prompt, 
                                *IMAGE_SIZES[image_size],
                                seed=i
                            )
                        )
                except Exception as e:
                    st.error(f"Generation failed:\n{e}")      

        if generated_images:
            st.session_state.history.append({
                "prompt": prompt,
                "style": style,
                "size": image_size,
                "count": num_images,
                "negative_prompt": negative_prompt
            })  
            st.session_state.generated_images = generated_images

if st.session_state.generated_images:
    with st.container(border=True):
        st.header("Generated Image")

        cols = st.columns(min(num_images, 2))
        for idx, image in enumerate(st.session_state.generated_images):
            with cols[idx % 2]:
                st.image(image, caption=f"Generated: {prompt}", use_container_width=True)
                
                buffer = BytesIO()
                image.save(buffer, format="PNG")
                buffer.seek(0)

                st.download_button(
                    "Download",
                    data=buffer.getvalue(),
                    file_name=f"generated_{idx+1}.png",
                    mime="image/png",
                    key=f"download_{idx}"
                )

with st.sidebar:
    st.header("Prompt History")
    st.divider()

    for item in reversed(st.session_state.history):
        with st.expander(label = f"{item['style']} • {item['count']} images", expanded=True):

            st.markdown(f"**Prompt:** {item['prompt']}")
            st.markdown(f"**Size:** {item['size']}")

            st.write("")
            if item["negative_prompt"]:
                st.markdown(f"**Negative:** {item['negative_prompt']}")

# ---- Streamlit App ----