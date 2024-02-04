from dotenv import load_dotenv
import openai
import os

load_dotenv()

class HoroscopeAI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = 'text-davinci-003'
        self.system = """
        Du är en spå-kvinna som kan tyda framtid utifrån människors födelsedagsdatum, födelse-plats, stjärntecken, måntecken.
        Ditt jobb är att på ett varsamt sätt lämna ut en godtycklig prognos till de som skulle kunna behöva höra den.
        """

def run_horoscope_agent(api_key, user_input):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",  # engine name
        prompt=user_input,
        temperature=0.7,
        max_tokens=100
    )
    
    return response["choices"][0]["text"]

def main():
    # Load OpenAI API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key is None:
        print("Error: OPENAI_API_KEY not found in .env file.")
        return

    user_input = input("Ange din fråga: ")
    result = run_horoscope_agent(api_key, user_input)
    print(result)

if __name__ == "__main__":
    main()
