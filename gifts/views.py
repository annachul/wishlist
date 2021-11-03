from django.shortcuts import redirect, render
from .models import Gifts
from .forms import GiftConformation

# Create your views here.

def index(request):
    gifts = Gifts.objects.all()
    return render(request,'gifts/index.html', {
        "gifts":gifts
    })


def giftdetail(request, id):
    try:
        if request.method == 'GET':
            giftselect = Gifts.objects.get(id=id)
            gifts = Gifts.objects.all()
            gift_conformation = GiftConformation()
            return render(request,'gifts/giftdetail.html',  {
                'gift_found': True,
                'gifttitle': giftselect.title,
                'gifdescription': giftselect.description,
                'gifturl':giftselect.url,
                'giftimage':giftselect.image,
                'form':gift_conformation,
                'taken':giftselect.taken
             })
        else:
            giftselect = Gifts.objects.get(id=id)
            gifts = Gifts.objects.all()
            giftselect.taken=True
            giftselect.save()
            return redirect('/gifts/')
    except:
        return render(request,'gifts/giftdetail.html', {'gift_found': False})