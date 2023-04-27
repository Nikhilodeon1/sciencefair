import random

R_EATING = "I don't like eating or drinking anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def internet(str):
    return str

def unknown():
    response = ["Could you please re-phrase that? ",
                "What?",
                "I don't get it.",
                "What did you just say?",
                "What does that mean?"][
        random.randrange(4)]
    return response