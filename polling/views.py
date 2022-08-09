from django.shortcuts import render
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from polling.models import Poll


class PollListView(ListView):
    '''
    Inherts built-in Django generic ListView class
    '''
    model = Poll
    template_name = 'polling/list.html'


class DetailListView(DetailView):
    '''
    Inherts built-in Django generic DetailView class
    '''
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        
        poll.save()

        context = {'object': poll}
        return render(request, 'polling/detail.html', context)
