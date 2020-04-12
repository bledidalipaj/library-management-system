from django.urls import path


from .views import home, ListPatronsView

urlpatterns = [
    path('', home, name='home'),
    path('patrons/', ListPatronsView.as_view(), name='patrons'),
]
