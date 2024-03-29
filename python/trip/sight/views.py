from django import http
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from sight import serializers
from sight.models import Sight, Comment
from utils.response import NotFoundJsonResponse


class SightListView(ListView):
	""" 景点列表 """
	# 每页放5条数据
	paginate_by = 5
	
	def get_queryset(self):
		""" 重写查询方法 """
		query = Q(is_valid=True)
		# 1. 热门景点
		is_hot = self.request.GET.get('is_hot', None)
		if is_hot:
			query = query & Q(is_hot=True)
		# 2. 精选景点
		is_top = self.request.GET.get('is_top', None)
		if is_top:
			query = query & Q(is_top=True)
		# TODO 3. 景点名称搜索
		queryset = Sight.objects.filter(query)
		return queryset
	
	def render_to_response(self, context, **response_kwargs):
		page_obj = context['page_obj']
		if page_obj is not None:
			data = serializers.SightListSerializer(page_obj).to_dict()
			return http.JsonResponse(data)
		else:
			return NotFoundJsonResponse()


# data = {
#     'meta': {
#         'total_count': page_obj.paginator.count,
#         'page_count': page_obj.paginator.num_pages,
#         'current_page': page_obj.number,
#     },
#     'objects': []
# }
# for item in page_obj.object_list:
#     data['objects'].append({
#         'id': item.id,
#         'name': item.name,
#         'main_img': item.main_img.url,
#         'score': item.score,
#         'province': item.province,
#         'min_price': item.min_price,
#         'city': item.city,
#         # TODO 评论数量暂时无法获取
#         'comment_count': 0
#     })
# return http.JsonResponse(data)


class SightDetailView(DetailView):
	"""2.2 景点详细信息"""
	
	def get_queryset(self):
		# return Sight.object.filter(is_vaild=True)
		return Sight.objects.all()
	
	def render_to_response(self, context, **response_kwargs):
		page_obj = context['object']
		if page_obj is not None:
			if not page_obj.is_valid:
				return NotFoundJsonResponse()
			data = serializers.SightDetailSerializer(page_obj).to_dict()
			return http.JsonResponse(data)
		return NotFoundJsonResponse()


class SightCommentListView(ListView):
	"""2.3 景点下的评论列表"""
	paginate_by = 10
	
	def get_queryset(self):
		# 根据景点ID查询景点
		sight_id = self.kwargs.get('pk', None)
		sight = Sight.objects.filter(pk=sight_id, is_valid=True).first()
		if sight:
			# return Common.objects.filter(pk=sight_id, sight=sight)
			return sight.comments.filter(is_valid=True)
		return Comment.objects.none()
	
	def render_to_response(self, context, **response_kwargs):
		"""重写响应的返回"""
		page_obj = context['page_obj']
		if page_obj is not None:
			data = serializers.CommentListSerializer(page_obj).to_dict()
			return http.JsonResponse(data)
		return NotFoundJsonResponse()
