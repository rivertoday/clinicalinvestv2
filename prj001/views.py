#from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from oauth2_provider.contrib.rest_framework import TokenHasScope
#from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, IsAuthenticatedOrTokenHasScope

from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload
from .serializers import GeneralInfoListSerializer, GeneralInfoCreateSerializer, GeneralInfoDetailSerializer
from .serializers import MenstruationSerializer, SymptomSerializer, OtherSerializer, ClinicalConclusionSerializer
from .serializers import MyUserGenInfoDetailSerializer, InvestFileUploadSerializer
from .permissions import IsOwnerOrReadOnly, CheckOperationPerm
from myusers.models import MyUser

import xlrd
import magic
import urllib.parse
from django.conf import settings

# Create your views here.
#######################################################################
# class MyUserList(generics.ListAPIView):
#     permission_classes = [TokenHasScope, IsOwnerOrReadOnly]
#     required_scopes = ['prj001']
#     queryset = MyUser.objects.all()
#     serializer_class = MyUserListSerializer

class MyUserGenInfoDetail(generics.RetrieveAPIView):
    """
        get:
        获取该用户所创建的所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, IsOwnerOrReadOnly]
    required_scopes = ['prj001']
    queryset = MyUser.objects.all()
    serializer_class = MyUserGenInfoDetailSerializer
#######################################################################
class GeneralInfoList(generics.ListAPIView):
    """
        get:
        获取所有 一般情况 列表
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name', 'nation')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$name', '$nation')

class GeneralInfoCreate(generics.CreateAPIView):
    """
        post:
        创建一个 一般情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GeneralInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    """
        get:
        获取该 一般情况 的详情

        put:
        整体更新该 一般情况.

        patch:
        部分更新该 一般情况.

        delete:
        删除该 一般情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoDetailSerializer

#######################################################################
class MenstruationViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 月经情况 的列表

        retrieve:
        获取该 月经情况 的详情

        create:
        创建一个 月经情况

        update:
        整体更新该 月经情况.

        partial_update:
        部分更新该 月经情况.

        delete:
        删除该 月经情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = Menstruation.objects.all()
    serializer_class = MenstruationSerializer

#######################################################################
class SymptomViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 全身症状 的列表

        retrieve:
        获取该 全身症状 的详情

        create:
        创建一个 全身症状

        update:
        整体更新该 全身症状.

        partial_update:
        部分更新该 全身症状.

        delete:
        删除该 全身症状
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

#######################################################################
class OtherViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 其它情况 的列表

        retrieve:
        获取该 其它情况 的详情

        create:
        创建一个 其它情况

        update:
        整体更新该 其它情况.

        partial_update:
        部分更新该 其它情况.

        delete:
        删除该 其它情况
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = Other.objects.all()
    serializer_class = OtherSerializer

#######################################################################
class ClinicalConclusionViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 临床诊断 的列表

        retrieve:
        获取该 临床诊断 的详情

        create:
        创建一个 临床诊断

        update:
        整体更新该 临床诊断.

        partial_update:
        部分更新该 临床诊断.

        delete:
        删除该 临床诊断
    """
    permission_classes = [TokenHasScope, CheckOperationPerm]
    required_scopes = ['prj001']
    queryset = ClinicalConclusion.objects.all()
    serializer_class = ClinicalConclusionSerializer


class InvestFileUploadViewSet(viewsets.ModelViewSet):
    """
        list:
        获取所有 上传文件 的列表

        retrieve:
        获取该 上传文件 的详情

        create:
        创建一个 上传文件，用于批量生成病例信息

        update:
        整体更新该 上传文件.

        partial_update:
        部分更新该 上传文件.

        delete:
        删除该 上传文件
    """
    serializer_class = InvestFileUploadSerializer
    def create(self, request, *args, **kwargs):
        # self.permission_classes = [TokenHasScope, CheckOperationPerm]
        # self.required_scopes = ['prj001']
        # self.serializer_class = InvestFileUploadSerializer
        file = request.data.dict()
        serial = InvestFileUploadSerializer(data=file)
        if not serial.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # 此时文件还是 InMemoryUploadedFile
        # 如果此时处理文件，则应形如：
        # wb = xlrd.open_workbook(file_contents=file['ivfile'].read())
        serial.save()
        # 此时文件已经变成磁盘上的实体了

        # 检查文件类型
        file_path = serial.data["ivfile"]
        tmp_str = file_path.split('/', 2)
        file_path = settings.MEDIA_ROOT + "/" + tmp_str[2]
        de_path = urllib.parse.unquote(file_path)
        print(de_path)
        checkresult = magic.from_file(de_path)
        print(checkresult)

        # if "Microsoft Excel" in checkresult:
        #     # 读取文件内容，进行处理
        #     wb = xlrd.open_workbook(de_path)
        #     table = wb.sheets()[0]
        #     row = table.nrows
        #     for i in range(1, row):
        #         col = table.row_values(i)
        #         print(col)
        # else:
        #     return Response(data="文件格式不是Excel！", status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        if "ASCII text" in checkresult:
            file_object = open('test.txt')
            try:
                file_context = file_object.read()
                print(file_context)
                # file_context是一个list，每行文本内容是list中的一个元素
                # file_context = open(file).read().splitlines()
            finally:
                file_object.close()
        else:
            return Response(data="上传文件不是文本文件！", status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        return Response(serial.data)

    def list(self, request, *args, **kwargs):
        # self.serializer_class = InvestFileUploadSerializer
        self.queryset = InvestFileUpload.objects.all()
        return super(InvestFileUploadViewSet, self).list(request)