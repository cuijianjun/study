from django.urls import path

from sight import views

urlpatterns = [
	# 景点列表接口
	path('sight/list/', views.SightListView.as_view(), name="sight_list"),
# 2.2 景点详细信息
	path('sight/detail/<int:pk>/', views.SightDetailView.as_view(), name="sight_detail"),
]
