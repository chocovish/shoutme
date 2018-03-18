from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect
from .forms import SignupForm, TestForm,User,CommentForm,ProfileUpdate,ProfileUpdate2,info
from .models import Comments

# Create your views here.

def home(request):
    return render(request,"home.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            u = form.save()
            info.objects.create(user=u)
            return HttpResponseRedirect('/login')
    return render(request,'r.html',{'form':SignupForm})


def test(request):
    if request.method == "POST":
        print(request.FILES)
        form  = TestForm(request.POST,request.FILES)
        if form.is_valid():
            return HttpResponse("success")
        return render(request,'form.html',{'form':form})
    return render(request,'form.html',{'form':TestForm})


def propage(request,username):
    pro = User.objects.get(username=username)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.profile = pro
            com.save()
            return HttpResponseRedirect("/")
    return render(request,'profile.html',{'profile': pro, 'form':CommentForm})


def profile(request):
    if str(request.user) == "AnonymousUser":
        return HttpResponse("You are not logged in, Log In First to edit profile")
    if request.method == "POST":
        form = ProfileUpdate(request.POST,instance=request.user)
        form2 = ProfileUpdate2(request.POST,request.FILES,instance=request.user.info)
        if form.is_valid and form2.is_valid():
            print("!!!!!!!!  valid !!!!!!!!!!!!")
            form2.save()
            form.save()
            return HttpResponseRedirect("/profile")
    form = ProfileUpdate(instance=request.user)
    form2 = ProfileUpdate2(instance=request.user.info)
    return render(request,'profileupdate.html',{'form': form, "form2":form2})
    

def viewshout(request):
    if str(request.user) == 'AnonymousUser':
        return HttpResponseRedirect("/login")
    clist = Comments.objects.filter(profile=request.user)
    return render(request,'viewshout.html',{'clist':clist})