import random

# Define lists of responses
greetings = ["Hello!", "Hi there!", "Hey, how are you?"]
small_talk = ["How's your day going?", "Nice weather today, isn't it?", "What's new with you?"]
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He’ll stop at nothing to avoid them!"
]
trivia = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars"
}
farewells = ["Goodbye!", "See you later!", "Have a great day!"]

def greeting_bot():
    print("Welcome! I'm your friendly greeting bot.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print(random.choice(greetings))
        elif "how's" in user_input or "weather" in user_input or "new" in user_input:
            print(random.choice(small_talk))
        elif "joke" in user_input or "funny" in user_input:
            print(random.choice(jokes))
        elif "trivia" in user_input or "question" in user_input:
            question = random.choice(list(trivia.keys()))
            print(question)
            user_answer = input("You: ").strip().lower()
            if user_answer == trivia[question].lower():
                print("Correct!")
            else:
                print(f"Sorry, the correct answer is: {trivia[question]}")
        elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
            print(random.choice(farewells))
            break
        else:
            print("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    greeting_bot()