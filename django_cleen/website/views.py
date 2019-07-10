from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'website/home.html')

def about(request):
	return render(request, 'website/about.html')

def book_cleen(request):
	return render(request, 'website/book.html')

def join_cleen(request):
	return render(request, 'website/join.html')

def help_cleen(request):
	return render(request, 'website/help.html')