from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from space.models import User
# from inspace.models import 테이블 이름


# 게시판
def write(request):
    return render(request, 'write.html')

# 회원가입
def signup(request):
    if request.method == 'POST':
        # 회원정보 저장
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            User.objects.get(email=email)
        except:
            user = User(email=email, name=name, password=password)
            user.save()
            return HttpResponseRedirect('/inspace/signin/')

        return HttpResponseRedirect('/inspace/signup/')
    # 회원가입을 위한 양식(HTML) 전송
    return render(request, 'signup.html')

# 로그인
def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(email=email, password=pwd)
            request.session['email'] = email
            
            return render(request, 'mypage.html')
        except:
            return HttpResponseRedirect('')

    return render(request, 'signin.html')

# 로그아웃
def signout(request):
    del request.session['email'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('inspace/signin/')

def mypage(request):
    return render(request, 'mypage.html')
