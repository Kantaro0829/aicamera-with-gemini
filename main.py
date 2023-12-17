import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup(api_key : str) -> genai: 
    genai.configure(api_key=api_key)
    return genai

def print_available_medels(genemi : genai):
    for m in genemi.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    api_key = os.getenv('API_KEY')
    genemi = setup(api_key=api_key)
    print_available_medels(genemi=genemi)
    
if __name__ == "__main__":
   main()