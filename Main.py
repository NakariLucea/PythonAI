import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


while True:
 pregunta = input("\033[34mCual es tu pregunta?\n\033[0n")

 if pregunta.lower() == "apagate":
   break
   print("Hasta la proxima!!")
 Completion = openai.ChatCompletion.create(
   model="gpt-3.5-turbo",
   messages=[
    {"role": "system", "content": "Hola!"},
    {"role": "user", "content": pregunta}
 ]
 )

 print("\033[32n" + Completion.choices[0].message.content + "\n")
