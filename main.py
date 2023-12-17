import os
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    api_key = os.getenv('API_KEY')
    print(api_key)
    
if __name__ == "__main__":
   main()