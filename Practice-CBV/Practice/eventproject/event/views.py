from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'

class EventCreateView(CreateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['title', 'description', 'location', 'date', 'time']
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    template_name = 'event_form.html'
    fields = ['title', 'description', 'location', 'date', 'time']
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

