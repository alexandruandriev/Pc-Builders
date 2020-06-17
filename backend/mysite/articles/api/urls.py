from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',ArticleViewSet, basename='article')
urlpatterns = router.urls



# from django.urls import path
# from .views
# from .views import (
#     ArticleListView,
#     ArticleDetailView,
#     ArticleCreateView,
#     ArticleDestroyView,
#     ArticleUpdateView,
#     RamDetailView,
#     RamListView,
# )

# urlpatterns = [
#     path('ram/',RamListView.as_view()),
#     path('ram/<pk>/',RamDetailView.as_view()),
#     path('',ArticleListView.as_view()),
#     path('create/',ArticleCreateView.as_view()),
#     path('<pk>/update/',ArticleUpdateView.as_view()),
#     path('<pk>/delete/',ArticleDestroyView.as_view()),
#     path('<pk>/',ArticleDetailView.as_view()),
    
# ]
