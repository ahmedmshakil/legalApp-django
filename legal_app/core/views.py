from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from .models import LegalExpert, User, Appointment
from .serializers import LegalExpertSerializer, UserSerializer, AppointmentSerializer

class LegalExpertViewSet(viewsets.ModelViewSet):

    queryset = LegalExpert.objects.all()
    serializer_class = LegalExpertSerializer
    filter_backends = [SearchFilter]
    search_fields = ['expertise_areas']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LegalExpertListView(generics.ListAPIView):
    serializer_class = LegalExpertSerializer

    def get_queryset(self):
        queryset = LegalExpert.objects.all()
        expertise_area = self.request.query_params.get('expertise_area', None)
        if expertise_area is not None:
            queryset = queryset.filter(expertise_areas__icontains=expertise_area)
        return queryset
    
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=['post'])
    def book_appointment(self, request, pk=None):
        expert = self.get_object()
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, expert=expert)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# core/serializers.py
from rest_framework import serializers
from .models import LegalExpert, User

class LegalExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalExpert
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['expert', 'time_slot']



# In your core/urls.py, assuming you have rest_framework installed:
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LegalExpertViewSet, UserViewSet,AppointmentViewSet

router = DefaultRouter()

router.register(r'appointments', AppointmentViewSet)

router.register(r'legal_experts', LegalExpertViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

# Remember to include core.urls in your project's urls.py:
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('core.urls')),  # Assuming you want your API under /api/
# ]