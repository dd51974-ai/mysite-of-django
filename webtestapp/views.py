from django.shortcuts import render
from .models import InfoModelForm

# Create your views here.
def info(request):
    infodata = InfoModelForm.objects.all()
    infodata2 = InfoModelForm.objects.values()
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'val2':infodata2,
    }
    return render(request, 'polls/info.html',my_dict2)
