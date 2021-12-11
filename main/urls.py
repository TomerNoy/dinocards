from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select_card/<int:transaction_id>/', views.select_card_view, name='select_card'),
    path('make_offer/<int:transaction_id>/<int:card_id>/', views.make_offer, name='make_offer'),
    path('toggle_transaction/<int:card_id>/<str:next_page>/', views.toggle_transaction, name='toggle_transaction'),
    path('toggle_sale/<int:card_id>/', views.SellCreationView.as_view(), name='toggle_sale'),
    path('remove_sale/<int:sell_id>/<str:next_page>', views.remove_sell, name='remove_sale'),
    path('offers/<int:transaction_id>/', views.offers_view, name='offers'),
    path('offer_reply/<int:offer_id>/<int:reply>/', views.offer_reply, name='offer_reply'),
    path('buy/<int:sell_id>/', views.buy, name='buy'),
]
