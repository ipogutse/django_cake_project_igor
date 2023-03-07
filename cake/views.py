from django.shortcuts import render
from .models import DataDescr

# Create your views here.

def index(request):
    dest = DataDescr.objects.all()
    # o1 = DataDescr()
    # o1.name = 'sponge cake'
    # o1.price = 51
    # o1.desc = 'This is a sponge cake'
    # o1.img = 'cake-1.jpg'
    
    # o2 = DataDescr()
    # o2.name = 'yellow cake'
    # o2.price = 55
    # o2.desc = 'This is a yellow'
    # o2.img = 'cake-2.jpg'

    # o3 = DataDescr()
    # o3.name = 'sugar cake'
    # o3.price = 60
    # o3.desc = 'This is a sugar cake'
    # o3.img = 'cake-3.jpg'

    # dl1 = [o1, o2, o3]
    return render(request, 'index.html',{'d1': dest})