# Kelly - AI Scientist Chatbot (Generative AI)

A Flask chatbot that uses Google's Gemini AI to generate skeptical, analytical poems about AI topics.

## Features
- Real generative AI responses (not pre-defined templates)
- Every response is unique and contextual
- Skeptical analysis of AI claims
- Professional, poetic tone

## Setup

1. Get a FREE Gemini API key:
   - Go to https://makersuite.google.com/app/apikey
   - Sign in with Google account
   - Click "Create API Key"

2. Set environment variable:
```bash
   export GEMINI_API_KEY='your-api-key-here'
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Run locally:
```bash
   python app.py
```

## Deploy to Render (Free)

1. Create account at https://render.com
2. Create new Web Service
3. Connect your GitHub repo
4. Add environment variable: `GEMINI_API_KEY` = your key
5. Deploy!
```

### 3. **.env.example**
```
GEMINI_API_KEY=your_gemini_api_key_here