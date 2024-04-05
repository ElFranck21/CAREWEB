from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    return render(request, 'contact/contact.html')
def reports(request):
    return render(request, 'reports/reports.html')