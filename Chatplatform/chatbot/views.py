from django.shortcuts import render, redirect
from .models import Chatbot
from .forms import ChatbotForm
import requests

# Create your views here.

def chat(request):
    if request.method == 'POST':
        form = ChatbotForm(request.POST)
        if form.is_valid():
            form.save()
            query = form.cleaned_data.get('query')
     

            response = requests.post("https://drsong-chatglm-6b-chatbot.hf.space/run/predict", json={
	        "data": [
		        query,
		        "Hello",
	        ]
            }).json()

            data = response["data"]
            # print(data)
            response = data[1]
            print(response)

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

    # else:
    #     form = ChatbotForm()
    #     context = {
    #         'form': form,
    #     }
    # return render(request, 'chatUI.html', context)

