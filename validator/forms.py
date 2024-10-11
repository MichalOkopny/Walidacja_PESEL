from django import forms

class PESELForm(forms.Form):
    pesel = forms.CharField(max_length=11, min_length=11, label="Numer PESEL")

    def clean_pesel(self): # Czyszczenie oraz obsługa błędów
        pesel = self.cleaned_data['pesel']
        if not pesel.isdigit() or len(pesel) != 11:
            raise forms.ValidationError("PESEL musi składać się z 11 cyfr.")
        
        if not self.is_valid_pesel(pesel):
            raise forms.ValidationError("PESEL jest nieprawidłowy.")
        
        return pesel

    def is_valid_pesel(self, pesel):
        weights = [9, 7, 3, 1, 9, 7, 3, 1, 9, 7] # mnoznik odpowiadający za sortowanie cyfr numeru PESEL
        check_sum = sum(int(pesel[i]) * weights[i] for i in range(10))
        return check_sum % 10 == int(pesel[10])
