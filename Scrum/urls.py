from django.urls import path
from .views import ListCreateSprintView, RetrieveUpdateDeleteSprintView, ListCreateTaskView, RetrieveUpdateDeleteTaskView, AuthAPIView
from rest_framework_swagger.views import get_swagger_view

from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Scrum API')

urlpatterns = [
    path('listcreatesprint/', ListCreateSprintView.as_view()),
    path('reupdesprint/<int:pk>/', RetrieveUpdateDeleteSprintView.as_view()),
    path('listcreatetask/', ListCreateTaskView.as_view()),
    path('reupdetask/<int:pk>/', RetrieveUpdateDeleteTaskView.as_view()),
    path('swagger/', schema_view),
    path('docs/', include_docs_urls(title='Polls API')),
    path('login/', AuthAPIView.as_view()),
]