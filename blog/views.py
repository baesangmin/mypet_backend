from rest_framework.viewsets import ModelViewSet

from modual.response import CustomResponse, DefaultResponse
from .models import Post
from .serializers import PostSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset().filter(owner=request.user)
        serializer = self.get_serializer(posts, many=True)
        return Response({"results": serializer.data})


def customRes(request):
    testData = {
        'ex': '예시 데이터'
    }
    return CustomResponse(200, '상태 메세지 변경 가능', testData)


def defaultRes(request):
    testData = {
        'ex': '예시 데이터'
    }
    return DefaultResponse(200, testData)
