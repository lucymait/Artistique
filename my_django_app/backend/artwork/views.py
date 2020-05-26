# from django.shortcuts import render
# from django.views import View
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


# Import different permission classes
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.permissions import BasePermission

from .models import Art, Artist, Period
from .serializers import ArtSerializer, PopulateArtSerializer, ArtistSerializer, PeriodSerializer

class IsOwnerOrReadOnly(BasePermission):
  # object level permissions
    def has_object_permission(self, request, view, obj):
    # This code will make it work for read-only endpoints.
        if request.method in permissions.SAFE_METHODS:
            return True
    # Only gives me permission if I'm logged in as nick!
    # return str(request.user) == 'nick'

    # This will now check if the user making the request is also the owner
    # If they are the owner, they should have permission!
        return request.user == obj.user



# shorthand version for a listview:
class ArtworkListView(ListCreateAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer

    def get(self, _request):
        artworks = Art.objects.all()
        serializer = PopulateArtSerializer(artworks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArtSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_422_UNPROCESSABLE_ENTITY)


class SingleArtView(RetrieveUpdateDestroyAPIView):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, pk):
        art = Art.objects.get(pk=pk)
        # We always have to do this:
        self.check_object_permissions(request, art)
        serializer = PopulateArtSerializer(art)

        return Response(serializer.data)

    # def put(self, request, pk):
    #     art = Art.objects.get(pk=pk)
    #     serializer = ArtSerializer(art, data=request.data)
    #     if serializer.is_valid():
    #       serializer.save()
    #       return Response(serializer.data, status=HTTP_202_ACCEPTED)
    #     return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

    # def delete(self, _request, pk):
    #     art = Art.objects.get(pk=pk)
    #     art.delete()
    #     return Response(status=HTTP_204_NO_CONTENT)


class PeriodListView(ListCreateAPIView):
        queryset = Period.objects.all()
        serializer_class = PeriodSerializer

class ArtistListView(ListCreateAPIView):
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer


class SingleArtistListView(RetrieveUpdateDestroyAPIView):
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer

        def put(self, request, pk):
          artist = Artist.objects.get(pk=pk)
          serializer = ArtistSerializer(artist, data=request.data)
          if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
          return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

        def delete(self, _request, pk):
          artist = Artist.objects.get(pk=pk)
          artist.delete()
          return Response(status=HTTP_204_NO_CONTENT)