from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Post
from .serializers import PostSerialzer


class PostListView(APIView):

    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerialzer(queryset, many=True)
        return Response(serializer.data)

