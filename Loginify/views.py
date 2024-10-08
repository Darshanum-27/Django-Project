from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Hello, Django!")

@csrf_exempt
def LoginPage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserData.objects.get(email=email)
            if user.password == password:
                return HttpResponse(email+" you have successfully LoggedIn")
                # return render(request, 'success.html', {'user': user})
            else:
                return render(request, 'LoginPage.html', {'error': 'Invalid username or password.'})
        except UserData.DoesNotExist:
            return render(request, 'LoginPage.html', {'error': 'User  not exist'})

    return render(request, 'LoginPage.html')

def SignUpView(request):
    if request.method == 'POST':
        username  = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print("inside if")
        if not UserData.objects.filter(email=email).exists():
            new_user = UserData(username=username, email=email, password=password)
            new_user.save()
            return redirect('LoginPage')
    return render(request, 'SignUpPage.html')

def DisplayAllUsers(request):
    return render(request, 'DisplayAllUsers.html', {'users': UserData.objects.all()})

def DeleteUser(request, email):
    DeletedUserObject = get_object_or_404(UserData, email=email)
    if request.method == 'POST':
        DeletedUserObject.delete()
        return redirect('AllUsers')
    return render(request, 'DeleteConfirmation.html', {'user': DeletedUserObject})

def GetUserInfo(request, email):
    return render(request, 'GetUserInfoPage.html', {'user': get_object_or_404(UserData, email=email)})

def UpdateUser(request, username):
    UpdateUserObject = get_object_or_404(UserData, username=username)
    if request.method == 'POST':
        UpdateUserObject.email = request.POST['email']
        UpdateUserObject.password = request.POST['password']
        UpdateUserObject.save()
        return redirect('AllUsers')
    return render(request, 'UpdateUser.html', {'user': UpdateUserObject})