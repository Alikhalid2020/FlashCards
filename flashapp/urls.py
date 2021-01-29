from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('add-deck', views.add_deck, name="add-deck"),
    path('deck/<deck>', views.deck, name="deck"),
    path('add-card/<deck>', views.add_card, name="add-card"),
    path('delete/<card>',views.delete_view, name="delete"),
    path('update/',views.delete_view, name="update"),
    path('edit-card/<card>', views.edit_card, name="edit-card"),
    path('search/', views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
