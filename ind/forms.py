from django import forms

from.models import Categoria, Indices, Ajustes


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {'descripcion':"Descripcion de la categoria",
                  "estado":"Estado"}
        widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kargs):
        super().__init__(*args,**kargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })    


class IndicesForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    ponderacion = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Valoracion'
            }
        )
    )

    class Meta:
        model = Indices
        fields = ['categoria','descripcion','estado','ponderacion']
        labels = {'descripcion':"Indice",
                  "estado":"Estado",
                  "ponderacion":"Valoracion"}
        widget={'descripcion':forms.TextInput}

    def __init__(self, *args, **kargs):
        super().__init__(*args,**kargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })                
        self.fields['categoria'].empty_label = "Seleccione Categoria"    



class AjustesForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')
    )
    
    descripcion = forms.CharField(
        max_length=100,
        required=False,
        help_text='Descripcion de el tipo de ajuste',
    )
    
    ajuste = forms.FloatField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Valoracion'
            }
        )
    )

    class Meta:
        model = Ajustes
        fields = ['categoria','descripcion','ajuste']
        
        labels = {'categoria':"categoria",
                  "descripcion":"descripcion",
                  "ajuste":"ajuste"}
  
    def __init__(self, *args, **kargs):
        super().__init__(*args,**kargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })                
        self.fields['categoria'].empty_label = "Seleccione Categoria"        