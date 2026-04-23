from django.urls import path
from . import views

urlpatterns = [

    # ----------------------------------------------------------
    # CRUD AUTOR - Vistas por función (Steven)
    # ----------------------------------------------------------
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/editar/<int:pk>/', views.editar_autor, name='editar_autor'),
    path('autores/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),

    # ----------------------------------------------------------
    # CRUD AUTOR - Vistas genéricas (Steven)
    # ----------------------------------------------------------
    path('autores/generica/', views.AutorListView.as_view(), name='autor_list_generica'),
    path('autores/generica/crear/', views.AutorCreateView.as_view(), name='autor_create_generica'),
    path('autores/generica/editar/<int:pk>/', views.AutorUpdateView.as_view(), name='autor_update_generica'),
    path('autores/generica/eliminar/<int:pk>/', views.AutorDeleteView.as_view(), name='autor_delete_generica'),

    # ----------------------------------------------------------
    # CRUD LIBRO - Vistas por función (Sebastián)
    # ----------------------------------------------------------
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/editar/<int:pk>/', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),

    # ----------------------------------------------------------
    # CRUD LIBRO - Vistas genéricas (Sebastián)
    # ----------------------------------------------------------
    path('libros/generica/', views.LibroListView.as_view(), name='libro_list_generica'),
    path('libros/generica/crear/', views.LibroCreateView.as_view(), name='libro_create_generica'),
    path('libros/generica/editar/<int:pk>/', views.LibroUpdateView.as_view(), name='libro_update_generica'),
    path('libros/generica/eliminar/<int:pk>/', views.LibroDeleteView.as_view(), name='libro_delete_generica'),
]
