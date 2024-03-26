from django.urls import path
from .views import Home, Contact, Projects

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('Contact-Us', Contact.as_view(), name='contact'),
    path('Projects', Projects.as_view(), name='projects')



]