# from app.views import TodoListAndCreate, TodoDetailChangeAndDelete
# '''todo_list, todo_detail_change_and_delete'''
from app.views import TodoViewSet

# from django.urls import path

# urlpatterns = [
#     # path('', todo_list),
#     path('', TodoListAndCreate.as_view()),
#     # path('<int:pk>/', todo_detail_change_and_delete),
#     path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls
