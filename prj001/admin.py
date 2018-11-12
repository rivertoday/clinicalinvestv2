from django.contrib import admin

from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion


# Register your models here.
class GeneralInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'记录日期', {'fields': ['recdate']}),
        (u'基本信息', {'fields': ['owner', 'serial', 'hospital', 'expert', 'title', 'name', 'telephone', 'age',
                              'height', 'weight', 'blood_type', 'nation', 'career']}),
        (u'特殊工作环境',
         {'fields': ['gaokong', 'diwen', 'zaosheng', 'fushe', 'huagongyinran', 'julieyundong', 'qiyou', 'wu']}),
        (None, {'fields': ['address', 'entrance', 'culture', 'marriage']}),
        (u'饮食偏好',
         {'fields': ['wuteshu', 'sushi', 'suan', 'tian', 'xian', 'xinla', 'you', 'shengleng', 'kafei', 'qita']}),
    ]
    list_display = ['serial', 'hospital', 'name', 'nation', 'age', 'height', 'weight', 'blood_type']
    ordering = ['-recdate', 'serial']
    list_filter = ['hospital', 'age', 'nation']
    search_fields = ['name', 'hospital', 'serial']
    verbose_name = u'基本信息'


#########################################################################
class MenstruationAdmin(admin.ModelAdmin):
    model = Menstruation
    fieldsets = [
        (u'信息关联', {'fields': ['owner', 'person']}),
        (u'月经情况', {'fields': ['first_time', 'cyclicity', 'normal', 'abnormal', 'cyclicity_sum',
                              'blood_cond', 'blood_color', 'blood_quality', 'blood_block', 'blood_character']}),
    ]
    list_display = ['person', 'first_time', 'cyclicity', 'normal', 'abnormal', 'cyclicity_sum',
                    'blood_cond', 'blood_color', 'blood_quality', 'blood_block', 'blood_character']
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'月经情况'


#########################################################################
class SymptomAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'信息关联', {'fields': ['owner', 'person']}),
        (u'精神症状', {'fields': ['spirit_jinglichongpei', 'spirit_jianwang', 'spirit_jingshenbujizhong',
                              'spirit_shenpifali', 'spirit_yalida', 'spirit_jiaodabiangu', 'spirit_beishangyuku']}),
        (u'情绪症状', {'fields': ['mood_zhengchang', 'mood_leguankailang', 'mood_silvguodu', 'mood_xinuwuchang',
                              'mood_fanzaoyinu', 'mood_jiaolv', 'mood_beishangyuku', 'mood_yiyu', 'mood_duosiduolv',
                              'mood_qita']}),
        (u'寒热症状', {
            'fields': ['chillfever_zhengchang', 'chillfever_weihan', 'chillfever_wuxinfanre', 'chillfever_wuhouchaore',
                       'chillfever_direbutui']}),
        (u'出汗症状', {'fields': ['sweat_zhengchang', 'sweat_duohan', 'sweat_mingxian', 'sweat_zihan', 'sweat_daohan',
                              'sweat_hongre', 'sweat_chaore']}),
        (u'语音症状', {'fields': ['sound_zhengchang', 'sound_qiduan', 'sound_xitanxi', 'sound_shaoqilanyan'
                              ]}),
        (u'面色症状', {'fields': ['face_zhengchang', 'face_danbaiwuhua', 'face_cangbai', 'face_qingbai', 'face_weihuang',
                              'face_huangzhong', 'face_chaohong', 'face_huian', 'face_baierfuzhong', 'face_baierandan',
                              'face_mianmulihei', 'face_shaohua', 'face_wuhua'
                              ]}),
        (u'心症状', {'fields': ['heart_zhengcheng', 'heart_xinfan', 'heart_xinji']}),
        (u'乳房症状',
         {'fields': ['breast_zhengchang', 'breast_biezhang', 'breast_citong', 'breast_zhangtong', 'breast_chutong']}),
        (u'胸胁症状', {'fields': ['chest_zhengchang', 'chest_zhangmen', 'chest_yintong', 'chest_citong']}),
        (u'腰膝症状', {
            'fields': ['waist_zhengchang', 'waist_suantong', 'waist_suanruan', 'waist_suanleng', 'waist_lengtong',
                       'waist_yaotongrushe']}),
        (u'腹部症状', {'fields': ['stomach_zhengchang', 'stomach_zhangtongjuan', 'stomach_xiaofuzhuizhang',
                              'stomach_xiaofubiezhang', 'stomach_xiaofulengtong', 'stomach_xiaofuzhuotong',
                              'stomach_yintongxian', 'stomach_dewentongjian', 'stomach_tongruzhenci',
                              'stomach_kongzhui']}),
        (u'头症状', {'fields': ['head_zhengchang', 'head_touyun', 'head_toutong', 'head_touchenzhong']}),

        (u'目症状', {'fields': ["eyes_zhengchang", "eyes_muxuan", "eyes_muse", "eyes_yanhua", "eyes_mutong", "eyes_muyang",
                             "eyes_chenqifz"]}),
        (u'耳症状', {'fields': ["ear_erming", "ear_erlong", "ear_tinglibq"]}),
        (u'咽喉症状',
         {'fields': ["throat_zhengchang", "throat_yangan", "throat_yantong", "throat_yanyang", "throat_yiwugan"]}),
        (u'口味症状', {'fields': ["breath_wuyiwei", "breath_kouku", "breath_kougan", "breath_koudan",
                              "breath_kouxian", "breath_koutian", "breath_kounian", "breath_danyuss"]}),
        (u'饮食症状', {'fields': ["diet_nadaishishao", "diet_shiyuws", "diet_yanshi", "diet_xireyin", "diet_xilengyin",
                              "diet_shiyujiantui", "diet_shihoufuzhang", "diet_shixinla",
                              "diet_shishengleng", "diet_kebuduoyin"]}),
        (u'睡眠症状', {'fields': ["sleep_zhengchang", "sleep_yiban", "sleep_duomengyixing", "sleep_nanyirumian",
                              "sleep_cheyebumian", "sleep_duomeng", "sleep_shishui"]}),
        (u'大便症状', {
            'fields': ["stool_sehuang", "stool_bianmi", "stool_zhixi", "stool_sgsx", "stool_xiexie",
                       "stool_tlzqxiexie", "stool_zhinian", "stool_weixiaohua"]}),
        (u'小便症状',
         {'fields': ["urine_zhengchang", "urine_duanchi", "urine_duanhuang", "urine_qingchang", "urine_yeniaopin",
                     "urine_xbpinshu", "urine_niaoji", "urine_niaotong", "urine_shaoniao", "urine_yulibujin"]}),
        (u'四肢症状', {'fields': ["limb_zhengchang", "limb_wuli", "limb_mamu", "limb_kunzhong", "limb_zhileng",
                              "limb_bingliang", "limb_szxinre", "limb_fuzhong"]}),
        (u'其它症状', {'fields': ["other_wu", "other_czjdanbai", "other_xyjiantui"]}),
        (u'舌质症状', {'fields': ["texture_danhong", "texture_danbai", "texture_pianhong", "texture_danan",
                              "texture_zian", "texture_yudian"]}),
        (u'舌苔症状', {'fields': ["coating_bai", "coating_huang", "coating_ni", "coating_bo", "coating_hou", "coating_run",
                              "coating_hua", "coating_hhouni", "coating_bairun", "coating_huangcao", "coating_wutai",
                              "coating_shaotai", "coating_huabo"]}),
        (u'舌体症状', {'fields': ["tongue_shoubo", "tongue_pangda", "tongue_bianjianhong", "tongue_youchihen",
                              "tongue_zhongyouliewen"]}),
        (u'脉象症状', {'fields': ["pulse_shi", "pulse_fu", "pulse_chen", "pulse_chi", "pulse_huan",
                              "pulse_xi", "pulse_ruo", "pulse_shu", "pulse_hua", "pulse_se", "pulse_xian",
                              "pulse_jin", "pulse_kou", "pulse_ru", "pulse_hong", "pulse_youli", "pulse_wuli"]}),
    ]
    list_display = ['person', "pulse_shi", "pulse_fu", "pulse_chen", "pulse_chi", "pulse_huan",
                    "pulse_xi", "pulse_ruo", "pulse_shu", "pulse_hua", "pulse_se", "pulse_xian",
                    "pulse_jin", "pulse_kou", "pulse_ru", "pulse_hong", "pulse_youli", "pulse_wuli"]
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'全身症状'


#########################################################################
class OtherAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'信息关联', {'fields': ['owner', 'person', ]}),
        (u'个人史', {'fields': ['person_born']}),
        (u'特殊嗜好', {'fields': ['hobbies_wu', 'hobbies_xiyan', 'hobbies_yinjiu', 'hobbies_qita']}),
        (None, {'fields': ['body_cond', 'career_labor', 'poor_blood', 'phycial_exercise']}),
        (u'减肥情况', {'fields': ['reducefat_ever', 'reducefat_yundong', 'reducefat_jieshi', 'reducefat_yaowu',
                              'reducefat_qita', 'reducefat_persist']}),
        (u'经期情况', {'fields': ['mens_yundong', 'mens_ganmao', 'mens_tongfang', 'mens_zhaoliang']}),
        (u'平素带下情况',
         {'fields': ['leucorrhea_liangshao', 'leucorrhea_liangke', 'leucorrhea_liangduo', 'leucorrhea_sehuang',
                     'leucorrhea_sebai', 'leucorrhea_selv', 'leucorrhea_zhiqingxi', 'leucorrhea_zhinianchou']}),
        (u'既往病史', {'fields': ['pasthistory_wu', 'pasthistory_yuejingbutiao', 'pasthistory_yindaoyan',
                              'pasthistory_zigongneimoyan',
                              'pasthistory_zigongneimoyiwei', 'pasthistory_zigongxianjizheng',
                              'pasthistory_penqiangyan',
                              'pasthistory_zigongjiliu', 'pasthistory_luancaonangzhong', 'pasthistory_ruxianzengsheng',
                              'pasthistory_jiazhuangxian', 'pasthistory_shengzhiyichang', 'pasthistory_naochuitiliu',
                              'pasthistory_feipang', 'pasthistory_ganyan', 'pasthistory_jiehe', 'pasthistory_qita']}),
        (u'月经不调病史',
         {'fields': ['pastmens_zhouqiwenluan', 'pastmens_liangduo', 'pastmens_zhouqisuoduan', 'pastmens_yanhou',
                     'pastmens_yanchang', 'pastmens_tingbi', 'pastmens_chuxie']}),
        (u'家族史', {
            'fields': ['womb_blood', 'ovulation', 'pastfamily_wu', 'pastfamily_gaoxueya', 'pastfamily_tangniaobing',
                       'pastfamily_xinzangbing', 'pastfamily_duonangluanchao', 'pastfamily_buxiang',
                       'pastfamily_qita']}),
        (u'孕育史', {'fields': ['pastpreg_yuncount', 'pastpreg_pougong', 'pastpreg_shunchan', 'pastpreg_yaoliu',
                             'pastpreg_renliu', 'pastpreg_ziranliu', 'pastpreg_shenghuarenshen',
                             'pastpreg_yiweirenshen', 'pastpreg_taitingyu', 'pastpreg_qinggongshu']}),
        (u'避孕措施', {
            'fields': ['prevent_jieza', 'prevent_jieyuqi', 'prevent_biyuntao', 'prevent_biyunyao',
                       'prevent_biyunyao_time', 'prevent_mafulong', 'prevent_daying', 'prevent_yousiming',
                       'prevent_zuoque', 'prevent_fufang', 'prevent_qita']}),
        (u'相关辅助检查', {
            'fields': ['accessory_hgb_value', 'accessory_quanxuexibaojishu', 'accessory_chuxuexingjibing',
                       'accessory_ningxue', 'accessory_jiazhuangxian', 'accessory_niaorenshen',
                       'accessory_penqiangchaosheng', 'accessory_jichutiwen', 'accessory_jisushuiping',
                       'accessory_guagong', 'accessory_qita']}),
    ]
    list_display = ['person', 'pasthistory_wu', 'pasthistory_yuejingbutiao', 'pasthistory_yindaoyan',
                    'pasthistory_zigongneimoyan',
                    'pasthistory_zigongneimoyiwei', 'pasthistory_zigongxianjizheng', 'pasthistory_penqiangyan',
                    'pasthistory_zigongjiliu', 'pasthistory_luancaonangzhong', 'pasthistory_ruxianzengsheng',
                    'pasthistory_jiazhuangxian', 'pasthistory_shengzhiyichang', 'pasthistory_naochuitiliu',
                    'pasthistory_feipang', 'pasthistory_ganyan', 'pasthistory_jiehe', 'pasthistory_qita']
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'其它情况'


#########################################################################
class ClinicalConclusionAdmin(admin.ModelAdmin):
    fieldsets = [
        (u'信息关联', {'fields': ['owner', 'person']}),
        (u'中医诊断', {'fields': ['benglou', 'yuejingguoduo', 'yuejingxianqi', 'jingqiyanchang', 'jingjianqichuxie']}),
        (u'分型虚证', {
            'fields': ['shenyin', 'shenyang', 'shenqi', 'piqi', 'qixuxiaxian', 'xure', 'xinpiliangxu', 'pishenyangxu',
                       'qixuekuixu', 'ganshenyinxu', 'qita_asthenic']}),
        (u'分型实证', {'fields': ['ganyuxuere', 'yangshengxuere', 'ganjingshire', 'tanreyuzu', 'tanshizuzhi', 'tanyuzuzhi',
                              'yurehujie', 'xueyu', 'qizhixueyu', 'hanningxueyu', 'qita_demonstration']}),
        (u'虚实夹杂', {'fields': ['shenxuxueyu', 'shenxuyure', 'shenxuganyu', 'qixuxueyu', 'yinxuxueyu', 'yinxuhuowang',
                              'ganyupixu', 'qita_def_ex']}),
        (u'西医诊断', {'fields': ['duonangluanchao', 'gaomirusu', 'dicuxingxianjisu', 'qita_west']}),
    ]
    list_display = ['person', 'benglou', 'yuejingguoduo', 'yuejingxianqi', 'jingqiyanchang', 'jingjianqichuxie']
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'临床诊断'


#########################################################################
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(Menstruation, MenstruationAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Other, OtherAdmin)
admin.site.register(ClinicalConclusion, ClinicalConclusionAdmin)
