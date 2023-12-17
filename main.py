import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup(api_key : str) -> genai: 
    genai.configure(api_key=api_key)
    return genai

def choose_model(gemini : genai, model_name : str):
    model = gemini.GenerativeModel(model_name)
    return model

def get_answer(model : genai, question : str, is_stream) -> str:
    if is_stream:
        response = model.generate_content(question, stream=True)
        return response.text
    
    response = model.generate_content(question)
    return response.text


def print_available_medels(gemini : genai):
    for m in gemini.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    api_key = os.getenv('API_KEY')
    gemini = setup(api_key=api_key)
    print_available_medels(gemini=gemini)
    model = choose_model(gemini=gemini, model_name='gemini-pro')
    answer = get_answer(model=model, question="What is the meaning of life?", is_stream=False)
    print(answer)

    
if __name__ == "__main__":
   main()