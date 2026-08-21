from django import forms
from .models import Producto
from django.core.exceptions import ValidationError

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'disponible', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # Sanitización y validación individual de campo (clean_<campo>)
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise ValidationError("El nombre es demasiado corto (mínimo 3 caracteres).")
        # Sanitización: elimina espacios vacíos basura y aplica formato título
        return nombre.strip().title()

    # Validación global multicampo del formulario (clean)
    def clean(self):
        cleaned_data = super().clean()
        categoria = cleaned_data.get('categoria')
        precio = cleaned_data.get('precio')

        # Regla de negocio cruzada entre dos campos
        if categoria == 'POSTRE' and precio and precio > 500:
            raise ValidationError("Un postre no puede costar más de $500 MXN.")
        return cleaned_data