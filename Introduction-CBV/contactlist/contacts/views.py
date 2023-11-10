# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Contact
# from .forms import ContactForm

# def contact_list(request):
#     contacts = Contact.objects.all()
#     return render(request, 'contact_list.html', {'contacts': contacts})

# def contact_create(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#     else:
#         form = ContactForm()
#     return render(request, 'contact_form.html', {'form': form})

# def contact_edit(request, contact_id):
#     contact = get_object_or_404(Contact, pk=contact_id)
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#             return redirect('contact_list')
#     else:
#         form = ContactForm(instance=contact)
#     return render(request, 'contact_form.html', {'form': form})

# def contact_delete(request, contact_id):
#     contact = get_object_or_404(Contact, pk=contact_id)
#     contact.delete()
#     return redirect('contact_list')


from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Contact
from .forms import ContactForm

class ContactListView(View):
    template_name = 'contact_list.html'

    def get(self, request):
        contacts = Contact.objects.all()
        return render(request, self.template_name, {'contacts': contacts})

class ContactCreateView(View):
    template_name = 'contact_form.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, self.template_name, {'form': form})

class ContactEditView(View):
    template_name = 'contact_form.html'

    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        form = ContactForm(instance=contact)
        return render(request, self.template_name, {'form': form})

    def post(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
        return render(request, self.template_name, {'form': form})

class ContactDeleteView(View):
    def get(self, request, contact_id):
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.delete()
        return redirect('contact_list')
