from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import google.generativeai as genai
import os

faq_page = Blueprint('faq_page', __name__, template_folder='templates')

# Configure Gemini API
genai.configure(api_key="AIzaSyC6XTNnm_O-BCRuyAKgrhIr73_LgrNa4uQ")

# Set up chat session with initial history
chat_session = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
).start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "TTT should be knowledgeable about various types of scams such as phishing, identity theft, fake investment schemes, and fraudulent loan offers. The chatbot should provide clear, accurate, and reassuring responses, educating users on how to identify scams, avoid common pitfalls, and respond safely if they suspect they’ve encountered a scam. Additionally, TTT should be able to provide general tips on financial safety and staying secure online. Ensure TTT’s tone is friendly, trustworthy, and easy to understand.\" YOu should the user for their name and email so that he can contact them in the future if needed"
            ],
        },
        {
            "role": "model",
            "parts": [
                "Hi there! I'm TTT, your friendly guide to financial safety. I can help you understand and avoid scams related to financial institutions. What can I do for you today?"
            ],
        },
    ]
)

@faq_page.route('/faq')
@login_required
def faq():
    return render_template('faq.html', user=current_user)

@faq_page.route('/faq/ask', methods=['POST'])
def ask_faq():
    user_input = request.json.get('question')
    response = chat_session.send_message(user_input)
    return jsonify({"response": response.text})
