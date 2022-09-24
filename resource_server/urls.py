
from django.contrib import admin
from django.urls import path

from account.views import AccountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('me/', AccountView.as_view(), name='me')
]
