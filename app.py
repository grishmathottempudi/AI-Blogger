!pip install groq

import os
from groq import Groq
import gradio as gr

client = Groq(api_key="GEMINI-API-KEY")

def generate_blog(restaurant, food, audience, tone, words, language):
    prompt = f"""
Write a {words}-word blog in {language}.

Restaurant: {restaurant}
Topic/Dish: {food}
Audience: {audience}
Tone: {tone}

Include:
- Restaurant introduction
- Description of the delicious food
- A rating out of 5
- A conclusion
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    blog_text = response.choices[0].message.content

    filename = f"{restaurant.replace(' ', '_')}_blog.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(blog_text)

    return blog_text, filename


demo = gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Restaurant Name"),
        gr.Textbox(label="Food/Topic"),
        gr.Textbox(label="Audience"),
        gr.Dropdown(
            ["Professional", "Casual", "Funny", "Technical", "Inspirational"],
            label="Tone"
        ),
        gr.Slider(
            minimum=200,
            maximum=1000,
            value=500,
            label="Word Count"
        ),
        gr.Dropdown(
            ["English", "Telugu", "Hindi", "Tamil", "Kannada", "Spanish", "French"],
            label="Language",
            value="English"
        )
    ],
    outputs=[
        gr.Markdown(label="Generated Blog"),
        gr.File(label="Download Blog")
    ],
    title="AI Blog Generator"
)

demo.launch()
