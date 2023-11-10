from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item_list')

class HomePageView(TemplateView):
    template_name = 'home.html'
