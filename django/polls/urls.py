from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ChoiceViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
