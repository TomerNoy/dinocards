from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from forum.forms import CommentForm
from forum.models import Thread
from main.models import Transaction


@login_required
def index_view(request):
    threads = Thread.objects.all()
    context = {'threads': threads}
    return render(request, 'index.html', context)


@login_required
def thread_view(request, thread_id):
    print(thread_id)
    thread = Thread.objects.get(id=thread_id)
    print('-->', request.method)
    if request.method == 'POST':

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.thread = thread
            comment.save()
            return redirect('thread', comment.thread.id)
        return redirect('index')
    comment_form = CommentForm()
    context = {'thread': thread, 'comment_form': comment_form}
    return render(request, 'thread.html', context)


class ThreadCreationView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['subject']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteThread(LoginRequiredMixin, DeleteView):
    model = Thread
    template_name = 'delete_thread.html'
    success_url = reverse_lazy('index')
