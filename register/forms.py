from django import forms
from django.conf.urls.static import static
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['ssn','tel','voucher_id']

        widgets = {
            'ssn' : forms.TextInput(attrs={'class':'form-control'}),
            'tel' : forms.TextInput(attrs = {'class':'form-control'}),
            'voucher_id' : forms.RadioSelect()
        }

        labels = {
            'ssn':'身分證字號',
            'tel':'電話號碼',
            'voucher':'綁定'
        }
    def clean_ssn(self):
        data = self.cleaned_data['ssn']

        if len(data) != 10 :
            raise ValidationError('身分證長度必為 10')
        return data
        
    def clean_tel(self):
        data = self.cleaned_data['tel']

        if len(data) < 5 :
            raise ValidationError('電話長度不可小於5')
        return data
