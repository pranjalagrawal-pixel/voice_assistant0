import speech_recognition as sr  # pyright: ignore
import pyttsx3
import webbrowser
import datetime
import os
import pywhatkit
import tkinter as tk
from tkinter import scrolledtext

# ========== TEXT TO SPEECH ==========
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    output_box.insert(tk.END, "Assistant: " + text + "\n")
    output_box.see(tk.END)

# ========== SPEECH RECOGNITION ==========
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        output_box.insert(tk.END, "You: " + command + "\n")
        return command.lower()
    except:
        speak("Sorry, I didn't understand.")
        return ""

# ========== COMMAND HANDLER ==========
def run_command(command):

    if "hello" in command:
        speak("Hello, how can I help you?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "send whatsapp" in command:
        speak("Tell the phone number with country code")
        number = input("Enter number (e.g. +911234567890): ")

        speak("What is the message?")
        message = listen()

        speak("Sending message")
        pywhatkit.sendwhatmsg_instantly(number, message)

    elif "turn on light" in command:
        speak("Turning on the light")
        print("Smart Light: ON")

    elif "turn off light" in command:
        speak("Turning off the light")
        print("Smart Light: OFF")

    elif "who are you" in command:
        speak("I am your personal voice assistant.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        root.quit()

    else:
        speak("I don't know that command yet.")

# ========== BUTTON FUNCTION ==========
def start_listening():
    command = listen()
    run_command(command)

# ========== GUI ==========
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("500x400")

label = tk.Label(root, text="Voice Assistant", font=("Arial", 16))
label.pack(pady=10)

listen_button = tk.Button(root, text="Start Listening", command=start_listening)
listen_button.pack(pady=10)

output_box = scrolledtext.ScrolledText(root, width=60, height=15)
output_box.pack(pady=10)

root.mainloop()