from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages
# Create your views here.

class Home(TemplateView):
    template_name = 'Site/home.html'

    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            names = self.request.POST.get('names')
            phone = self.request.POST.get('phone-number')
            mail = self.request.POST.get('mail')
            about = self.request.POST.get('about')
            message = self.request.POST.get('message')
            print(names, phone, mail, about, message,'names')
            messages.info(self.request, 'We have received your message, We will get back to you ASAP')


            return redirect(self.request.get_full_path())
class Contact(TemplateView):
    template_name = 'Site/contact.html'

class Projects(TemplateView):
    template_name = 'Site/projects.html'
