# 💬 Gemini Chat API (FastAPI + Google Generative AI)

This project is a lightweight API server built with **FastAPI** that integrates with **Google's Generative AI (Gemini)** to simulate chatbot responses. It's designed with an easily pluggable architecture so you can connect it to any frontend (React, Vue, etc.).

---

## ✨ Features

- 🔌 Google Gemini AI (via `google.generativeai`)
- 🚀 FastAPI for blazing-fast backend API
- 🧠 Role-based prompt style (custom personality)
- 🔐 `.env` support for sensitive config
- 🌐 CORS-enabled (default React dev port)
- 🔄 Easy integration with frontend

---

## 📁 Project Structure

```
gemini-chat-api/
│
├── chat_module.py          # Contains chat logic (AI prompt + Gemini call)
├── main.py                 # FastAPI app and endpoints
├── .env                    # Environment variables (DO NOT COMMIT)
├── requirements.txt        # Dependencies
└── README.md               # You're here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chat-api.git
cd gemini-chat-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the root directory with this content:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔑 You can get an API key from: https://makersuite.google.com/app

---

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

This starts the API at:

```
http://localhost:8000
```

---

## 🧪 API Usage

---

### ➤ `POST /chat`

Send a prompt and receive a Gemini-powered response.

#### Request Example:

```json
{
  "user": "javaScript kya hota hai",
  "model_type": "AI"
}
```

#### Response Example:

```json
"2+2 is 4"
```

✅ The response includes a quirky, humanized prefix (defined in `chat_module.py`).

---

## 🔧 Customizing Personality

You can edit the `role_prompt` in `chat_module.py` to change the assistant’s tone, humor, or behavior.

Example content:

```python
role_prompt = '''
Example
User: What is 2+2
"ye toh chai ke bina bhi ho jayega 2+2 is 4"
'''
```

The user input is appended to this `role_prompt` and sent to the Gemini model.

---

## 🔐 Security Notes

- **Never commit your `.env` file or API key to public repos.**
- Make sure to handle API rate limits and error cases in production setups.

---

## 🌐 CORS Setup

The app is CORS-enabled for local frontend development (like React at port 5173):

```python
origins = [
    "http://localhost:5173"
]
```

Modify this list in `main.py` based on your frontend URLs.

---

## 📦 requirements.txt

If you need to generate it, use:

```bash
pip freeze > requirements.txt
```

Example contents:

```
fastapi
uvicorn
python-dotenv
google-generativeai
pydantic
```

---

## 👨‍💻 Example Integration (React)

Here's a basic fetch example from React:

````javascript
      const response = await axios.post(
        "https://localhost:8000/chat",
        {
          user: currentInput,
          model_type: personas,
        },
      )
      ;```

---


````
