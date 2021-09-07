from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "google/index.html")

def gsearch(request):
	return render(request, "google/gsearch.html", {})

def gimgsearch(request):
	return render(request, "google/gimgsearch.html", {})

def gadvsearch(request):
	return render(request, "google/gadvsearch.html", {})