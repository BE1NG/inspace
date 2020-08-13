from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from space.models import User, Posting
from django.http import JsonResponse  # JSON 응답



# 회원가입
def signup(request):
    if request.method == 'POST':
        # 회원정보 저장
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        try:
            User.objects.get(email=email)
        except:
            user = User(email=email, name=name, password=password, phone=phone)
            user.save()
            return HttpResponseRedirect('/inspace/signin/')
        return render(request, 'signup_id_exist.html', {'msg' : '중복 아이디'})
        # return HttpResponseRedirect('/inspace/signup/')
    # 회원가입을 위한 양식(HTML) 전송
    return render(request, 'signup.html')

# 아이디 중복검사
def check_id(request):
    email = request.GET.get('email')
    try:
            User.objects.get(email=email)
    except:
        return JsonResponse({'code':'아이디 중복 확인', 'msg':email + ' 사용 가능한 아이디입니다.'})
    return JsonResponse({'code':'아이디 중복 확인', 'msg': '중복된 아이디입니다.'})
    # DB 값 비교

    # result = {'code':'아이디 중복 확인', 'msg':email + ' 사용 가능한 아이디입니다.'}

    # return JsonResponse(result)

# 로그인
def signin(request):
    if request.method == 'POST':
        # 회원정보 조회
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # select * from user where email=? and pwd=?
            user = User.objects.get(email=email, password=password)
            request.session['email'] = email
            
            return HttpResponseRedirect('/inspace/mypage/')
        except:
            return render(request, 'signin.html')

    return render(request, 'signin.html')

# 로그아웃
def signout(request):
    del request.session['email'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/inspace/signin/')

def mypage(request):
    return render(request, 'mypage.html')



### 게시판 ###
def write(request):
    ### 사진업로드
    # if post
    # 파일 업로드 코드 동작
    # => 파일 저장 경로 / 파일명
    # Post(title=dd,content=dd, picture=OOOOOO)
    # post.save()

    if request.method == 'POST':
        try:
            email = request.session['email']
            user = User.objects.get(email=email)

            content = request.POST.get('content')
            # picture = request.POST.get('picture')
            location = request.POST.get('location')

            posting = Posting(content=content, picture=picture, location=location, email=user)
            posting.save()
            return HttpResponseRedirect('/inspace/signup/')
        except:
            return HttpResponseRedirect('/inspace/signin/')

    return render(request, 'write.html')


## 사진 업로드
import os
def upload(request):
    if request.method == 'GET':
      return render(request, 'upload.html', {})
    else:
        upload_file = request.FILES['my_file']
        try: # 디렉토리 생성
          os.mkdir('static/profile_image')
        except FileExistsError as e:
          pass
        file_name = upload_file.name
        with open('static/profile_image/' + file_name, 'wb') as file:
          for chunk in upload_file.chunks():
            file.write(chunk)
        return HttpResponse('파일 업로드 완료')


## 위도/경도 -> 주소
import requests
def coord_to_address(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    params = {'y': lat, 'x': lng}
    headers = {'Authorization': 'KakaoAK 8bf7271ae8d6c842984b0beb033e9b27'}
    result = requests.get('https://dapi.kakao.com/v2/local/geo/coord2regioncode.json', params=params, headers=headers)
    result = result.json()

    print(result)

    return JsonResponse(result)

