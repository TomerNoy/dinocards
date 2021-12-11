import random
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, redirect
from accounts.forms import ProfileForm, MyUserCreationForm
from accounts.models import Profile
from main.models import Deck, Card


class UserCreationView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileForm()
        return context

    def form_valid(self, form):
        profile_form = ProfileForm(self.request.POST)
        if profile_form.is_valid():
            new_user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            # create a deck
            deck = Deck.objects.create(user=profile.user)

            rarity_d_cards = Card.objects.filter(rarity_rate=200)
            rarity_d_cards = random.sample(list(rarity_d_cards), 4)

            rarity_c_cards = Card.objects.filter(rarity_rate=500)
            rarity_c_cards = random.sample(list(rarity_c_cards), 3)

            rarity_b_cards = Card.objects.filter(rarity_rate=800)
            rarity_b_cards = random.sample(list(rarity_b_cards), 2)

            rarity_a_cards = Card.objects.filter(rarity_rate=1000)
            rarity_a_cards = random.sample(list(rarity_a_cards), 1)

            cards = rarity_d_cards + rarity_c_cards + rarity_b_cards + rarity_a_cards
            for card in cards:
                deck.cards.add(card)

            # print(user, cards)

            if user:
                login(self.request, user)
                print('logged in')
            return redirect('home')
        else:
            return self.form_invalid(form)


@login_required
class UserUpdateView(UpdateView):
    form_class = ProfileForm
    model = Profile
    fields = ['username', 'password']
    template_name_suffix = '_update_form'


@login_required
def profile_update_view(request):
    deck = Deck.objects.get(user_id=request.user.id)
    cards = deck.cards.all()
    context = {'cards': cards}
    return render(request, 'registration/profile.html', context)
