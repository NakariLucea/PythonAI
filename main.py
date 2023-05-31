#Code by Nakari-
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY") #Its easy for repl.it users, you will ned to put OPENAI_API_KEY as a secret and the api key as your value.

while True: #Set loop of the questions
 pregunta = input("Cual es tu pregunta? \n")

 if pregunta.lower() == "apagate": #if you type "Apagate" the script will shut down
   break
   print("Hasta la proxima!!")
 Completion = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
    {"role": "system", "content": "Hola!"},
    {"role": "user", "content": pregunta}
 ]
 )

 print("\n" + Completion.choices[0].message.content + "\n")
