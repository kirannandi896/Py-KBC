import requests
import random
import time
import pygame
import threading
import pyttsx3



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    rate = 150
    print(audio)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', 10)
    engine.say(audio)
    engine.runAndWait()

def welcome(name):
    t = time.localtime()
    h = t.tm_hour
    if h < 12:
        speak("Good Morning " + name)
    elif h < 16:
        speak("Good Afternoon " + name)
    else:
        speak("Good Evening " + name)

def play_music():
    pygame.init()
    pygame.mixer.music.load("surprise.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)



#Main Code -------------->>>>>>>>>
speak("-------------------WELCOME TO PYTHON PROGRAM----------------------")
current_time = time.strftime("%H:%M:%S", time.localtime())
print("Current Time =", current_time)
speak("What is your name?")
time.sleep(1)
speak("Let's know your name first!\nEnter your name: ")
name = input()
time.sleep(2)
welcome(name)
print("Loading...")
time.sleep(4)
speak("WELCOME TO KBC")
music_thread = threading.Thread(target=play_music)
music_thread.start()
speak("Kaun Banega Crorepati")

time.sleep(10)
speak("Your Game will start in 3 seconds")
speak("Get ready")
time.sleep(1)
speak("1")
time.sleep(1)
speak("2")
time.sleep(1)
speak("and...")
time.sleep(1)
speak("3")
time.sleep(1)
speak("Let's Go!!")
time.sleep(2)
print("  \n")
speak("The questions are of Nature Science Category, so take your time and answer them correctly")
speak("Whishing you All the Best!")
speak("So " + name + " Your First Question is...")
time.sleep(3)

amount = 5000
score = 00

for i in range(5):
    url = "https://opentdb.com/api.php?amount=50&category=17&difficulty=easy"
    response = requests.get(url)
    data = response.json()
    question = data["results"][0]["question"]
    options = data["results"][0]["incorrect_answers"] + [data["results"][0]["correct_answer"]]
    random.shuffle(options)

    speak(question)
    for i, option in enumerate(options):
        speak(f"{i + 1}. {option}")

    user_answer = int(input("Enter your answer (Option number): ")) - 1
    if options[user_answer] == data["results"][0]["correct_answer"]:
        speak("Hurray!!!!!\nYour answer is Correct!")
        speak("Congratulations " + name)
        speak("You have earned 5000 Rupees")
        score += amount
    else:
        speak("Oops!!!!!\nYour answer is Incorrect!")
        speak("Better luck next time " + name)
        speak("You have lost 5000 Rupees")
        score -= amount
    print("\n")

print("   \n")
time.sleep(6)
speak("So you have won rupees - " + str(score))
time.sleep(2)
speak("Thanks for playing!!")
time.sleep(2)
speak("And Once again...")
time.sleep(1)
speak("Congratulations " + name)
time.sleep(3)
speak("Hope to see you again soon...")
time.sleep(2)
speak("Thanks for playing!!")
time.sleep(5)
speak("Closing program in 10 seconds...")
time.sleep(10)





