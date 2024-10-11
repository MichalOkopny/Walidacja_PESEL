
from django import forms
from django.shortcuts import render
from .forms import PESELForm

def extract_data_from_pesel(pesel):
    year = int(pesel[:2]) # Określanie poszczególnych danych 
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    # Dopasowanie roku na podstawie przedziałów
    if month > 80:
        year += 1800
        month -= 80
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    # Ustalenie płci
    gender = "Mężczyzna" if int(pesel[9]) % 2 != 0 else "Kobieta"

    return f"{year}-{month:02}-{day:02}", gender

def index(request):
    if request.method == 'POST':
        form = PESELForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            birth_date, gender = extract_data_from_pesel(pesel)
            return render(request, 'result.html', {
                'valid': True,
                'birth_date': birth_date,
                'gender': gender
            })
    else:
        form = PESELForm()
    
    return render(request, 'index.html', {'form': form})
