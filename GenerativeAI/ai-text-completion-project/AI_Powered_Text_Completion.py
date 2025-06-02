################################################################################################
# Assignment: AI Powered-Text-Completion
# Name: Nicholas Hamilton
# This project is the Capstone in my GEN AI Externship with Cognizant.
# This app uses OpenAI's GPT model for text generation.
################################################################################################



from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def menu():
    options = {1, 2, 3}
    while True:
        try:
            user_choice = int(input("\nWhat would you like to do?\n"
            "1. Enter a prompt for the AI to complete\n"
            "2. Change model settings (temperature, max tokens)\n"
            "3. Exit\n"
            "Please enter 1, 2, or 3: "))
            if user_choice in options:
                return user_choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_prompt():
    prompt = input("\nEnter your prompt: ").strip()
    if not prompt:
        print("Prompt cannot be empty.")
        return None
    return prompt

def get_model_settings():
    while True:
        try:
            temp = float(input("Set temperature (0.0 to 1.0): "))
            if not (0.0 <= temp <= 1.0):
                raise ValueError
            max_tokens = int(input("Set max tokens (e.g., 50): "))
            if max_tokens <= 0:
                raise ValueError
            return temp, max_tokens
        except ValueError:
            print("Invalid values. Try again.")

def generate_completion(prompt, temperature, max_tokens):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        generated_text = response.choices[0].message.content.strip()
        print(f"\nAI Response:\n{generated_text}")
    except Exception as e:
        print(f"Error during API call: {e}")

def main():
    print("Welcome to the Text Completion App (using OpenAI GPT)!")
    temperature = 0.7
    max_tokens = 60

    while True:
        choice = menu()

        if choice == 1:
            prompt = get_prompt()
            if prompt:
                generate_completion(prompt, temperature, max_tokens)

        elif choice == 2:
            temperature, max_tokens = get_model_settings()
            print(f"Settings updated. Temperature: {temperature}, Max Tokens: {max_tokens}")

        elif choice == 3:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()