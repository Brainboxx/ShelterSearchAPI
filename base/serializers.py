from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Property, Agent, BlogPost, BlogCategory


class AgentSerializer(ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    agents = AgentSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ['name', 'image', 'house_address', 'street', 'amount', 'status',
                  'beds', 'baths', 'garages', 'area', 'description', 'agents']


class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'


class BlogPostSerializer(ModelSerializer):
    category_name = ReadOnlyField(source='category.name')

    class Meta:
        model = BlogPost
        fields = ['post_image', 'title', 'author', 'category_name', 'date_posted', 'content']

