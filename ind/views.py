from msilib.schema import ListView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import F

from .models import Categoria,Indices,Ajustes
from .forms import CategoriaForm,IndicesForm,AjustesForm

class CategoriaView(LoginRequiredMixin,generic.ListView): 
    model = Categoria
    template_name = "ind/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin,generic.CreateView):
    model=Categoria
    template_name="ind/categoria_form.html"
    context_object_name ="obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("ind:categoria_list")
    login_url="bases:login"

    def form_valid(self, form):
        descripcion = self.request.POST['descripcion']  
        # Asignar al objeto Categoria 
        form.instance.descripcion = descripcion
        # Guardar objeto
        form.instance.uc = self.request.user 
        form.save()

        return super().form_valid(form)
    

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Categoria
    template_name="ind/categoria_form.html"
    context_object_name ="obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("ind:categoria_list")
    login_url="bases:login"

    def form_valid(self, form):
        descripcion = self.request.POST['descripcion']  
        # Asignar al objeto Categoria 
        form.instance.descripcion = descripcion
        # Guardar objeto en usuario modifica(um)
        form.instance.um = self.request.user.id 
        form.save()

        return super().form_valid(form)
    
class CategoriaDel(LoginRequiredMixin,generic.DeleteView):
    model=Categoria
    template_name='ind/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("ind:categoria_list")

class IndicesView(LoginRequiredMixin,generic.ListView): 
    model = Indices
    template_name = "ind/indices_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class IndicesNew(LoginRequiredMixin,generic.CreateView):
    model=Indices
    template_name="ind/indices_form.html"
    context_object_name ="obj"
    form_class=IndicesForm
    success_url=reverse_lazy("ind:indices_list")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user 

        return super().form_valid(form)
        
class IndicesEdit(LoginRequiredMixin, generic.UpdateView):
    model=Indices
    template_name="ind/indices_form.html"
    context_object_name ="obj"
    form_class=IndicesForm
    success_url=reverse_lazy("ind:indices_list")
    login_url="bases:login"

    def form_valid(self, form):
       
        form.save()
        form.instance.uc = self.request.user 
        return super().form_valid(form)
    
class IndicesDel(LoginRequiredMixin,generic.DeleteView):
    model=Indices
    template_name='ind/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("ind:indices_list")    
  

class AjustesView(LoginRequiredMixin,generic.ListView): 
    model = Ajustes
    template_name = "ind/ajustes_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class AjustesNew(LoginRequiredMixin,generic.CreateView):
    model=Ajustes
    template_name="ind/ajustes_form.html"
    context_object_name ="obj"
    form_class=AjustesForm
    success_url=reverse_lazy("ind:ajustes_list")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user 

        return super().form_valid(form)   
    
class AjustesEdit(LoginRequiredMixin, generic.UpdateView):
    model=Ajustes
    template_name="ind/ajustes_form.html"
    context_object_name ="obj"
    form_class=AjustesForm
    success_url=reverse_lazy("ind:ajustes_list")
    login_url="bases:login"

    def form_valid(self, form):
       
        form.save()
        form.instance.uc = self.request.user 
        return super().form_valid(form)
    
class AjustesDel(LoginRequiredMixin,generic.DeleteView):
    model=Ajustes
    template_name='ind/catalogos_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("ind:ajustes_list")    


class ReporteView(LoginRequiredMixin, generic.ListView):
    model = Indices
    template_name = "ind/reporte_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        categoria_id = self.request.GET.get('categoria_id', None)

        indices = Indices.objects.all()
        categorias = Categoria.objects.all()

        if categoria_id:
            ajustes = Ajustes.objects.filter(categoria=categoria_id)
        else:
            ajustes = Ajustes.objects.all()

        resultados = []

        for indice in indices:
            # Obtener el ajuste correspondiente a la categoría del índice actual
            ajuste = ajustes.filter(categoria=indice.categoria).first()

            # Verificar si hay un ajuste para la categoría del índice
            if ajuste:
                # Realizar la multiplicación y agregar el resultado a la lista de resultados
                resultado = indice.ponderacion * ajuste.ajuste
                resultados.append(resultado)

        # items_with_resultados = zip(indices, resultados)
        # context ['resultados']=items_with_resultados
        # tab = zip(indices, categorias, ajustes, resultados)
        # context['tab']=tab
                
        context ['resultados']=resultados
        context['indices'] = indices
        context['categorias'] = categorias
        context['ajustes'] = ajustes
        print (resultados)

        return context








# class ReporteView(LoginRequiredMixin, generic.ListView):

#     model = Indices
#     model1 = Ajustes.objects.filter(categoria=6).first()


#     # for obj in model1:
#     print(model1.ajuste)



#     template_name = "ind/reporte_list.html"

#     context_object_name = "obj"

#     login_url = 'bases:login'


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         indices = Indices.objects.all()
#         categorias = Categoria.objects.all()
#         ajustes = Ajustes.objects.all()

#         context['indices'] = indices
#         context['categorias'] = categorias
#         context['ajustes'] = ajustes

#         return context

