from django.shortcuts import render 

def index(request):
    template_name = 'index.html'
    context = {
        'title':'Halaman Home'
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'about.html'
    context = {
        'title':'Halaman About'
    }
    return render(request, template_name, context)
