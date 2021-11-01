from django.shortcuts import render
from .models import Gifts

# Create your views here.

def index(request):
    gifts = Gifts.objects.all()
    return render(request,'gifts/index.html', {
        "gifts":gifts
    })


def giftdetail(request, id):
    try:
        giftselect = Gifts.objects.get(id=id)
        gifts = Gifts.objects.all()
        return render(request,'gifts/giftdetail.html',  {
            'gift_found': True,
            'gifttitle': giftselect.title,
            'gifdescription': giftselect.description,
            'gifturl':giftselect.url,
            'giftimage':giftselect.image
    })
    except:
        return render(request,'gifts/giftdetail.html', {'gift_found': False})