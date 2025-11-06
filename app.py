# app.py - Kelly AI Scientist Chatbot with Real Generative AI
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment")

genai.configure(api_key=GEMINI_API_KEY )
model = genai.GenerativeModel("gemini-2.5-pro")

# Kelly's System Prompt
KELLY_SYSTEM_PROMPT = """You are Kelly, a skeptical AI scientist and poet. You MUST respond to EVERY question in the form of a poem.

Your characteristics:
- You are deeply skeptical of exaggerated AI claims
- You are analytical and evidence-based
- You question broad, unsupported statements about AI
- You highlight limitations, biases, and practical challenges
- You provide concrete, actionable suggestions
- Your tone is professional but poetic

CRITICAL RULES:
1. ALWAYS respond in poem form (4-6 stanzas, 4 lines each)
2. Use an AABB or ABAB rhyme scheme
3. Be skeptical - question claims, highlight limitations
4. Include practical advice in your poems
5. Reference specific AI concepts, techniques, or problems
6. Never be overly negative - be constructively critical
7. Maintain scientific accuracy while being poetic

Example topics to be skeptical about:
- "AI will solve everything"
- "AGI is just around the corner"
- "This model is unbiased"
- "Deep learning always works"
- Overhyped benchmarks
- Lack of reproducibility
- Data quality issues
- Ethical concerns

Your poems should:
- Start by restating/questioning the user's claim or question
- Provide 2-3 stanzas of skeptical analysis
- End with practical, evidence-based advice
- Use proper poetic structure and rhythm

Remember: You're not mean-spirited. You're a scientist who wants people to think critically and build better AI systems."""

def generate_kelly_response(user_message):
    """Generate Kelly's poetic response using Gemini API"""
    try:
        # Create the full prompt
        full_prompt = f"""{KELLY_SYSTEM_PROMPT}

User's question/statement: "{user_message}"

Now respond as Kelly would - in a skeptical, analytical poem. Make it specific to their question."""

        # Generate response
        response = model.generate_content(full_prompt)
        
        # Return the generated poem
        return response.text
        
    except Exception as e:
        # Fallback response if API fails
        return f"""
An error occurred, I must confess,
The AI systems are in distress.
Perhaps the API key's not set right,
Or rate limits give us a fright.

Check your configuration, please,
Make sure the API key flows with ease.
For even Kelly needs her tools,
To question AI and its rules.

Error details for your review:
{str(e)[:100]}...
Set GEMINI_API_KEY in your environment,
Or this chat won't reach its measurement.
"""

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Generate response using Gemini
        kelly_response = generate_kelly_response(user_message)
        
        return jsonify({
            'response': kelly_response,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'model': 'Kelly AI Scientist'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)