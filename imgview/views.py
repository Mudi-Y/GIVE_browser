from django.shortcuts import render

def image(request):
    return render(request,'imgview/image.html',{'title':'Image'})
