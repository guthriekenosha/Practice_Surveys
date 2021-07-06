from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def create(request):
    request.session['name'] = request.POST['your_name']
    request.session['location'] = request.POST['Location']
    request.session['language'] = request.POST['Language']
  
  

    return redirect('/survey_dash')

def dashboard(request): 
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
    }

    return render(request, 'survey.html')



