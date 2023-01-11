from django.shortcuts import render
from .forms import ZodiacForm, ZodiacForm2 
from .zodiac_calculator import *


from django.contrib import messages

# Create your views here.
def calculate_zodiac_sign(request):
    if request.method == 'POST':
        form = ZodiacForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            month = form.cleaned_data['month']
            astro_sign = zodiac_sign(day, month)
            messages.success(request, f"Your star sign is {astro_sign}")
            return render(request,'zodiac/result.html', {'zodiac_sign': astro_sign})
    else:
        form = ZodiacForm()
    return render(request, 'zodiac/result.html', {'form': form})


def cal_zod(request):
    if request.method == 'POST':
        form = ZodiacForm2(request.POST)
        if form.is_valid():
            birthdate = form.cleaned_data['birthdate']
            day = birthdate.day
            month = birthdate.strftime('%B').lower()
            astro_sign = zodiac_sign(day, month)
            return render(request,'zodiac/form2.html', {'zodiac_sign': astro_sign})
    else:
        form = ZodiacForm2()
    return render(request, 'zodiac/form2.html', {'form': form})