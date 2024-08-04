from django.shortcuts import render
from .forms import Register_User_Form
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class home(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        return Response({"message": f"Welcome {user} to Home page!, Successfully entering the page because you are authenticated and your JWT is valid!"}, status=200)

def register(request):
    if request.method == "POST":
        form = Register_User_Form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = Register_User_Form()
        
    context = {'form': form}
    return render(request, 'register.html', context)
