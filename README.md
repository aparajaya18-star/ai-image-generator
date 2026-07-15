# AI Image Generator

A simple AI Image Generator built with **Python** and **Streamlit**. Users can enter a text prompt, choose an artistic style, and generate AI-powered images using the Hugging Face Inference API.

## Live Demo

**Streamlit App:** https://ai-image-generator-18.streamlit.app/

---

## Features

* 🎨 Generate AI images from text prompts
* 🖌️ Multiple artistic styles
* 📐 Image size selection
* 🚫 Optional negative prompts
* 🖼️ Generate multiple images at once
* 📥 Download generated images
* 📝 Prompt history
* 🔒 API keys managed through environment variables

---

## Project Structure

```text
AI-Image-Generator/
│── app.py                 # Streamlit frontend
│── image_gen.py           # Image generation logic
│── utils.py               # Style modifiers and image sizes
│── requirements.txt
│── .env                   # Local API key (not committed)
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd AI-Image-Generator
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## API Key Setup

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_api_token
TEST_MODE=False
```

You can obtain a Hugging Face access token from your Hugging Face account settings.

---

## Running the Application

Start the Streamlit app with:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Technologies Used

* Python
* Streamlit
* Hugging Face Inference API
* Pillow
* python-dotenv

---

## Future Improvements

* Image gallery for previous generations
* Additional image generation models
* More artistic styles
* Prompt presets and random prompt generator
* Image editing and variations
* Better prompt history management

---

## License

This project was created for educational purposes as part of a Gen and Agentic AI Bootcamp.
