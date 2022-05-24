from django.shortcuts import render
from django.http import HttpResponse
import json

x = '{"name":"John",\n"age":25}'

y = {
	"name": "alex",
	"age": 25
}

z = json.dumps(y, indent=4, separators=(", ", " = ")) #separators=(". ", " = ")

# Create your views here.
# Request handler.

def me(request):
	# return HttpResponse(x)
	# return HttpResponse("Hello World")
	return HttpResponse(z)
	# return render(request, "about.html", y)

def another(request):
	return render(request, "about.html", y)