from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS, BasePermission
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Property, Agent, BlogPost
from .serializers import PropertySerializer, BlogPostSerializer, AgentSerializer


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PropertyViewSet(viewsets.ViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_permissions(self):
        if self.action in ['create', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, PostUserWritePermission]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list(self, request):
        serializer_class = PropertySerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        property = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PropertySerializer(property)
        return Response(serializer_class.data)

    def update(self, request, pk=None):
        property = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PropertySerializer(property)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=400)

    def destroy(self, request, pk=None):
        property = get_object_or_404(self.queryset, pk=pk)
        property.delete()
        return Response(status=204)


class PropertySearchView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']


class BlogPostView(viewsets.ViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def list_by_category(self, request):
        category_name = request.query_params.get('category')

        if category_name:
            filtered_posts = BlogPost.objects.filter(category__name=category_name)
            serializer = self.serializer_class(filtered_posts, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Category parameter is required.'}, status=400)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new blog post to the database
            return Response(serializer.data, status=201)  # Return the created data
        return Response(serializer.errors, status=400)  # Return validation errors)

    def list(self, request):
        serializer_class = BlogPostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = BlogPostSerializer(post)
        return Response(serializer_class.data)

    def update(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = BlogPostSerializer(post)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=400)


class AgentView(viewsets.ViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def list(self, request):
        serializer_class = self.serializer_class(self.queryset, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = AgentSerializer(post)
        return Response(serializer_class.data)
