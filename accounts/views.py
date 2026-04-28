from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# وظيفة إنشاء حساب جديد (Register)
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # تسجيل الدخول تلقائياً بعد إنشاء الحساب
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# وظيفة تسجيل الدخول (Login)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# وظيفة تسجيل الخروج (Logout)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    # الصفحة الرئيسية
def home_view(request):
    return render(request, 'accounts/home.html')