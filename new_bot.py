import requests
import random

# Define lists of responses
greetings = ["Hello!", "Hi there!", "Hey, how are you?"]
small_talk = ["How's your day going?", "Nice weather today, isn't it?", "What's new with you?"]
farewells = ["Goodbye!", "See you later!", "Have a great day!"]

# Function to get weather information
def get_weather(city):
    api_key = "9cac778a210024312c2c659148707129"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The weather in {city} is currently {weather_desc} with a temperature of {temperature}°C."
    else:
        return "City not found. Please check the city name and try again."

def get_trivia():
    url = "https://opentdb.com/api.php?amount=2&category=9&difficulty=easy"
    response = requests.get(url)
    data = response.json()
    
    if data["response_code"] == 0:
        questions = data["results"]
        return questions
    else:
        return None

def get_joke():
    API_KEY = "eERM9krHF4wnneZT+yctOw==vD8RDYhPHmqjhZhk"
    url = "https://api.api-ninjas.com/v1/jokes"
    headers = {
        'X-Api-Key': API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        joke = response.json()[0]['joke']
        return joke
    else:
        return "Sorry, I couldn't fetch a joke at the moment."

def greeting_bot():
    print("Welcome! I'm your friendly greeting bot.")
    while True:
        user_input = input("You: ").strip().lower()
        
        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print(random.choice(greetings))
        elif "name" in user_input:
            print("My name is The Friendly Bot :)")
        elif "how's" in user_input or "new" in user_input:
            print(random.choice(small_talk))
        elif "joke" in user_input or "funny" in user_input:
            print(get_joke())
        elif "trivia" in user_input or "question" in user_input:
            questions = get_trivia()
            if questions:
                for question in questions:
                    print(question["question"])
                    user_answer = input("You: ").strip().lower()
                    correct_answer = question["correct_answer"].strip().lower()
                    if user_answer == correct_answer:
                        print("Correct!")
                    else:
                        print(f"Sorry, the correct answer is: {question['correct_answer']}")
            else:
                print("Sorry, I couldn't fetch trivia questions right now.")
        elif "weather" in user_input:
            city = input("Please enter the city name: ").strip()
            print(get_weather(city))
        elif "bye" in user_input or "goodbye" in user_input or "see you" in user_input:
            print(random.choice(farewells))
            break
        else:
            print("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    greeting_bot()