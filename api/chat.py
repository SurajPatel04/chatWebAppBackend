import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the GenAI client
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the model instance
model = genai.GenerativeModel(model_name='gemini-2.0-flash-001')

# Define a role-based prefix

def chat(user):
    role_prompt = """
    Example
User: What is the 2+2
Your Response: "ye toh chai ke bina bhi ho jayega 2+2 is 4"
}
} 
"""

# Get user input


# Combine role prompt with user query
    full_prompt = f"{role_prompt}User Query: {user}"

# Generate content using the role-based prompt
    response = model.generate_content(full_prompt)

# Print the response
    return response.text

chat("2+4")
