from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Q, Max, Sum, Count
from accounts.models import Profile
from .models import *


def home(request):
    cards = Card.objects.filter(Q(transaction__isnull=False) | Q(sell__isnull=False))
    profile_by_coins = Profile.objects.order_by('coins')
    deck_by_cards = Deck.objects.annotate(q_count=Count('cards')).order_by('q_count')
    # todo value by card rarity rate

    context = {'cards': cards,
               'most_coins': profile_by_coins.last().user,
               'most_cards': deck_by_cards.last().user
               }
    return render(request, 'home.html', context)


@login_required
def select_card_view(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    deck = Deck.objects.get(user_id=request.user.id)
    cards = deck.cards.all()
    # print(cards)
    # remove already offered
    for card in cards:
        offers = card.offer_set.all()
        if offers:
            print(card, offers.first().owner, request.user)  # todo fix multiple owners
            if offers.first().owner == request.user:
                cards = cards.exclude(pk=card.pk)
    # print(cards)

    context = {'transaction': transaction, 'cards': cards}
    return render(request, 'select_card.html', context)


@login_required
def make_offer(request, transaction_id, card_id):
    transaction = Transaction.objects.get(id=transaction_id)
    card = Card.objects.get(id=card_id)

    print(card.id)

    Offer.objects.create(
        owner=request.user,
        card=card,
        transaction=transaction,
    )

    return redirect('home')


@login_required
def toggle_transaction(request, card_id, next_page):
    card = Card.objects.get(id=card_id)
    transaction = card.transaction_set.all()
    if transaction:
        transaction.delete()
    else:
        Transaction.objects.create(owner=request.user, card=card)
    return redirect(next_page)


class SellCreationView(LoginRequiredMixin, CreateView):
    model = Sell
    fields = ['price']
    success_url = reverse_lazy('profile')
    template_name = 'sell_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        card_id = self.kwargs.get('card_id', None)
        self.object.card = Card.objects.get(id=card_id)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@login_required
def offers_view(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    offers = transaction.offer_set.all()
    context = {'offers': offers}
    return render(request, 'offers.html', context)


@login_required
def offer_reply(request, offer_id, reply):
    offer = Offer.objects.get(id=offer_id)
    transaction = offer.transaction
    # print(offer)
    if reply:
        seller_deck = request.user.deck
        seller_card = transaction.card

        buyer_deck = offer.owner.deck
        buyer_card = offer.card

        # rm seller card and add buyer card to seller
        seller_deck.cards.remove(seller_card)
        seller_deck.cards.add(buyer_card)

        # add seller card to buyer
        seller_deck.cards.add(seller_card)

        buyer_deck.save()
        seller_deck.save()

        # delete transaction
        transaction.delete()
    else:
        offer.delete()

    return redirect('profile')


@login_required
def remove_sell(request, sell_id, next_page):
    Sell.objects.get(id=sell_id).delete()
    return redirect(next_page)


@login_required
def buy(request, sell_id):
    sell = Sell.objects.get(id=sell_id)

    # buyer - add card and remove money
    buyer = request.user
    buyer.deck.cards.add(sell.card)
    buyer.profile.coins -= sell.price
    buyer.profile.save()
    buyer.save()

    # seller - add money and remove card
    seller = sell.owner

    seller.deck.cards.remove(sell.card)
    seller.profile.coins += sell.price
    seller.profile.save()
    seller.save()

    transaction = Transaction.objects.filter(card=sell.card)

    if transaction:
        transaction.delete()

    sell.delete()

    return redirect('profile')
