# ✍️ AI Restaurant Blog Generator

An AI-powered blog generation application built using **Python**, **Gradio**, and the **Groq API**. The application generates engaging restaurant and food blogs based on user inputs such as restaurant name, food topic, audience, writing tone, word count, and language. The generated blog can also be downloaded as a text file.

---

## Features

- 🍽️ Generate restaurant and food blogs instantly
- 🤖 Powered by Groq's Llama 3.3 70B Versatile model
- 🌍 Supports multiple languages
- 🎭 Choose different writing tones
- 📏 Adjustable blog length (200–1000 words)
- 💾 Download the generated blog as a TXT file
- 🌐 Simple Gradio web interface

---

## Technologies Used

- Python
- Gradio
- Groq API
- Llama 3.3 70B Versatile

---

## Project Structure

```
AI-Restaurant-Blog-Generator/
│
├── app.py
├── requirements.txt
├── README.md
└── generated_blogs/        (Optional)
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AI-Restaurant-Blog-Generator.git

cd AI-Restaurant-Blog-Generator
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

---

## Configure the Groq API Key

Replace:

```python
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

with your own Groq API key.

Example:

```python
client = Groq(api_key="YOUR_API_KEY")
```

---

## Run the Application

```bash
python app.py
```

Gradio will launch a local server, typically at:

```
http://127.0.0.1:7860
```

Open the URL in your browser.

---

## How to Use

1. Enter the restaurant name.
2. Specify the food or topic.
3. Select the target audience.
4. Choose a writing tone.
5. Adjust the desired word count.
6. Select the output language.
7. Click **Submit**.
8. Read the generated blog and download it as a `.txt` file.

---

## Input Parameters

- **Restaurant Name** – Name of the restaurant.
- **Food/Topic** – Dish or topic to focus on.
- **Audience** – Intended readers (e.g., food lovers, tourists, families).
- **Tone** – Professional, Casual, Funny, Technical, or Inspirational.
- **Word Count** – 200 to 1000 words.
- **Language** – English, Telugu, Hindi, Tamil, Kannada, Spanish, or French.

---

## Example Workflow

```
User Inputs
      │
      ▼
Groq API
(Llama 3.3 70B)
      │
      ▼
AI Generates Blog
      │
      ▼
Display in Gradio
      │
      ▼
Download as TXT File
```

---

## Example Output

A generated blog includes:

- Restaurant introduction
- Food description
- Rating out of 5
- Conclusion

---

## Future Improvements

- Add restaurant images
- Export blogs as PDF or DOCX
- SEO keyword optimization
- AI-generated blog titles
- Social media caption generation
- Blog editing and rewriting
- Additional language support
- Multiple AI model selection

---

## Author

**Grishma Thottempudi**

B.Tech – Data Science

---

## License

This project is developed for educational and learning purposes.
