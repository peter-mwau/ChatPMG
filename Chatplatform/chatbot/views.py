from django.shortcuts import render, redirect
from .models import Chatbot
from .forms import ChatbotForm
import requests
import openai

# Create your views here.

# def chat(request):
#     if request.method == 'POST':
#         form = ChatbotForm(request.POST)
#         if form.is_valid():
#             form.save()
#             query = form.cleaned_data.get('query')
     

#             response = requests.post("https://elitecode-chatglm-6b-chatbot.hf.space/run/predict", json={
# 	        "data": [
# 		        query,
# 		        "Hello",
# 	        ]
#             }).json()

#             data = response["data"]
#             # print(data)
#             response = data[1]
#             print(response)

#             form = ChatbotForm(initial={'response': response})

#             context = {
#                 'form': form,
#                 'response': response,
#             }
#             return render(request, 'chatUI.html', context)
#     else:
#         form = ChatbotForm()
#         context = {
#             'form': form,
#         }
#     return render(request, 'chatUI.html', context)


def chat(request):
    openai.api_key = "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"
    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            form.save()
            query = form.cleaned_data.get('query')

            URL = "https://api.openai.com/v1/chat/completions"
            
            messages = [
            {"role": "system", "content": "You are a kind helpful assistant."},
            ]

            while True:
                # message = input("User : ")
                message = query
                if message:
                    messages.append(
                    {"role": "user", "content": message},
                    )
                    chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                    )
    
                reply = chat.choices[0].message.content
                print(f"ChatGPT: {reply}")
                # messages.append({"role": "assistant", "content": reply})
                response = reply

                form = ChatbotForm(initial={'response': response})

                context = {
                'form': form,
                'response': response,
                }
                return render(request, 'chatUI.html', context)
    else:
        form = ChatbotForm()
        context = {
            'form': form,
        }
    return render(request, 'chatUI.html', context)
