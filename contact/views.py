from django.shortcuts import render
import pyrebase
from .forms import ContactoForm



def home(request):
    return render(request, 'home/home.html')
def reports(request):
    return render(request, 'reports/reports.html')

def contact(request):
    form=ContactoForm()
    return render(request, 'contact/contact.html',{"form":form})

config={
  "apiKey": "AIzaSyDlkIFU8S_Y2bTYrKBFF9FIMuPGNDUyajU",
  "authDomain": "contactanos-c6748.firebaseapp.com",
  "databaseURL": "https://contactanos-c6748-default-rtdb.firebaseio.com",
  "projectId": "contactanos-c6748",
  "storageBucket": "contactanos-c6748.appspot.com",
  "messagingSenderId": "419719396234",
  "appId": "1:419719396234:web:999e2ff639c196a9a92673"
}
firebase=pyrebase.initialize_app(config)

