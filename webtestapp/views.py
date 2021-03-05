from django.shortcuts import render
from .models import InfoModelForm

# Create your views here.
#404エラーの送出
from django.shortcuts import get_object_or_404,render
from .models import InfoModelForm
# ...
def detail(request, question_id):
    try:
        question = InfoModelForm.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("InfoModelForm does not exist")
    return render(request, 'webtestapp/info.html', {'question': question})


def info(request):
    infodata = InfoModelForm.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header
    }
    return render(request, 'webtestapp/info.html',my_dict2)

from django.http import HttpResponse


#def index(request):
    #return HttpResponse("Hello, world. You're at the webtestapp index.")
