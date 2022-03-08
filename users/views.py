from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

# logout 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from users.models import Member

# 만든 loginForm 불러오기
from users.forms import LoginForm


# Create your views here.
# 함수명과 장고가 제공해주는 모듈이름이 겹침 주의
# render : templates을 불러옴
# redirect : URL로 이동 => 이동하는 URL에 맞는 view가 다시 실행되고, render할지/redirect할지 결정

'''
def login(request):
    login_form = LoginForm()
    context = {
        "my_form": login_form
    }
    return render(request, 'users/login_test.html', context)
'''

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

        # if not (username and password):
        #     messages.warning(request, "모든 값을 입력하세요!")
        # else:
        #     member = Member.objects.get(username=username)
        #     if check_password(password, member.password):
        #         request.session['user'] = member.id

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        member = Member.objects.get(username=username)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            request.session['user'] = member.id
            return redirect('home')  # 하고 홈으로 보냄

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

'''
def login_process(request):
    # 사용자가 request를 보내는데, 그 방식이 POST 방식이라면
    if request.method == 'POST':
        # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            return redirect('home')  # 하고 홈으로 보냄

        # 유저 객체가 없다면
        elif user is None:
            messages.warning(request, "아이디 또는 비밀번호가 일치하지 않습니다. :D")
            return redirect('users:login')
    else:
        return render(request, 'users/login.html')
'''


def Home(request):
    user_id = request.session.get('user')

    if user_id:
        user = Member.objects.get(pk=user_id)
        print('ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ')
        return HttpResponse(user.username)

    return HttpResponse('Home!')

'''
def login_process(request):
    if request.method == "GET":
        return render(request, 'users/login_test.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if not (username and password):
            pass

        else:
            user = Member.objects.get(username=username)
            # print(member.id)

            if check_password(password, user.password):
                # print(request.session.get('user'))
                user_id = user.username
                request.session['user'] = user.id

                return redirect('/test')

            else:
                messages.warning(request, "비밀번호가 다릅니다 !_!")

        return render(request, 'users/login_test.html')
'''

# 회원가입

def signup2(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        image = request.FILES.get('image')
        print(password != password2)

        if not (username and nickname and password and password2):
            messages.warning(request, "프로필 사진을 제외한 모든 칸을 채워주세용!")
            return redirect('users:signup')

        elif password != password2:
            messages.warning(request, "비밀번호가 일치하지 않습니다")
            return redirect('users:signup')

        elif Member.objects.filter(username=username).exists():
            messages.warning(request, "아이디가 이미 사용중 입니다.")
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


def do_duplicate_check(request):
    print('아이디 중복 체크')
    username = request.GET.get('username')
    try:
        # 중복 검사 실패
        username = Member.objects.get(username=username)

    except:
        # 중복 검사 성공
        username = None

    if username is None:
        duplicate = "pass"
    else:
        duplicate = "fail"
    context = {'duplicate': duplicate}
    return JsonResponse(context)
