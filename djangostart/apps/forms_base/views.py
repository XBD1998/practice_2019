from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def index(request):
    form = ContactForm()
    return render(request, "forms_base/index.html", {"form": form})