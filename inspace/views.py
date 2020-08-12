from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from inspace.models import 테이블 이름


# 게시판
def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            email = request.session['email']
            # select * from user where email = ?
            user = User.objects.get(email=email)
            # insert into article (title, content, user_id) values (?, ?, ?)
            article = Article(title=title, content=content, user=user)
            article.save()
            return render(request, 'write_success.html')
        except:
            return render(request, 'write_fail.html')
    return render(request, 'write.html')