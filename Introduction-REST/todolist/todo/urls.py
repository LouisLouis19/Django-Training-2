from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskList, TaskDetail, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/tasks/', TaskDetail.as_view(), name='task-detail'),
]



#GET /api/tasks/: List all tasks (curl http://127.0.0.1:8000/api/tasks/)
#POST /api/tasks/: Create a new task (curl -X POST http://127.0.0.1:8000/api/tasks/ -d "title=New Task" -d "description=Important task")
#GET /api/tasks/{id}/: Retrieve details of a specific task (curl http://127.0.0.1:8000/api/tasks/1/)
#PUT /api/tasks/{id}/: Update a specific task (curl -X PUT http://127.0.0.1:8000/api/tasks/1/ -d "title=Updated Task")
#DELETE /api/tasks/{id}/: Delete a specific task (curl -X DELETE http://127.0.0.1:8000/api/tasks/1/)