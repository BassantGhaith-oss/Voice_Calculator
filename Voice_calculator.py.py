# First Import The Required Libraries

import sounddevice as sd
import wavio
import whisper
import time
import webbrowser
import os
import sys
import re
# Important Parameters 

Sample_rate =16000
Duration_sec = 6
FileName = "Bassant.wav"

# Importing The Model

print(" Wait until loading the whisper model.....")
model = whisper.load_model("base")
print("Model loaded successfuly")

# Defining important Functions

def record_to_wav():
     print(f"recording {Duration_sec} seconds ......speak now ")
     audio = sd.rec(int(Duration_sec * Sample_rate), samplerate = Sample_rate , channels =1, dtype="int16")
     sd.wait()
     wavio.write(FileName,audio,Sample_rate,sampwidth =2 )
     print(f"Saved Recording to {FileName}")

def transcribe(FileName):
     result = model.transcribe(FileName)
     text = result["text"].strip().lower()
     print(f" You Said :  {text}")
     return text


def calculate(command):
    numbers = re.findall(r'\d+(?:\.\d+)?', command)

    if len(numbers) < 2:
        print("I need two numbers")
        return

    num1 = float(numbers[0])
    num2 = float(numbers[1])

    if "plus" in command or "add" in command:
        result = num1 + num2

    elif "minus" in command or "subtract" in command:
        result = num1 - num2

    elif "times" in command or "multiply" in command:
        result = num1 * num2

    elif "divided by" in command or "divide" in command:
        if num2 == 0:
            print("Cannot divide by zero")
            return

        result = num1 / num2

    else:
        print("Operation not recognized")
        return

    print(f"Result: {result}")

def define_command(command):
    command = command.lower()

    if "exit" in command or "quit" in command or "stop" in command:
        print("Closing calculator")
        return False

    elif ("plus" in command or "add" in command or
          "minus" in command or "subtract" in command or
          "times" in command or "multiply" in command or
          "divided by" in command or "divide" in command):

        calculate(command)
        return True

    else:
        print("Command not recognized")
        return True
# Main Functionality of The Code

while True:
    record_to_wav()
    command = transcribe(FileName)
    define_command(command)