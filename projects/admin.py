from django.contrib import admin
from .models import ClinicalProjects
from django.db import connection


# Register your models here.
class CLinicalProjectsAdmin(admin.ModelAdmin):
    model = ClinicalProjects
    fieldsets = [
        (u'用户关联', {'fields': [ 'relusers']}),
        (u'项目说明', {'fields': ['name', 'prj_code', 'status', 'starttime', 'endtime', 'linkurl', 'description']}),
    ]
    list_display = ('name', 'prj_code', 'status', 'starttime', 'endtime', 'linkurl')
    list_filter = ['name']
    search_fields = ['name']

    readonly_fields = ['prj_code']
    def get_readonly_fields(self, request, obj=None):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if request.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    # insert into django_content_type(id, app_label, model) values(14, 'case002', 'case002operation');
    # insert into auth_permission(id, name, content_type_id, codename) values(38, '处理排卵障碍性异常子宫出血_case002', 14, 'case002_operation');
    # def save_model(self, request, obj, form, change):
    #     sapp_label = request.POST.get('prj_code') #这个值不变，查询以这个值为准
    #     smodel = sapp_label + "operation"
    #     sname = request.POST.get('name') + '_' + sapp_label
    #     scodename = sapp_label + "_operation"
    #     cursor = connection.cursor()
    #     print(">>>Project name: %s, code: %s" % (sname, scodename))
    #
    #     if change: #更改当前权限
    #         #sqlquery1 = "select id from django_content_type where app_label=\'%s\' and model=\'%s\'" % (sapp_label, smodel)
    #         sqlquery2 = "select id from auth_permission where codename=\'%s\'" % scodename
    #         # cursor.execute(sqlquery1)
    #         # row = cursor.fetchone()
    #         # sid1 = str(row[0])
    #         # sqlupdate1 = "update django_content_type set app_label=\'%s\', model=\'%s\' where id=%s" % (sapp_label, smodel, sid1)
    #         # cursor.execute(sqlupdate1)
    #         # print(">>>sqlupdate1: %s" % (sqlupdate1))
    #         cursor.execute(sqlquery2)
    #         row = cursor.fetchone()
    #         sid2 = str(row[0])
    #         sqlupdate2 = "update auth_permission set name=\'%s\' where id=%s" % (sname, sid2)
    #         print(">>>sqlupdate2: %s" % (sqlupdate2))
    #         cursor.execute(sqlupdate2)
    #     else: #新增一个权限
    #         cursor.execute("select max(id) from django_content_type")
    #         row = cursor.fetchone()
    #         sid1 = str(row[0]+1)
    #         sqlinsert1 = "insert into django_content_type(id, app_label, model) values(%s, \'%s\', \'%s\')" % (sid1, sapp_label, smodel)
    #         cursor.execute("select max(id) from auth_permission")
    #         row = cursor.fetchone()
    #         sid2 = str(row[0]+1)
    #         sqlinsert2 = "insert into auth_permission(id, name, content_type_id, codename) values(%s, \'%s\', %s, \'%s\')" % (sid2, sname, sid1, scodename)
    #         cursor.execute(sqlinsert1)
    #         cursor.execute(sqlinsert2)
    #     super(CLinicalProjectsAdmin, self).save_model(request, obj, form, change)
    #
    # def delete_model(self, request, obj):
    #     sapp_label = request.POST.get('prj_code')#这个值不变，查询以这个值为准
    #     smodel = sapp_label + "operation"
    #     sname = request.POST.get('name') + '_' + sapp_label
    #     scodename = sapp_label + "_operation"
    #     cursor = connection.cursor()
    #     print(">>>Project name: %s, code: %s" % (sname, scodename))
    #     sqldelete1 = "delete from django_content_type where app_label=\'%s\' and model=\'%s\'" % (sapp_label, smodel)
    #     sqldelete2 = "delete from auth_permission where codename=\'%s\'" % (scodename)
    #     cursor.execute(sqldelete2)
    #     cursor.execute(sqldelete1)
    #     super(CLinicalProjectsAdmin, self).delete_model(request, obj)

admin.site.register(ClinicalProjects, CLinicalProjectsAdmin)