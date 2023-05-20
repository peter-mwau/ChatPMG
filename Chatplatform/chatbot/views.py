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
    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            form.save()
            query = form.cleaned_data.get('query')

            URL = "https://api.openai.com/v1/chat/completions"
            # api_key = "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"

            payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": query}],
            "temperature" : 1.0,
            "top_p":1.0,
            "n" : 1,
            "stream": False,
            "presence_penalty":0,
            "frequency_penalty":0,
            }

            headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
            }

            response = requests.post(URL, headers=headers, json=payload, stream=False)
     

            # response = requests.post("https://elitecode-chatglm-6b-chatbot.hf.space/run/predict", json={
	        # "data": [
		    #     query,
		    #     "Hello",
	        # ]
            # }).json()

            # data = response["data"]
            # # print(data)
            # response = data[1]
            print(response.content)

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
