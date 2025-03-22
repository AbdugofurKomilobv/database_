from pyexpat.errors import messages
from django.shortcuts import redirect, render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from django.contrib.auth import authenticate,login

from common.forms import UserLoginForm


from .models import *



class EmployesView(ListView):
    model = Employes
    template_name = 'emp_view.html'
    context_object_name = 'emp_v'


class FormAdd(CreateView):
    model = Employes
    template_name = 'employes_add.html'
    fields = ['last_name', 'first_name', 'midle_name', 'email', 'phone', 'data_fild','fk_departamen', 'fk_region']
    success_url = reverse_lazy('emp')


# def LoginPage(request):

#     form = UserLoginForm()
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')


#         user = authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('emp')
        
#         else:
#             form = UserLoginForm()

#         return render(request=request,template_name='login.html',context={"form":form})

def LoginPage(request):
    form = UserLoginForm()  # Formani POST bo‘lmagan holatda ham yaratish kerak

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("emp")  # Login muvaffaqiyatli bo‘lsa, redirect

        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto‘g‘ri!")  

    return render(request, "login.html", {"form": form})  # ✅ To‘g‘ri return







