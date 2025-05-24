import google.generativeai as genai
import ast
import re

# Configure your Gemini API key
genai.configure(api_key="Paste your API Key here")

model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-1219') #enter you model here by choosing from the list of models you get when you run getmodel.py

prompt = """
Generate 10 general knowledge multiple choice questions. Each should have 4 options and indicate the correct one using a number (1 to 4).The difficulty level of the questions should gradually increase from easy to hard. Format the response as a Python list of lists. Example format:
[
    ["What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3],
    ...
]
"""

response = model.generate_content(prompt)
print("Raw Gemini response:\n", response.text)

text = response.text.strip()

#Remove code block markdown if it exists
if "```" in text:
    match = re.search(r"```(?:python)?(.*?)```", text, re.DOTALL)
    if match:
        text = match.group(1).strip()

#Replace curly quotes with straight ones (just in case)
text = text.replace("“", "\"").replace("”", "\"")

#Safely evaluate the list into Python format
try:
    questions = ast.literal_eval(text) #ast stands for Abstract Syntax Tree and it's a safer alternative to eval and it is used to parse the string into a Python object 
except Exception as e:
    print("Failed to parse Gemini response:", e)
    questions = []
i=1000
j=0
for question in questions:
    print(question[0])#it gests the question
    #it gets the options
    print(" Option 1: ", question[1])
    print(" Option 2: ", question[2])
    print(" Option 3: ", question[3])
    print(" Option 4: ", question[4])
    a=int(input("enter the correct option number: "))
    if a==question[5]:
        print("correct\n")
        i+=1000 
        j+=1
        print("Your Prize is: ", i,"\n")
    else:
        print(f"\nwrong \nCorrect answer is: {question[5]}\n")
        print("Game Over")  
        break
print("Your won: ",j*i,"\n")
