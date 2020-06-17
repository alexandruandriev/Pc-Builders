from rest_framework import serializers
from articles.models import Article,Ram
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title','content')

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = ('title','product_code','memory_type','size','frequency','voltage')