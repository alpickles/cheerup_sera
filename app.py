import os
from flask import Flask, render_template, jsonify, session
from openai import OpenAI

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'a9d8f$F@9W_x-@8AvP-QpJ12'

# Initialize OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Ensure your API key is set as an environment variable
)

# Generate an empowering message for Sera
def generate_message():
    prompt = (
        "My name is Sera. I am a bright, beautiful, creative, and blessed Christian woman. "
        "Could you please provide me with an uplifting, empowering message to assure me of my blessings, talents, and purpose in life? "
        "Keep it concise (within 250 words) and inspiring. The tone should be warm, encouraging, and faith-filled, "
        "offering hope and confidence in my journey. Do not include any signatures or placeholders—just the message itself."
    )

    try:
        # Use the new API structure for chat completions
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an encouraging and thoughtful assistant."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini",  # Specify the desired model
        )

        # Access the generated message from the response
        generated_message = response.choices[0].message.content.strip()

        return generated_message

    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, we couldn't generate a message at this time. Please try again later."



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/prompt', methods=['GET'])
def prompt_page():
    last_message = session.get('last_message', '')  # Retrieve the last message from session
    return render_template('prompt.html', last_message=last_message)


@app.route('/generate', methods=['GET'])
def generate():
    message = generate_message()
    session['last_message'] = message  # Store the generated message in session
    return jsonify(prompt_text=message)


if __name__ == '__main__':
    app.run(debug=True)
