# from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogapp.models import Article, Article_categories
from blogapp.models import User, Post
from .serializer import ArticleSerializer, UserSerializer, PostSerializer
from rest_framework import generics


class ArticleView(generics.RetrieveAPIView):
	queryset = Article.objects.all()

	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = ArticleSerializer(queryset, many=True)
		return Response(serializer.data)

class UserView(generics.RetrieveAPIView):
	queryset = User.objects.all()

	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)


# @api_view(['GET'])
# def getData(request):
# 	articles = Article.objects.all()
# 	serializer = ArticleSerializer(articles, many=True)
# 	return Response(serializer.data)
