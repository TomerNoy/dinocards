from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import DeleteView, CreateView, FormView, DetailView

from main.models import Card
from manager.forms import RemoveUser, DeleteCard


@user_passes_test(lambda u: u.is_superuser)
def edit(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request, 'edit.html', context)


@user_passes_test(lambda u: u.is_superuser)
def remove_user(request):
    if request.method == 'POST':
        form = RemoveUser(request.POST)

        if form.is_valid():
            rem = get_object_or_404(User, username=form.cleaned_data['username'])
            if rem is not None:
                rem.delete()
                return redirect('edit')
    else:
        form = RemoveUser()
    context = {'form': form}
    return render(request, 'delete_user.html', context)


class CreateCardView(LoginRequiredMixin, CreateView):
    model = Card
    fields = '__all__'
    template_name = 'create_card.html'

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')


@user_passes_test(lambda u: u.is_superuser)
def delete_card(request):
    if request.method == 'POST':
        form = DeleteCard(request.POST)

        if form.is_valid():
            rem = get_object_or_404(Card, name=form.cleaned_data['name'])
            if rem is not None:
                rem.delete()
                return redirect('edit')
    else:
        form = DeleteCard()
    context = {'form': form}
    return render(request, 'delete_card.html', context)
