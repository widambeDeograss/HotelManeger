from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'HmanagerBackend'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutUs.as_view(), name='about'),
    path('rooms', RoomsTemplate.as_view(), name='rooms'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('blog', BlogTemplates.as_view(), name='news'),
    path('contact', Contact.as_view(), name='contact'),
    path('reservation', ClientReservation.as_view(), name='reservation'),
    path('spa', Spa.as_view(), name='spa'),
    path('reservation_response', ReservationResponse.as_view(), name='resresponce'),
    path('admin/', admin.site.urls),
    path('register', register_Users),
    path('login', login_user),
    path('logout', logout_user),
    path('roomtype',roomtype_list),
    path('roomtype_details/<int:pk>/', roomtype_detail),
    path('status', status_list),
    path('reservation_list', reservation_list),
    path('room_list', room_list),
    path('bookings', booking),
    path('suggestions', suggestions_list),
    path('blogs_list', blogs_list)
  ]
urlpatterns = format_suffix_patterns(urlpatterns)
