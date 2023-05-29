from django.urls import path

from api.v1.Category.views import CategoryView
from api.v1.Contact.views import ContactView
from api.v1.Tarif.views import TarifView
from api.v1.User.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('ctg/list/', CategoryView.as_view(), name='ctg_list'),
    path('ctg/list/<int:pk>/', CategoryView.as_view(), name='ctg_one'),

    path('contact/list/', ContactView.as_view(), name='contact_list'),
    path('contact/list/<int:pk>/', ContactView.as_view(), name='contact_one'),

    path('tarif/list/', TarifView.as_view(), name='tarif_list'),
    path('tarif/list/<int:pk>/', TarifView.as_view(), name='tarif_one'),

    path('auth/register/', RegisterView.as_view(), name="api_register"),
    path('auth/login/', LoginView.as_view(), name="api_login"),
    path('auth/loginout/', LogoutView.as_view(), name="api_logout")

]
