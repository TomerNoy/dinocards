from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    class Rarity(models.IntegerChoices):
        D = 200,
        C = 500,
        B = 800,
        A = 1000,

    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=300)
    rarity_rate = models.PositiveIntegerField(choices=Rarity.choices)
    image = models.URLField(max_length=200)

    def __str__(self):
        return f'card id:{self.id} value:{self.rarity_rate}'


class Deck(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cards = models.ManyToManyField(Card, related_name='cards', blank=True)


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Offer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class Sell(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
