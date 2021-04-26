from django.shortcuts import render, redirect
from.models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'index.html')

def register(request):
	errors = User.objects.user_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	user_with_email = User.objects.filter(email = request.POST('email'))
	if user_with_email:
		messages.error(request, 'That email is already registered.')
		return redirect('/')
	pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
	User.objects.create(
		username = request.POST['username'],
		email = request.POST['email'],
		password = pw_hash,
	)
	user = User.objects.filter(email = request.POST['email'])
	if user:
		registered_user = user[0]
		request.session['userId'] = registered_user.id
	return redirect('/messages/dashboard')

def login(request):
	errors = User.objects.user_validator(request.GET)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	