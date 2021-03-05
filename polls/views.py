# ...vote()関数
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
#from django.template import loader
from django.urls import reverse
from django.utils import timezone




#<<<<<<< HEAD
#<<<<<<< HEAD
#<<<<<<< Updated upstream
#=======
#>>>>>>> parent of a68deb9... Auto stash before rebase of "4th-commit"
from django.views import generic

from .models import Choice,Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    #追加
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
#<<<<<<< HEAD
#<<<<<<< Updated upstream
#=======

from .models import Choice,Question
#>>>>>>> parent of 8b39849... チュートリアル4の完了
#=======
#>>>>>>> parent of a68deb9... Auto stash before rebase of "4th-commit"
# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# ...vote()関数




# ...投票の結果を表示するビュー (results) を定義します。
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# ...投票の結果を表示するビュー (results) を定義します。

# ...404ショートカット　①
from django.shortcuts import get_object_or_404, render
# ...404ショートカット終わり

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})



# ...元のコード　そして書き換え
#from django.http import HttpResponse
#from django.template import loader

#from .models import Question


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
# ...元のコード　そして書き換え終わり

# ...ショートカット：render()
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# ...ショートカット：render()終わり

# ...404ショートカット2
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
# ...404ショートカット2

##def detail(request, question_id):
##    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
