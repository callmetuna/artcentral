from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import pyrebase
from django.shortcuts import render
from pyrebase.pyrebase import Database

config = {
    'apiKey' : "AIzaSyAJZ34HvqHz94_q-cs68s1xmMSsrk95SnE",
    'authDomain': "artcentral-526a7.firebaseapp.com",
    'projectId': "artcentral-526a7",
    'storageBucket': "artcentral-526a7.appspot.com",
    'messagingSenderId': "872419911661",
    'appId': "1:8724199 11661:web:27ee010ed6dd5ab022e9e4",
    'measurementId' : "G-XBN296W10L"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def signIn(request):
    return render(request, "")
def home(request):
    return render(request, "")

def postsigIn(request):
    