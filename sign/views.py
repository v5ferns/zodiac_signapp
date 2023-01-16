from django.shortcuts import render
from .forms import ZodiacForm, PersonForm
from .zodiac_calculator import *
from . zodiac_calculator2 import *

from datetime import date




from django.contrib import messages

# Create your views here.
# This is the first calculation rendered to calculate_zodiac
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


# This is the second calculation rendered to zod_cal view and form2.html template below perfoming same task as above
def determine_star_sign(birthdate):
    # Determine the month and day of the birthdate
    month = birthdate.month
    day = birthdate.day    

    if month == 3 and day >= 21 or month == 4 and day <= 19:
        return 'aries'
    elif month == 4 and day >= 20 or month == 5 and day <= 20:
        return 'taurus'
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        return 'gemini'
    elif month == 6 and day >= 21 or month == 7 and day <= 20:
        return 'cancer'
    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        return 'leo'
    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        return 'virgo'
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        return 'libra'
    elif month == 10 and day >= 23 or month == 11 and day <= 22:
        return 'scopio'
    elif month == 11 and day >= 23 or month == 12 and day <= 21:
        return 'sagittarius'
    elif month == 12 and day >= 22 or month == 1 and day <= 19:
        return 'capricon'
    elif month == 1 and day >= 20 or month == 2 and day <= 19:
        return 'aqarius'
    elif month == 2 and day >= 20 or month == 3 and day <= 20:
        return 'pisces'
    # The rest of the star sign calculation here
    else:
        return ''

        
def cal_zod(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            birthdate = form.cleaned_data['birthdate']
            astro_sign = determine_star_sign(birthdate)
            return render(request,'zodiac/form2.html', {'zodiac_sign': astro_sign})
    else:
        form = PersonForm()
    return render(request, 'zodiac/form2.html', {'form': form})