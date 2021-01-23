from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate
from dateutil.relativedelta import relativedelta
from . import forms
from django.contrib import messages

click = 0
varislug = 0
varislug2 = 0
varislug3 = 0
planoftheday = 0


def home(request):
    return render(request, 'calentemp/home.html')

def calendarnext(request):
    global click
    click = click+1
    now = datetime.today()+ relativedelta(months=click)
    today = now.strftime("Y%m_%Y")
    u = request.user
    today2 = datetime.today()
    today3 = int(today2.strftime("%d"))
    clickmois = click
    
    
    if(today=="Y01_2020"):
        Today = A_2020_January
    elif(today=="Y02_2020"):
        Today = B_2020_February
    elif(today=="Y03_2020"):
        Today = C_2020_March  
    elif(today=="Y04_2020"):
        Today = D_2020_April
    elif(today=="Y05_2020"):
        Today = E_2020_May        
    elif(today=="Y06_2020"):
        Today = F_2020_June       
    elif(today=="Y07_2020"):
        Today = G_2020_July
    elif(today=="Y08_2020"):
        Today = H_2020_August
    elif(today=="Y09_2020"):
        Today = I_2020_September
    elif(today=="Y10_2020"):
        Today = J_2020_October
    elif(today=="Y11_2020"):
        Today = K_2020_November
    elif(today=="Y12_2020"):
        Today = L_2020_December
    elif(today=="Y01_2021"):
        Today = A_2021_January
    elif(today=="Y02_2021"):
        Today = B_2021_February
    elif(today=="Y03_2021"):
        Today = C_2021_March  
    elif(today=="Y04_2021"):
        Today = D_2021_April
    elif(today=="Y05_2021"):
        Today = E_2021_May        
    elif(today=="Y06_2021"):
        Today = F_2021_June       
    elif(today=="Y07_2021"):
        Today = G_2021_July
    elif(today=="Y08_2021"):
        Today = H_2021_August
    elif(today=="Y09_2021"):
        Today = I_2021_September
    elif(today=="Y10_2021"):
        Today = J_2021_October
    elif(today=="Y11_2021"):
        Today = K_2021_November
    elif(today=="Y12_2021"):
        Today = L_2021_December
    elif(today=="Y01_2022"):
        Today = A_2022_January
    elif(today=="Y02_2022"):
        Today = B_2022_February
    elif(today=="Y03_2022"):
        Today = C_2022_March  
    elif(today=="Y04_2022"):
        Today = D_2022_April
    elif(today=="Y05_2022"):
        Today = E_2022_May        
    elif(today=="Y06_2022"):
        Today = F_2022_June       
    elif(today=="Y07_2022"):
        Today = G_2022_July
    elif(today=="Y08_2022"):
        Today = H_2022_August
    elif(today=="Y09_2022"):
        Today = I_2022_September
    elif(today=="Y10_2022"):
        Today = J_2022_October
    elif(today=="Y11_2022"):
        Today = K_2022_November
    elif(today=="Y12_2022"):
        Today = L_2022_December       
       
    calendar = Today.objects.filter(user=u) 
    return render(request, 'calentemp/calendar.html', {'calendars': calendar,
                                                       'today3': today3,
                                                       'click': clickmois})

def calendarprev(request):
    global click    
    click = click-1
    now = datetime.today()+ relativedelta(months=click)
    today = now.strftime("Y%m_%Y")
    u = request.user
    today2 = datetime.today()
    today3 = int(today2.strftime("%d"))
    clickmois = click
    
    if(today=="Y01_2020"):
        Today = A_2020_January
    elif(today=="Y02_2020"):
        Today = B_2020_February
    elif(today=="Y03_2020"):
        Today = C_2020_March  
    elif(today=="Y04_2020"):
        Today = D_2020_April
    elif(today=="Y05_2020"):
        Today = E_2020_May        
    elif(today=="Y06_2020"):
        Today = F_2020_June       
    elif(today=="Y07_2020"):
        Today = G_2020_July
    elif(today=="Y08_2020"):
        Today = H_2020_August
    elif(today=="Y09_2020"):
        Today = I_2020_September
    elif(today=="Y10_2020"):
        Today = J_2020_October
    elif(today=="Y11_2020"):
        Today = K_2020_November
    elif(today=="Y12_2020"):
        Today = L_2020_December
    elif(today=="Y01_2021"):
        Today = A_2021_January
    elif(today=="Y02_2021"):
        Today = B_2021_February
    elif(today=="Y03_2021"):
        Today = C_2021_March  
    elif(today=="Y04_2021"):
        Today = D_2021_April
    elif(today=="Y05_2021"):
        Today = E_2021_May        
    elif(today=="Y06_2021"):
        Today = F_2021_June       
    elif(today=="Y07_2021"):
        Today = G_2021_July
    elif(today=="Y08_2021"):
        Today = H_2021_August
    elif(today=="Y09_2021"):
        Today = I_2021_September
    elif(today=="Y10_2021"):
        Today = J_2021_October
    elif(today=="Y11_2021"):
        Today = K_2021_November
    elif(today=="Y12_2021"):
        Today = L_2021_December
    elif(today=="Y01_2022"):
        Today = A_2022_January
    elif(today=="Y02_2022"):
        Today = B_2022_February
    elif(today=="Y03_2022"):
        Today = C_2022_March  
    elif(today=="Y04_2022"):
        Today = D_2022_April
    elif(today=="Y05_2022"):
        Today = E_2022_May        
    elif(today=="Y06_2022"):
        Today = F_2022_June       
    elif(today=="Y07_2022"):
        Today = G_2022_July
    elif(today=="Y08_2022"):
        Today = H_2022_August
    elif(today=="Y09_2022"):
        Today = I_2022_September
    elif(today=="Y10_2022"):
        Today = J_2022_October
    elif(today=="Y11_2022"):
        Today = K_2022_November
    elif(today=="Y12_2022"):
        Today = L_2022_December       
       
    calendar = Today.objects.filter(user=u) 
    return render(request, 'calentemp/calendar.html', {'calendars': calendar,
                                                       'today3': today3,
                                                       'click': clickmois})

def calendar(request):
    global click    
    click = 0
    now = datetime.today()+ relativedelta(months=click)
    today = now.strftime("Y%m_%Y")
    u = request.user
    today2 = datetime.today()
    today3 = int(today2.strftime("%d"))
    clickmois = click
    
    if(today=="Y01_2020"):
        Today = A_2020_January
    elif(today=="Y02_2020"):
        Today = B_2020_February
    elif(today=="Y03_2020"):
        Today = C_2020_March  
    elif(today=="Y04_2020"):
        Today = D_2020_April
    elif(today=="Y05_2020"):
        Today = E_2020_May        
    elif(today=="Y06_2020"):
        Today = F_2020_June       
    elif(today=="Y07_2020"):
        Today = G_2020_July
    elif(today=="Y08_2020"):
        Today = H_2020_August
    elif(today=="Y09_2020"):
        Today = I_2020_September
    elif(today=="Y10_2020"):
        Today = J_2020_October
    elif(today=="Y11_2020"):
        Today = K_2020_November
    elif(today=="Y12_2020"):
        Today = L_2020_December
    elif(today=="Y01_2021"):
        Today = A_2021_January
    elif(today=="Y02_2021"):
        Today = B_2021_February
    elif(today=="Y03_2021"):
        Today = C_2021_March  
    elif(today=="Y04_2021"):
        Today = D_2021_April
    elif(today=="Y05_2021"):
        Today = E_2021_May        
    elif(today=="Y06_2021"):
        Today = F_2021_June       
    elif(today=="Y07_2021"):
        Today = G_2021_July
    elif(today=="Y08_2021"):
        Today = H_2021_August
    elif(today=="Y09_2021"):
        Today = I_2021_September
    elif(today=="Y10_2021"):
        Today = J_2021_October
    elif(today=="Y11_2021"):
        Today = K_2021_November
    elif(today=="Y12_2021"):
        Today = L_2021_December
    elif(today=="Y01_2022"):
        Today = A_2022_January
    elif(today=="Y02_2022"):
        Today = B_2022_February
    elif(today=="Y03_2022"):
        Today = C_2022_March  
    elif(today=="Y04_2022"):
        Today = D_2022_April
    elif(today=="Y05_2022"):
        Today = E_2022_May        
    elif(today=="Y06_2022"):
        Today = F_2022_June       
    elif(today=="Y07_2022"):
        Today = G_2022_July
    elif(today=="Y08_2022"):
        Today = H_2022_August
    elif(today=="Y09_2022"):
        Today = I_2022_September
    elif(today=="Y10_2022"):
        Today = J_2022_October
    elif(today=="Y11_2022"):
        Today = K_2022_November
    elif(today=="Y12_2022"):
        Today = L_2022_December       
       
    calendar = Today.objects.filter(user=u) 
    return render(request, 'calentemp/calendar.html', {'calendars': calendar,
                                                       'today3': today3,
                                                       'click': clickmois})


def session_list(request, slug):
    global varislug
    global planoftheday
    first = request.user.first_name
    last = request.user.last_name
    varislug = slug
    planoftheday = M_DailyPlan.objects.filter(slugdaily=slug)
    return render(request, 'calentemp/sessions_list.html', {'dailyplans': planoftheday,
                                                            'first': first,
                                                            'last': last})

def exercise_list(request, slug, slugb):
    global varislug2
    global varislug3
    first = request.user.first_name
    last = request.user.last_name    
    u = request.user
    varislug2 = varislug
    varislug3 = slugb   
    if request.method == 'POST':
        form = forms.SaveData(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.title = varislug3
            instance.save()
            messages.info(request, 'Your data has been saved successfully!')
    else:    
        form = forms.SaveData()    
    session = N_Session.objects.filter(slugSess=slugb)

    return render(request, 'calentemp/exercises_list.html', {'sessions': session,
                                                             'form': form,
                                                             'varislug2': varislug2,
                                                             'varislug3': varislug3,
                                                             'first': first,
                                                             'last': last })

