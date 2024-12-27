from django.shortcuts import render,redirect
from .forms import QuestionnaireForm
from django.contrib.auth.decorators import login_required
from .models import QuestionnaireResponse

@login_required
def questionnaire_view(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            total_score = sum(int(value) for value in request.POST.values() if value.isdigit())

            response = form.save(commit=False)
            response.user = request.user  # Associate the response with the logged-in user
            response.total_score = total_score  
            response.save()

            if total_score <= 23:
                return redirect('ok')
            elif total_score <= 28:
                return redirect('mid')
            else:
                return redirect('severe')

    else:
        form = QuestionnaireForm()

    return render(request, 'ques/questionnaire.html', {
        'form': form,
        'user': request.user,  # Pass the logged-in user to the template
    })



def ok(request):
    return render(request,'ques/ok.html')

def mid(request):
    return render(request,'ques/mid.html')

def severe(request):
    return render(request,'ques/severe.html')