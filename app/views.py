from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app.models import box
import datetime,time

# Create your views here.
#@login_required(login_url='loginpage')
def loginpage(request):
    if request.method == 'POST':
        if 's1' in request.POST:
            name = request.POST.get('nam')
            pass1 = request.POST.get('password')
            user = authenticate(request,username=name,password=pass1)
            if user is not None:
                login(request,user)
                current_user = request.user
                user_id = current_user.id
                context = {'user_id' : user_id}
                #return render(request,'',context)
                return redirect('home')
            else:
                return HttpResponse("Email address or Password is incorrect")
        if 's2' in request.POST:
            uname = request.POST.get('name')
            email = request.POST.get('email')
            passw = request.POST.get('pass')
            cpassword = request.POST.get('cpass')
            if(passw!=cpassword):
                return HttpResponse("Your Password and Confirm Password are not same, Please check and try again....")
            my_user = User.objects.create_user(uname,email,passw)
            my_user.save()
            return redirect('loginpage')
            #return HttpResponse("User is created successfully....")
        
    return render(request,'login.html')

def homepage(request):
    if 's3' in request.POST:
        email = request.POST.get('email')
        message = request.POST.get('message')
        current_user = request.user
        id = (box.objects.last()).id
        id = id+1
        a = """
        
        
        
        
        
        If you want to give a reply to the sender use this id as a input --> """
        b = """ http://127.0.0.1:8000/reply/
        By this way your message will reach out to the sender"""
        message = message + a + str(id) + b
        nam = current_user.username
        em = current_user.email
        toem = request.POST.get('email')
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        x = box(name=nam,email=em,message=message,date=datetime.date.today(), time=current_time,toemail=toem)
        x.save()
        send_mail(
            'Queries',
            message,
            'qwertyks7122@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponse('Your message was sent successfully...')
    return render(request,'home.html')


def replypage(request):
    if 's4' in request.POST:
        id = request.POST.get('id')
        message = request.POST.get('message')
        id = int(id)-1
        x = box.objects.all()[id]
        a = x.email
        b = "This mail is from --> " + x.toemail
        send_mail(
            b,
            message,
            'qwertyks7122@gmail.com',
            [a],
            fail_silently=False,
        )
        return HttpResponse('Your reply was sent successfully...')
    return render(request,'reply.html')
