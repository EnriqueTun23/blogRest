from rest_framework.serializers import (ModelSerializer, 
HyperlinkedIdentityField, SerializerMethodField)
from blog.models import post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name="detail", lookup_field="pk")
    user = SerializerMethodField()
    class Meta:
        model = post
        fields = ('id','user','title', 'content', 'publish', 'url')
    def get_user(self, obj):
        return str(obj.user.username)

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ('title', 'content', 'publish')

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = post
        fields = ('title', 'content', 'publish')

class PostDetailSerializer(ModelSerializer):
    image = SerializerMethodField()
    class Meta:
        model = post
        fields = ('id','user', 'title', 'content', 'publish', 'image')
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
        

