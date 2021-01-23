from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from Calendar import forms
from Calendar import models


def signup_view(request):
    if request.method =='POST':
        form=UserCreationForm(request.POST)
      
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            forma1 = models.A_2020_January()
            forma1.user = request.user
            forma1.save()
            forma2 = models.A_2021_January()
            forma2.user = request.user
            forma2.save()            
            forma3 = models.A_2022_January()
            forma3.user = request.user
            forma3.save()            
            formb1 = models.B_2020_February()
            formb1.user = request.user
            formb1.save()
            formb2 = models.B_2021_February()
            formb2.user = request.user
            formb2.save()
            formb3 = models.B_2022_February()
            formb3.user = request.user
            formb3.save()            
            formc1 = models.C_2020_March()
            formc1.user = request.user
            formc1.save()
            formc2 = models.C_2021_March()
            formc2.user = request.user
            formc2.save()        
            formc3 = models.C_2022_March()
            formc3.user = request.user
            formc3.save()            
            formd1 = models.D_2020_April()
            formd1.user = request.user
            formd1.save()
            formd2 = models.D_2021_April()
            formd2.user = request.user
            formd2.save()            
            formd3 = models.D_2022_April()
            formd3.user = request.user
            formd3.save()            
            forme1 = models.E_2020_May()
            forme1.user = request.user
            forme1.save()
            forme2 = models.E_2021_May()
            forme2.user = request.user
            forme2.save()
            forme3 = models.E_2022_May()
            forme3.user = request.user
            forme3.save()            
            formf1 = models.F_2020_June()
            formf1.user = request.user
            formf1.save()
            formf2 = models.F_2021_June()
            formf2.user = request.user
            formf2.save()        
            formf3 = models.F_2022_June()
            formf3.user = request.user
            formf3.save()            
            formg1 = models.G_2020_July()
            formg1.user = request.user
            formg1.save()
            formg2 = models.G_2021_July()
            formg2.user = request.user
            formg2.save()            
            formg3 = models.G_2022_July()
            formg3.user = request.user
            formg3.save()            
            formh1 = models.H_2020_August()
            formh1.user = request.user
            formh1.save()
            formh2 = models.H_2021_August()
            formh2.user = request.user
            formh2.save()
            formh3 = models.H_2022_August()
            formh3.user = request.user
            formh3.save()            
            formi1 = models.I_2020_September()
            formi1.user = request.user
            formi1.save()
            formi2 = models.I_2021_September()
            formi2.user = request.user
            formi2.save()        
            formi3 = models.I_2022_September()
            formi3.user = request.user
            formi3.save()            
            formj1 = models.J_2020_October()
            formj1.user = request.user
            formj1.save()
            formj2 = models.J_2021_October()
            formj2.user = request.user
            formj2.save()            
            formj3 = models.J_2022_October()
            formj3.user = request.user
            formj3.save()            
            formk1 = models.K_2020_November()
            formk1.user = request.user
            formk1.save()
            formk2 = models.K_2021_November()
            formk2.user = request.user
            formk2.save()
            formk3 = models.K_2022_November()
            formk3.user = request.user
            formk3.save()            
            forml1 = models.L_2020_December()
            forml1.user = request.user
            forml1.save()
            forml2 = models.L_2021_December()
            forml2.user = request.user
            forml2.save()        
            forml3 = models.L_2022_December()
            forml3.user = request.user
            forml3.save()               
     
            return redirect('Calendar:calend')
    else :
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form':form})


def signin_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            
            return redirect('Calendar:calend')    
    else :
        form = AuthenticationForm()
    return render(request, 'login/signin.html', {'form':form})


def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('login:signin')


