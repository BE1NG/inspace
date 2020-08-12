from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from inspace.models import 테이블 이름


# 게시판
def write(request):
    return render(request, 'write.html')

