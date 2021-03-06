from django.urls import path


from .views import (
    home,
    checkin_item,
    get_holds,
    CheckoutItemView,
    get_item_metadata,
    get_checkout_history,
    get_item_checkouts,
    LibraryItemDetailView,
    ListCatalogView,
    ListPatronsView,
    PlaceHoldItemView,
    # patron_detail
    PatronCreateView,
    PatronDetailView,
    PatronUpdateView,
)

urlpatterns = [
    path('', home, name='home'),
    path('patrons/', ListPatronsView.as_view(), name='patrons'),
    path('patron/<int:pk>', PatronDetailView.as_view(), name='patron'),
    path('patron/<int:pk>/update', PatronUpdateView.as_view(), name='patron-update'),
    path('patron/create/', PatronCreateView.as_view(), name='patron-create'),
    path('catalog/', ListCatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>', LibraryItemDetailView.as_view(), name='item-detail'),
    path('checkin/<int:pk>', get_item_checkouts, name='item-checkouts'),
    path('checkin/', checkin_item, name='checkin'),
    path('checkout/<int:pk>', CheckoutItemView.as_view(), name='checkout'),
    path('checkout-history/<int:pk>',
         get_checkout_history, name='checkout-history'),
    path('hold/<int:pk>', PlaceHoldItemView.as_view(), name='hold'),
    path('holds/<int:pk>', get_holds, name='holds'),
    path('metadata/<int:pk>', get_item_metadata, name='metadata'),
]
