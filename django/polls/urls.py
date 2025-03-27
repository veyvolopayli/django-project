from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, ChoiceViewSet, UserProfileViewSet, index, detail, vote, results, user_profile

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/results/', results, name='results'),
    path('profile/<str:username>/', user_profile, name='user_profile'),
    path('api/', include(router.urls)),  # Подключаем маршруты API
]
