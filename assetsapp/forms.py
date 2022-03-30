from django import forms

from .models import Asset, Person


class AssetCreateForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = '__all__'

        widgets = {
            'person': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'area': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'name': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'serial': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'purchase_price': forms.NumberInput(
                attrs = {'class': 'form-control'}
            ),
            'purchase_date': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'leaving_date': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'current_status': forms.Select(
                attrs = {'class': 'form-select'}
            ),
        }


class AssetUpdateForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ['person', 'area', 'name', 'leaving_date', 'current_status']
        widgets = {
            'person': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'area': forms.Select(
                attrs = {'class': 'form-select'}
            ),
            'name': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'leaving_date': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'current_status': forms.Select(
                attrs = {'class': 'form-select'}
            ),
        }


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs = {'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs = {'class': 'form-control'}
            )
        }
