from django.urls import path


from .views import home, ListCatalogView, ListPatronsView

urlpatterns = [
    path('', home, name='home'),
    path('patrons/', ListPatronsView.as_view(), name='patrons'),
    path('catalog/', ListCatalogView.as_view(), name='catalog'),
]
