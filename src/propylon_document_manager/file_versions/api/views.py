from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from ..models import FileVersion
from .serializers import FileVersionSerializer, RegisterSerializer


class FileVersionViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = FileVersionSerializer
    queryset = FileVersion.objects.all()
    lookup_field = "id"


class RegisterView(generics.CreateAPIView):
    """
    API view that handles registration (creation) of new users in the system
    using the RegisterSerializer.

    The RegisterSerializer is responsible for validating the incoming user
    data and creating the new user instance. This view exposes a POST
    endpoint where clients can submit user registration payloads.
    permission_classes = [AllowAny] permits unauthenticated clients to
    access this endpoint.

    Behavior summary:
    - serializer_class: RegisterSerializer — validates input and performs
        user instance creation.
    - permission_classes: AllowAny — no authentication required to call
        this view.
    """

    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
