from django.urls import path

from .views import ArtworkListView
from .views import SingleArtView
from .views import ArtistListView
from .views import SingleArtistListView
from .views import PeriodListView

urlpatterns = [
  path('', ArtworkListView.as_view()),
  path('<int:pk>/', SingleArtView.as_view()),
  path('artist/', ArtistListView.as_view()),
  path('artist/<int:pk>/', SingleArtistListView.as_view()),
  path('period/', PeriodListView.as_view()),
]
