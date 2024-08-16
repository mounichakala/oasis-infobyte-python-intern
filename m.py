import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}\n")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return "None"
        return command.lower()

# Main function for the assistant
def assistant():
    speak("Hello! How can I help you today?")
    
    while True:
        command = take_command()
        
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {time}")
        
        elif 'wikipedia' in command:
            speak("What do you want to search on Wikipedia?")
            topic = take_command()
            results = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'play' in command:
            song = command.replace('play', '')
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
        
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        
        else:
            speak("I am sorry, I didn't get that. Can you please repeat?")

# Start the assistant
assistant()
