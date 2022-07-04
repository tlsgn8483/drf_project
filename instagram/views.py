import genetics as genetics
from django.db.models import Sum
from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadonly
from .serializers import PostSerializer
from .models import Post
# Create your views here.

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()

# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # 유저 인증 됨을 보장받을 수 있음
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content']

    def perform_create(self, serializer):
        # 인증이 되어있다는 가정하에 Author 정의
        author = self.request.user # User or AnonymousUser
        ip = self.request.META['REMOTE_ADDR']
        point = 0
        if self.request.data['content'] != "":
            point += 1
        if self.request.data['location'] != "":
            point += 1
        if self.request.data['attachedPhotoIds'] is not None:
            point += 1

        serializer.save(author=author, ip=ip, point=point)

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    #남긴 리뷰 조회
    @action(detail=False, methods=['GET'])
    def user_select(self, request):
        qs = self.get_queryset().filter(author=request.user)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    #현재 포인트 확인
    @action(detail=False, methods=['GET'])
    def user_select_point(self, request):
        total_price = self.get_queryset().filter(author=request.user).aggregate(Sum('point'))
        return Response(total_price)

    #사용자만 업데이트 가능
    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        if self.request.user == instance.author:
            print("동일한 사용자가 아닙니다.")
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    # HTML이 없을 경우, Serializer로 넘긴다.
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        return Response({
        'post' : PostSerializer(post).data,
        })


