from django.shortcuts import render


from django.http import HttpResponse
def mycv(request):
    return render(request,'index.html')