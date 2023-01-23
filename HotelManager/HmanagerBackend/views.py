from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializers import *
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


class ClientReservation(TemplateView):
    template_name = "appoinment.html"
    # def get(self, request):
    #     data = RoomType.objects.
    def post(self, request):
        if request.method == 'POST':
            name = request.POST['clientname']
            checkin = request.POST['checkin']
            checkout = request.POST['checkout']
            roomtype = request.POST['roomtype']
            no_adults = request.POST['adults']
            no_children = request.POST['children']
            client_email = request.POST['email']
            client_phone = request.POST['phone']
            print(name, checkout, client_email, client_phone, roomtype)
            rt_id = RoomType.objects.get(room_type_name=roomtype)
            stat_id = Status.objects.get(id=1)
            reservation_instance = Reservation(client_name=name, client_email=client_email, client_phone=client_phone,
                                               room_type_id=rt_id, client_checkin=checkin, client_checkout=checkout,
                                               no_of_adults=no_adults, no_of_children=no_children, statusid=stat_id)
            reservation_instance.save()
            print(reservation_instance)

            return render(request, 'confirmation.html')



class ReservationResponse(TemplateView):
    template_name = "confirmation.html"


class Contact(TemplateView):
    template_name = "contact.html"


class AboutUs(TemplateView):
    template_name = "about.html"


class RoomsTemplate(TemplateView):
    template_name = "rooms.html"


class Gallery(TemplateView):
    template_name = "gallery.html"


class BlogTemplates(TemplateView):
    template_name = "news.html"


class Spa(TemplateView):
    template_name = "dinning.html"


@api_view(['POST','GET'])
def roomtype_list(request):
    '''
    lists all the available room types and adds new types
    '''
    if request.method == 'GET':
        roomtypes = RoomType.objects.all()
        roomtypes_set = RoomTypeSerializer(roomtypes, many=True)
        return Response(roomtypes_set.data)

    elif request.method == 'POST':
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def roomtype_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        roomtype = RoomType.objects.get(pk=pk)
    except RoomType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RoomTypeSerializer(roomtype)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomTypeSerializer(roomtype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        roomtype.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes({AllowAny})
def register_Users(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print('hey i reach here')
        account = serializer.save()
        account.is_active = True
        account.save()
        return Response({'sms': 'successful register'})

    data = serializer.errors

    return Response(data)


# {
#     "username":"Michael",
#     "email":"michaelcyril71@gmail.com",
#     "password":"123",
# }


@api_view(['POST'])
@permission_classes({AllowAny})
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    # if user:
    print(user)
    if user is not None:
        login(request, user)
        return Response({'message': 'login successful'})
    return Response({'sms': 'failed'})


# return render(request, 'login.html')
# {
#  "username":"widambe",
# "password":"widambe30"
#  }

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'message': 'successfull logout'})


@api_view(['POST','GET'])
def status_list(request):
    '''
    lists all the available room types and adds new types
    '''
    if request.method == 'GET':
        statuses = Status.objects.all()
        status_set = StatusSerializer(statuses, many=True)
        return Response(status_set.data)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def reservation_list(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        reservation_set = ReservationSerializer(reservations, many=True)
        return Response(reservation_set.data)
    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        room_set = RoomSerializer(rooms, many=True)
        return Response(room_set.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        booking_set = BookingSerializer(bookings, many=True)
        return Response(booking_set.data)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def suggestions_list(request):
    if request.method == 'GET':
        suggestions = Suggestions.objects.all()
        suggestions_set = SuggestionsSerializer(suggestions, many=True)
        return Response(suggestions_set.data)
    elif request.method == 'POST':
        serializer = SuggestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def blogs_list(request):
    if request.method == 'GET':
        blogposts = Blog.objects.all()
        blogpost_set = BlogSerializer(blogposts, many=True)
        return Response(blogpost_set.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



