
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .serializers import ClinicalProjectsSerializer
from .models import ClinicalProjects

# Create your views here.
class ClinicalProjectsViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 流调项目 的列表

        retrieve:
        获取该 流调项目 的详情

        create:
        创建一个 流调项目

        update:
        整体更新该 流调项目.

        partial_update:
        部分更新该 流调项目.

        delete:
        删除该 流调项目
    """
    permission_classes = [IsOwnerOrReadOnly]
    # required_scopes = ['prj001']
    queryset = ClinicalProjects.objects.all()
    serializer_class = ClinicalProjectsSerializer
