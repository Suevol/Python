from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpRequest

def main(request):
	title = 'Главная'
	return render(request, 'main_app/index.html', {'title': title})

def contacts(request):
	title = 'Контакты'
	return render(request, 'main_app/contacts.html', {'title': title})

def goods(request):
	title = 'Товары'
	return render(request, 'main_app/goods.html', {'title': title})
