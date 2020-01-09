from .models import Task, Sprint
from rest_framework import generics, mixins
from .serializers import TaskSerializer, SprintSerializer
from .permissions import DeveloperPermissions, SrumMasterPermissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import IsAuthenticated
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


User = get_user_model()


#Sprint
class ListCreateSprintView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated,SrumMasterPermissions]
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDeleteSprintView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [SrumMasterPermissions]
    serializer_class = SprintSerializer
    queryset = Sprint.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Task
class ListCreateTaskView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [DeveloperPermissions]
    queryset = Task.objects.all()
    serializer_class = SprintSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrieveUpdateDeleteTaskView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [DeveloperPermissions]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AuthAPIView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
            else:
                Response({'detail': 'Invalid credentials'}, status=403)
        return Response({'detail': 'Invalid qs'}, status=400)

