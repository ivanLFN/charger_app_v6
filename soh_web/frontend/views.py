from django.shortcuts import render

def main_app(request):
    return render(request, 'main_app.html')
