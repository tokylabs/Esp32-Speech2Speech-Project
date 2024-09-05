import requests  # For making HTTP requests
from config import credentials  # For accessing stored credentials
import utime  # For handling time-related tasks
import time

# Retrieve the API key for the language model service
api_key = credentials.get("GROQ_API_KEY")

# Function to interact with the language model and get a response
def invoke_llm(user_message, api_key):
    # Template for the AI's response behavior
    prompt_template = """You are a helpful AI. Follow these rules,
                            1. If query is related to following tools, respond with the exact tool name and one exact parameter only:
                            [move(left, right, forward, backword): "move car left, right, forward, or backword",
                            light(on, off): "turn the light on or off",
                            stop(None): "stop the car"]
                            2. Otherwise, respond with the exact answer to the user's query for 10 years old child under 50 words without using any newline escape character.
                            User: {user_message}"""
    # Format the prompt with the user's message
    formatted_prompt = prompt_template.format(user_message=user_message)
    
    # Define the API endpoint and headers for the request
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    # Define the request payload with the formatted prompt and model specification
    payload = {
        "messages": [{"role": "user", "content": f"{formatted_prompt}"}],
        "model": "llama3-8b-8192"
    }
    
    try:
        # Measure the time taken for the API request
        start_time = utime.ticks_ms()
        response = requests.post(url, headers=headers, json=payload)
        elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

        # Check if the request was successful and process the response
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content'].lower()
            return content
        else:
            raise Exception(f"API error ({response.status_code}): {response.reason}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Main function to test the LLM interaction
if __name__ == "__main__":
    prompt = "Tell me about machine Learning"
    
    # Invoke the language model and print the response
    response = invoke_llm(prompt, api_key)
    print(response)
