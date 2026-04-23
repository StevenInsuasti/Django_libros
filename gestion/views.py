from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


# ============================================================
# CRUD AUTOR - Vistas por función (Steven)
# ============================================================

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_form.html', {'form': form, 'titulo': 'Crear Autor'})


def editar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_form.html', {'form': form, 'titulo': 'Editar Autor'})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


# ============================================================
# CRUD AUTOR - Vistas genéricas (Steven)
# ============================================================

class AutorListView(ListView):
    model = Autor
    template_name = 'gestion/autor_list_generica.html'
    context_object_name = 'autores'


class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_create_generica.html'
    success_url = reverse_lazy('autor_list_generica')


class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'gestion/autor_update_generica.html'
    success_url = reverse_lazy('autor_list_generica')


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'gestion/autor_delete_generica.html'
    success_url = reverse_lazy('autor_list_generica')


# ============================================================
# CRUD LIBRO - Vistas por función (Compañero)
# ============================================================

# TODO: compañero implementa aquí las vistas por función de Libro
# def lista_libros(request): ...
# def crear_libro(request): ...
# def editar_libro(request, pk): ...
# def eliminar_libro(request, pk): ...


# ============================================================
# CRUD LIBRO - Vistas genéricas (Compañero)
# ============================================================

# TODO: compañero implementa aquí las vistas genéricas de Libro
# class LibroListView(ListView): ...
# class LibroCreateView(CreateView): ...
# class LibroUpdateView(UpdateView): ...
# class LibroDeleteView(DeleteView): ...
