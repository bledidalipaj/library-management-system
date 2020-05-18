from django.urls import path


from .views import (
    home,
    checkin_item,
    CheckoutItemView,
    get_item_checkouts,
    LibraryItemDetailView,
    ListCatalogView,
    ListPatronsView,
    PlaceHoldItemView
)

urlpatterns = [
    path('', home, name='home'),
    path('patrons/', ListPatronsView.as_view(), name='patrons'),
    path('catalog/', ListCatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>', LibraryItemDetailView.as_view(), name='item-detail'),
    path('checkin/<int:pk>', get_item_checkouts, name='item-checkouts'),
    path('checkin/', checkin_item, name='checkin'),
    path('checkout/<int:pk>', CheckoutItemView.as_view(), name='checkout'),
    path('hold/<int:pk>', PlaceHoldItemView.as_view(), name='hold'),
]
