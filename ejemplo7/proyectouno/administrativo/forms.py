# forms.py
from django import forms
from django.forms import ModelForm
from administrativo.models import Modulo, Estudiante, Matricula


class EstudianteForm(ModelForm):
    class Meta:
        model  = Estudiante
        fields = ['nombre', 'apellido', 'cedula',
                  'edad', 'tipo_estudiante', 'modulos']

        widgets = {
            'nombre':  forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Nombre'}),
            'apellido':forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Apellido'}),
            'cedula':  forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Cédula'}),
            'edad':    forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Edad'}),
            'tipo_estudiante': forms.Select(attrs={'class': 'form-select'}),
            # select múltiple → misma clase
            'modulos': forms.SelectMultiple(attrs={'class': 'form-select',
                                                   'size': 6}),
        }


class ModuloForm(ModelForm):
    class Meta:
        model  = Modulo
        fields = ['nombre', 'estudiantes']
        widgets = {
            'nombre':      forms.Select(attrs={'class': 'form-select'}),
            'estudiantes': forms.SelectMultiple(attrs={'class': 'form-select',
                                                       'size': 6}),
        }


class MatriculaForm(ModelForm):
    class Meta:
        model  = Matricula
        fields = ['estudiante', 'modulo', 'comentario']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-select'}),
            'modulo':     forms.Select(attrs={'class': 'form-select'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control',
                                                'rows': 4,
                                                'placeholder': 'Comentario'}),
        }


class MatriculaEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ocultamos estudiante y módulo (no cambian)
        for campo in ('estudiante', 'modulo'):
            self.initial[campo] = getattr(self.instance, campo)
            self.fields[campo].widget = forms.widgets.HiddenInput()

    class Meta:
        model  = Matricula
        fields = ['estudiante', 'modulo', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'class': 'form-control',
                                                'rows': 4,
                                                'placeholder': 'Comentario'}),
        }
