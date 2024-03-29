from system.serializers import BaseImageSerializer
from utils.serializers import BaseListPageSerializer, BaseSerializer


class SightListSerializer(BaseListPageSerializer):
    """ 景点列表 """

    def get_object(self, obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'main_img': obj.main_img.url,
            'score': obj.score,
            'province': obj.province,
            'min_price': obj.min_price,
            'city': obj.city,
            # TODO 评论数量暂时无法获取
            'comment_count': 0
        }
    

class SightDetailSerializer(BaseSerializer):
    """ 景点详情 """

    def to_dict(self):
        obj = self.obj
        return {
            'id': obj.id,
            'name': obj.name,
            'desc': obj.desc,
            'img': obj.banner_img.url,
            'content': obj.content,
            'score': obj.score,
            'min_price': obj.min_price,
            'province': obj.province,
            'city': obj.city,
            'area': obj.area,
            'town': obj.town,
            # TODO 评论数量暂时无法获取
            'comment_count': 0
        }
    
class CommentListSerializer(BaseListPageSerializer):
    """评论列表"""
    def get_object(self, obj):
        user = obj.user
        images = []
        for image in obj.images.filter(is_valid=True):
            images.append(BaseImageSerializer(image).to_dict())
        return {
            'user': {
                'pk': user.pk,
                'nickname': user.nickname
            },
            'pk': obj.pk,
            'content': obj.content,
            'is_top': obj.is_top,
            'love_count': obj.love_count,
            'score': obj.score,
            'is_public': obj.is_public,
            'images': images,
            'created_at': obj.created_at.strftime('%Y-%m-%d')
        }