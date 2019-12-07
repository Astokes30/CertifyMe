from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def myschool(request):
    return render(request, 'highschools.html')

def certifyschools(request):
    return render(request, 'colleges.html')

def whycertificate(request):
    return render(request, 'importance.html')

def certification(request):
    return render(request, 'college_certs.html')

def sign_in(request):
    return render(request, 'profile.html')

def blog(request):
    return render(request, 'blog.html')

def contactus(request):
    return render(request, 'contactus.html')

def faqs(request):
    return render(request, 'faqs.html')

def feedback(request):
    return render(request, 'feedback.html')

