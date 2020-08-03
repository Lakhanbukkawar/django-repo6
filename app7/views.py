from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def cal (request):
    val1=int(request.POST.get("val1"))
    val2=int(request.POST.get("val2"))
    op=request.POST.get("op")
    res=0
    if(op=="+"):
        res=val1+val2
    elif(op=="-"):
        res=val1-val2
    elif(op=="*"):
        res=val1*val2
    elif(op=="/"):
        res=val1/val2
    return HttpResponse(res)