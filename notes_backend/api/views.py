from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET'])
def health(request):
    """Health check endpoint."""
    return Response({"message": "Server is up!"})

# PUBLIC_INTERFACE
class NoteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing, retrieving, creating, updating, and deleting notes.
    """
    queryset = Note.objects.all().order_by('-updated_at')
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]
