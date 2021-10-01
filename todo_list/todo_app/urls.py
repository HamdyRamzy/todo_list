from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview.as_view(), name="api-overview"),
	path('task-list/', views.taskList.as_view(), name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail.as_view(), name="task-detail"),
	path('task-create/', views.taskCreate.as_view(), name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate.as_view(), name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete.as_view(), name="task-delete"),
]