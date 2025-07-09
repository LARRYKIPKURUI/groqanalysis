import os
from dotenv import load_dotenv
from groq import Groq
from helpers.sample_data import sample_workflow_data, sample_user_details
from helpers.prompt_utils import create_prompt_from_workflow_data

# Load Groq API Key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("🔧 Generating analysis prompt...")
prompt = create_prompt_from_workflow_data(sample_workflow_data, sample_user_details)

print("🚀 Sending prompt to Groq...")
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a retail field performance analyst. Analyze the data provided below. "
                "Always use the field representative's actual name (never say 'User 101'). "
                "Give insights on performance, compliance, training needs, and stock-related issues."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3,
    max_tokens=4000
)

print("\n✅ AI-Generated Report:\n")
print(response.choices[0].message.content)
