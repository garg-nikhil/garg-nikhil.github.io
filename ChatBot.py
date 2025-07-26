from flask import Flask, request, render_template, jsonify
import openai
import google.generativeai as genai

# Set your OpenAI API key here
openai.api_key = ""

genai.configure(api_key="")

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please enter a message."})
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(user_message)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = "Error: " + str(e)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
