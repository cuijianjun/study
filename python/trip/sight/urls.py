from django.urls import path

from sight import views

urlpatterns = [
	# 景点列表接口
	path('sight/list/', views.SightListView.as_view(), name="sight_list"),
	# 2.2 景点详细信息
	path('sight/detail/<int:pk>/', views.SightDetailView.as_view(), name="sight_detail"),
	# 2.3 景点下的评论列表
	path('comment/list/<int:pk>/', views.SightCommentListView.as_view(), name="sight_comment_list"),
]
