from django.urls import path

from.views import CategoriaView, CategoriaNew, CategoriaEdit ,CategoriaDel, \
    IndicesView,IndicesNew,IndicesEdit,IndicesDel,AjustesView,AjustesNew,AjustesEdit,AjustesDel,ReporteView

urlpatterns = [
    path('categorias/',CategoriaView.as_view(),name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(),name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(),name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(),name='categoria_del'),

    path('indices/',IndicesView.as_view(),name='indices_list'),
    path('indices/new',IndicesNew.as_view(),name='indices_new'),
    path('indices/edit/<int:pk>',IndicesEdit.as_view(),name='indices_edit'),
    path('indices/delete/<int:pk>',IndicesDel.as_view(),name='indices_del'),
 
    path('ajustes/',AjustesView.as_view(),name='ajustes_list'),
    path('ajustes/new',AjustesNew.as_view(),name='ajustes_new'),
    path('ajustes/edit/<int:pk>',AjustesEdit.as_view(),name='ajustes_edit'),
    path('ajustes/delete/<int:pk>',AjustesDel.as_view(),name='ajustes_del'),


    path('reporte/', ReporteView.as_view(), name='reporte_list'),
    
]   