from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .chatbot_logic import generate_response  # Import the chatbot logic

def chatbot_view(request):
    if request.method == 'GET':
        return render(request, 'chatbot/chatbot.html')



@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if not user_message:
            return JsonResponse({'error': 'Message cannot be empty'}, status=400)

        # Generate a response using the chatbot logic
        bot_response = generate_response(user_message)
        return JsonResponse({'response': bot_response}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
