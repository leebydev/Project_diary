from django.http import HttpResponse
from django.contrib import messages

# logout 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from users.models import Member

# 만든 loginForm 불러오기
from users.forms import LoginForm

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.
# 함수명과 장고가 제공해주는 모듈이름이 겹침 주의
# render : templates을 불러옴
# redirect : URL로 이동 => 이동하는 URL에 맞는 view가 다시 실행되고, render할지/redirect할지 결정
def login(request):
    if request.method == 'GET':
        login_form = LoginForm()
        context = {
            "my_form": login_form
        }
        return render(request, 'users/login.html', context)

    elif request.method == 'POST':
        # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        member = Member.objects.get(username=username)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            request.session['user'] = member.id
            return redirect('users:test')  # 하고 홈으로 보냄

        # 유저 객체가 없다면
        elif user is None:
            messages.warning(request, "아이디 또는 비밀번호가 일치하지 않습니다. :D")
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')


def logout(request):
    # 장고가 제공해주는 logout기능 사용
    django_logout(request)
    return redirect('home')


def home(request):
    user_id = request.session.get('user')

    if user_id:
        member = Member.objects.get(pk=user_id)
        context = {
            'member': member
        }
        # return HttpResponse(member.nickname)
        return redirect('home')

    return HttpResponse('Home!')


# 회원가입
def signup2(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('image')
        # if request.FILES.get('image'):
        #     image = request.FILES.get('image')
        # else:
        #     image = 'C:/python-django/AI_Project/static/img/짱구.jpeg'

        print(password != password2)

        if not (username and nickname and password and password2 and image):
            messages.warning(request, "모든 칸을 채워주세용!")
            return redirect('users:signup')

        elif password != password2:
            messages.warning(request, "비밀번호가 일치하지 않습니다")
            return redirect('users:signup')

        else:
            user = Member.objects.create_user(
                username=username,
                nickname=nickname,
                password=password,
                image=image
            )
            user.save()
        return redirect('users:login')
    return render(request, "users/signup.html")
