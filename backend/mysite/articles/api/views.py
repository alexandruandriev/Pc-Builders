
from .serializers import ArticleSerializer,RamSerializer
from articles.models import Article,Ram
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



# from rest_framework.generics import ( 
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     UpdateAPIView,
#     DestroyAPIView,
# )

#  class ArticleListView(ListAPIView):
#     queryset = Article.objects.all()
#      serializer_class = ArticleSerializer

#  class ArticleDetailView(RetrieveAPIView):
#    queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#  class RamListView(ListAPIView):
    #  queryset = Ram.objects.all()
    #  serializer_class = RamSerializer

#  class RamDetailView(RetrieveAPIView):
#      queryset = Ram.objects.all()
#      serializer_class = RamSerializer

#  class ArticleCreateView(CreateAPIView):
#      queryset = Article.objects.all()
#      serializer_class = ArticleSerializer

#  class ArticleDestroyView(DestroyAPIView):
#      queryset = Article.objects.all()
#      serializer_class = ArticleSerializer
    
#  class ArticleUpdateView(UpdateAPIView):
#      queryset = Article.objects.all()
# #     serializer_class = ArticleSerializer

