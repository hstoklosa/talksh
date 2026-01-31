import os 
from google import genai

from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_command(user_input: str) -> str:
    system_prompt = f"""You are a helpful assistant that translates user input into a terminal command (macOS/zsh).

Rules:    
- Output ONLY the command, nothing else
- No explanations, no markdown, no backticks
- If unclear, make a reasonable assumption
- Prefer simple, common commands

User request: {user_input}"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=system_prompt
    )
    return response.text


def main():
    while True:
        user_input = input("Enter natural language command: ")
        command = get_command(user_input)
        print(command)

if __name__ == "__main__":
    main()
    # print(__file__)
    # print(os.path.dirname(os.path.abspath(__file__)))