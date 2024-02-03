from overthink import AIAgent

class HoroscopeAI(AIAgent):
    model = 'gpt-4-turbo'
    system = """
    Du är en spå-kvinna som kan tyda framtid utifrån människors födelsedagsdatum, födelse-plats, stjärntecken, måntecken.
    Ditt jobb är att på ett varsamt sätt lämna ut en godtycklig prognos till de som skulle kunna behöva höra den.
    """

def run_horoscope_agent(user_input):
    agent = HoroscopeAI()
    result = agent.think([
        {"role": "user", "content": user_input}
    ])
    return result

def main():
    user_input = input("Ange din fråga: ")
    result = run_horoscope_agent(user_input)
    print(result)

if __name__ == "__main__":
    main()
