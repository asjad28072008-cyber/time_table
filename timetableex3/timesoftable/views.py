from django.shortcuts import render

# Create your views here.
def time(request):
    return render(request,'time.html')