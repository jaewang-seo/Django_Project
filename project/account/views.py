from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

#회원가입
def signup(request):

    # POST요청이 왔을 때, 새로운 유저를 만듬
    if request.method == 'POST':
        
        # 비번 == 비번확인
        if request.POST['password'] == request.POST['confirm']:

            # username과, password를 new생성
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])

            # 로그인해줌
            auth.login(request, user)
            return redirect('/')

    # GET요청이 왔을 때, 회원가입 화면 띄움
    return render(request, 'sigup.html')

#로그인
def login(request):

    # POST요정이 왔을 때, 로그인 절차 ㄱㄱ
    if request.method == "POST"
        
        # 아이디랑 비번 지정
        username = request.POST['username']
        password = request.POST['password']

        # 아디와 비번이 일치하는 user 객체를 가져옴 
        user = auth.authenticate(request, username=username, password=password)

        # 회원가입 되있는지 확인

        # 객체가 있으면
        if user is not None:

            # 로그인
            auth.login(request,user)
            return redirect('/')
        
        # 객체가 없으면 
        else:

            # 에러메세지 띄우고, 다시 로그인창으로 감
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})

# 로그아웃
def logout(request):

    # logout으로 POST요청이 왔을 때
    if request.method == 'POST':
        auth.logout(request)





