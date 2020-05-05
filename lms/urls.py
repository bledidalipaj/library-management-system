from django.urls import path


from .views import (
    home,
    LibraryItemDetailView,
    ListCatalogView,
    ListPatronsView
)

urlpatterns = [
    path('', home, name='home'),
    path('patrons/', ListPatronsView.as_view(), name='patrons'),
    path('catalog/', ListCatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>', LibraryItemDetailView.as_view(), name='item-detail'),
]
