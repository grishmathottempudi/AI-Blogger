# ✍️ AI Blog Generator (Gemini)

An AI-powered Blog Generator built using **Python**, **Gradio**, and the **Google Gemini API**. This application generates well-structured blogs on any topic based on the user's preferences, including audience, writing tone, word count, and blog style.

---

## Features

- ✍️ Generate blogs on any topic
- 🤖 Powered by Google Gemini 2.5 Flash
- 👥 Customize the target audience
- 🎭 Multiple writing tones
- 📏 Adjustable blog length (200–1000 words)
- 📰 Different blog styles (Informative, Storytelling, SEO-Friendly)
- 🌐 Interactive Gradio web interface

---

## Technologies Used

- Python
- Gradio
- Google Gemini API (`google-genai`)

---

## Project Structure

```
AI-Blog-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Blog-Generator.git
cd AI-Blog-Generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API Key

Replace:

```python
client = genai.Client(api_key="YOUR_API_KEY")
```

with your own Gemini API key.

---

## Run the Application

```bash
python app.py
```

After running, Gradio will provide a local URL similar to:

```
http://127.0.0.1:7860
```

Open it in your web browser.

---

## How to Use

1. Enter the blog topic.
2. Specify the target audience.
3. Select a writing tone.
4. Choose the desired word count.
5. Select a blog style.
6. Click **Submit**.
7. Read the generated blog.

---

## Inputs

- **Topic**
- **Audience**
- **Tone**
  - Professional
  - Casual
  - Funny
  - Sarcastic
  - Sad
  - Technical
- **Word Count**
  - 200–1000 words
- **Blog Style**
  - Informative
  - Storytelling
  - SEO-Friendly

---

## Blog Structure

The generated blog includes:

- Introduction
- Fun Facts
- Tips
- Advantages
- Conclusion

---

## Example Workflow

```
User Inputs
      │
      ▼
Google Gemini API
      │
      ▼
AI Generates Blog
      │
      ▼
Displayed in Gradio Interface
```

---

## Future Enhancements

- Download blog as PDF or DOCX
- Multi-language support
- AI-generated blog titles
- SEO keyword optimization
- Grammar checking
- Blog rewriting
- Image generation for blogs
- Social media caption generation

---

## Author

**Grishma Thottempudi**

B.Tech – Data Science

---

## License

This project is intended for educational and learning purposes.
