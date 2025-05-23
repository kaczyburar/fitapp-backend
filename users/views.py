from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Rejestracja
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Informacje o zalogowanym użytkowniku
class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_premium(request):
    user = request.user
    user.is_premium = True
    user.save()
    return Response({"message": "Dostęp premium przyznany!"})

def hello_world(request):
    return HttpResponse("<h1>Witaj świecie!</h1><p>Aplikacja Django działa na Render! 🎉</p>")
