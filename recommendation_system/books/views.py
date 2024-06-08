from django.shortcuts import render, redirect
from .models import Emenitites, Books
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required(login_url="/login/")
def home(request):
	#emenities = Emenitites.objects.all()
	#context = {'emenities': emenities}
	return render(request, 'home.html', context)

@login_required(login_url="/login/")
def api_books(request):
	books_objs = Book.objects.all()
	
	price = request.GET.get('price')
	if price:
		books_objs = books_objs.filter(price__lte=price)
		
	emenities = request.GET.get('emenities')
	if emenities:
		emenities = [int(e) for e in emenities.split(',') if e.isdigit()]
		books_objs = books_objs.filter(emenities__in=emenities).distinct()
	
	payload = [{'book_name': book_obj.book_name,
				'book_description': book_obj.book_description,
				'book_image': book_obj.book_image,
				'price': book_obj.price} for book_obj in books_objs]
	
	return JsonResponse(payload, safe=False)

def login_page(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_obj = User.objects.filter(username=username)
			
			if not user_obj.exists():
				messages.error(request, "Username not found")
				return redirect('/login/')
			
			user_obj = authenticate(username=username, password=password)
			
			if user_obj:
				login(request, user_obj)
				return redirect('/')
			
			messages.error(request, "Wrong Password")
			return redirect('/login/')
			
		except Exception as e:
			messages.error(request, "Something went wrong")
			return redirect('/register/')
		
	return render(request, "login.html")

def register_page(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_obj = User.objects.filter(username=username)
			
			if user_obj.exists():
				messages.error(request, "Username is taken")
				return redirect('/register/')
			
			user_obj = User.objects.create(username=username)
			user_obj.set_password(password)
			user_obj.save()
			
			messages.success(request, "Account created")
			return redirect('/login/')
		
		except Exception as e:
			messages.error(request, "Something went wrong")
			return redirect('/register/')
	
	return render(request, "register.html")

def custom_logout(request):
	logout(request)
	return redirect('login')

