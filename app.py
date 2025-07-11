from flask import Flask, render_template, request
import openai
import os
from config import OPENAI_API_KEY

app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = OPENAI_API_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    blog_content = ""
    if request.method == "POST":
        topic = request.form["topic"]
        if topic:
            prompt = f"Write a detailed, SEO-optimized blog post about: {topic}. Make it engaging and easy to read."
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=800,
                    temperature=0.7
                )
                blog_content = response.choices[0].message["content"]
            except Exception as e:
                blog_content = f"Error: {str(e)}"
    return render_template("index.html", content=blog_content)

if __name__ == "__main__":
    app.run(debug=True)
  
