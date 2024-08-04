# Normal View importation packages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import Register_Form, Login_Form
from BackEnd.models import Author, Book
# Importation packages for API View protected by JWT
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

"""API View Protected with JWT Authentication"""
class ProtectedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Return a JSON response with a message
        return Response({"message": "This view is protected with JWT authentication"})


# View for the home page that requires the user to be authenticated
@login_required
def home(request):
    try:
        # Get the authenticated user
        user = request.user
        
        # Get the list of authors and books
        authors = Author.objects.all()
        books = Book.objects.all()
        
        context = {"user": user, "authors": authors, "books": books}
        return render(request, "home.html", context)
    except:
        return redirect('login')

# View for user registration
def register(request):
    if request.method == "POST":
        form = Register_Form(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = Register_Form()
        
    context = {'form': form}
    return render(request, 'register.html', context)

# View for user login
def login(request):
    if request.method == "POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/home/')  # Redirect to the home page after login
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = Login_Form()
    
    return render(request, 'login.html', {'form': form})

# View for user logout
def logout(request):
    auth.logout(request)  # Logout the user
    return 
