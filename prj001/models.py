# -*- coding: utf-8 -*-
from django.db import models
from datetime import date
import json
# Create your models here.
# 一、基本信息
class GeneralInfo(models.Model):
    TITLE = (
        (u'主任医师', u'主任医师'),
        (u'副主任医师', u'副主任医师'),
        (u'主治医师', u'主治医师'),
    )
    BLOOD_TYPE = (
        (u'A', u'A'),
        (u'B', u'B'),
        (u'O', u'O'),
        (u'AB', u'AB'),
    )
    NATION = (
        (u'汉族', u'汉族'),
        (u'蒙族', u'蒙古族'),
        (u'回族', u'回族'),
        (u'藏族', u'藏族'),
        (u'维吾尔族', u'维吾尔族'),
        (u'苗族', u'苗族'),
        (u'彝族', u'彝族'),
        (u'壮族', u'壮族'),
        (u'布依族', u'布依族'),
        (u'朝鲜族', u'朝鲜族'),
        (u'满族', u'满族'),
        (u'侗族', u'侗族'),
        (u'瑶族', u'瑶族'),
        (u'白族', u'白族'),
        (u'土家族', u'土家族'),
        (u'哈尼族', u'哈尼族'),
        (u'哈萨克族', u'哈萨克族'),
        (u'傣族', u'傣族'),
        (u'黎族', u'黎族'),
        (u'傈傈族', u'傈傈族'),
        (u'佤族', u'佤族'),
        (u'畲族', u'畲族'),
        (u'高山族', u'高山族'),
        (u'拉祜族', u'拉祜族'),
        (u'水族', u'水族'),
        (u'东乡族', u'东乡族'),
        (u'纳西族', u'纳西族'),
        (u'景颇族', u'景颇族'),
        (u'科尔克孜族', u'科尔克孜族'),
        (u'土族', u'土族'),
        (u'达斡尔族', u'达斡尔族'),
        (u'仫佬族', u'仫佬族'),
        (u'羌族', u'羌族'),
        (u'布朗族', u'布朗族'),
        (u'撒拉族', u'撒拉族'),
        (u'毛难族', u'毛难族'),
        (u'仡佬族', u'仡佬族'),
        (u'锡伯族', u'锡伯族'),
        (u'阿昌族', u'阿昌族'),
        (u'普米族', u'普米族'),
        (u'塔吉克族', u'塔吉克族'),
        (u'怒族', u'怒族'),
        (u'乌孜别克族', u'乌孜别克族'),
        (u'俄罗斯族', u'俄罗斯族'),
        (u'鄂温克族', u'鄂温克族'),
        (u'崩龙族', u'崩龙族'),
        (u'保安族', u'保安族'),
        (u'裕固族', u'裕固族'),
        (u'京族', u'京族'),
        (u'塔塔尔族', u'塔塔尔族'),
        (u'独龙族', u'独龙族'),
        (u'鄂伦春族', u'鄂伦春族'),
        (u'赫哲族', u'赫哲族'),
        (u'门巴族', u'门巴族'),
        (u'珞巴族', u'珞巴族'),
        (u'基诺族', u'基诺族'),
        (u'其他', u'其他'),
    )
    CAREER = (
        (u'学生', u'学生'),
        (u'个体', u'个体'),
        (u'农民', u'农民'),
        (u'军人', u'军人'),
        (u'工人', u'工人'),
        (u'财会人员', u'财会人员'),
        (u'技术人员', u'技术人员'),
        (u'服务业', u'服务业'),
        (u'科教文卫', u'科教文卫'),
        (u'行政管理', u'行政管理'),
        (u'无业', u'无业'),
        (u'其它', u'其它'),
    )
    ENTRANCE = (
        (u'门诊', u'门诊'),
        (u'病房', u'病房'),
    )
    CULTURE = (
        (u'文盲', u'文盲'),
        (u'小学及以下', u'小学及以下'),
        (u'中学或中专', u'中学或中专'),
        (u'大专', u'大专'),
        (u'本科', u'本科'),
        (u'研究生及以上', u'研究生及以上'),
    )
    MARRIAGE = (
        (u'未婚无性生活', u'未婚无性生活'),
        (u'未婚有性生活', u'未婚有性生活'),
        (u'已婚同居', u'已婚同居'),
        (u'已婚分居', u'已婚分居'),
        (u'离婚', u'离婚'),
    )
    owner = models.ForeignKey('myusers.MyUser', related_name='mygi',
                              on_delete=models.CASCADE)  # related name used in serializer for relation

    recdate = models.DateField(verbose_name=u'日期', blank=True, default=date.today)
    serial = models.CharField(verbose_name=u'问卷编码', max_length=50)
    hospital = models.CharField(verbose_name=u'医院名称', max_length=100)
    expert = models.CharField(verbose_name=u'填表专家姓名', max_length=50)
    title = models.CharField(verbose_name=u'职称', choices=TITLE, max_length=30)
    name = models.CharField(verbose_name=u'患者姓名', max_length=50)
    telephone = models.CharField(verbose_name=u'电话', max_length=20)
    age = models.IntegerField(verbose_name=u'年龄')
    height = models.IntegerField(verbose_name=u'身高cm')
    weight = models.DecimalField(verbose_name=u'体重kg', max_digits=4, decimal_places=1)
    blood_type = models.CharField(verbose_name=u'血型', choices=BLOOD_TYPE, max_length=10)
    nation = models.CharField(verbose_name=u'民族', choices=NATION, max_length=20)
    career = models.CharField(verbose_name=u'职业', choices=CAREER, max_length=20)

    # 一般情况-特殊工作环境
    # spec_env = models.ForeignKey(GeneralSpecEnv, on_delete=models.CASCADE)
    gaokong = models.BooleanField(verbose_name=u'高空', default=False)
    diwen = models.BooleanField(verbose_name=u'低温', default=False)
    zaosheng = models.BooleanField(verbose_name=u'噪声', default=False)
    fushe = models.BooleanField(verbose_name=u'辐射', default=False)
    huagongyinran = models.BooleanField(verbose_name=u'化工印染', default=False)
    julieyundong = models.BooleanField(verbose_name=u'剧烈运动', default=False)
    qiyou = models.BooleanField(verbose_name=u'汽油', default=False)
    wu = models.BooleanField(verbose_name=u'无', default=False)

    address = models.CharField(verbose_name=u'病人现住址', max_length=100)
    entrance = models.CharField(verbose_name=u'病人来源', choices=ENTRANCE, max_length=10)
    culture = models.CharField(verbose_name=u'文化程度', choices=CULTURE, max_length=30)
    marriage = models.CharField(verbose_name=u'婚姻状况', choices=MARRIAGE, max_length=30)

    # 一般情况-饮食偏好
    # eat_hobbies = models.ForeignKey(GeneralEatHobbies, on_delete=models.CASCADE)
    wuteshu = models.BooleanField(verbose_name=u'无特殊', default=False)
    sushi = models.BooleanField(verbose_name=u'素食', default=False)
    suan = models.BooleanField(verbose_name=u'酸', default=False)
    tian = models.BooleanField(verbose_name=u'甜', default=False)
    xian = models.BooleanField(verbose_name=u'咸', default=False)
    xinla = models.BooleanField(verbose_name=u'辛辣', default=False)
    you = models.BooleanField(verbose_name=u'油', default=False)
    shengleng = models.BooleanField(verbose_name=u'生冷', default=False)
    kafei = models.BooleanField(verbose_name=u'含咖啡因食物或饮品', default=False)
    qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无')

    def __int__(self):
        return self.name

    def __str__(self):
        return '%d, %s, %s' % (self.id, self.serial, self.name)

    class Meta:
        verbose_name = u'基本信息'
        ordering = ('recdate',)
        permissions = (
            ("prj001_operation", "prj001_all_permissions"),
        )


################################################################################
# 二、月经情况
class Menstruation(models.Model):
    ABNORMAL = (
        (u'或提前7天以上', u'或提前7天以上'),
        (u'或1月多次', u'或1月多次'),
        (u'或数月1次', u'或数月1次'),
    )
    CYCLICITY_SUM = (
        (u'不足2天', u'不足2天'),
        (u'3-7天', u'3-7天'),
        (u'7天以上', u'7天以上'),
        (u'有时几日即净，有时7日以上甚至达半月余不净', u'有时几日即净，有时7日以上甚至达半月余不净'),
    )
    BLOOD_COND = (
        (u'出血量中等，每次约需5-20张卫生巾', u'出血量中等，每次约需5-20张卫生巾'),
        (u'出血量多，每次多于20张卫生巾', u'出血量多，每次多于20张卫生巾'),
        (u'经量少，每次少于5张卫生巾', u'经量少，每次少于5张卫生巾'),
        (u'经量极少，几乎不用卫生巾，用护垫即可', u'经量极少，几乎不用卫生巾，用护垫即可'),
    )
    BLOOD_COLOR = (
        (u'淡红', u'淡红'),
        (u'鲜红', u'鲜红'),
        (u'暗红', u'暗红'),
        (u'紫红', u'紫红'),
        (u'紫黯', u'紫黯'),
        (u'紫黑', u'紫黑'),
        (u'褐色', u'褐色'),
        (u'其他', u'其他'),
    )
    BLOOD_QUALITY = (
        (u'正常', u'正常'),
        (u'粘稠', u'粘稠'),
        (u'清稀', u'清稀'),
    )
    BLOOD_BLOCK = (
        (u'无', u'无'),
        (u'偶有', u'偶有'),
        (u'常夹少量小血块', u'常夹少量小血块'),
        (u'常夹较大血块', u'常夹较大血块'),
    )
    BLOOD_CHARACTER = (
        (u'顺畅', u'顺畅'),
        (u'势急暴下', u'势急暴下'),
        (u'淋漓不断', u'淋漓不断'),
        (u'点滴即净', u'点滴即净'),
    )

    person = models.OneToOneField(GeneralInfo, related_name='menstruation', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='mymenstruation', on_delete=models.CASCADE)

    first_time = models.IntegerField(verbose_name=u'初潮年龄')
    cyclicity = models.BooleanField(verbose_name=u'月经周期是否规律', default=False)
    normal = models.IntegerField(verbose_name=u'月经周期尚规律的间隔天数', blank=True, null=True)
    abnormal = models.CharField(verbose_name=u'月经不规律的情况', choices=ABNORMAL, max_length=30, blank=True, null=True)
    cyclicity_sum = models.CharField(verbose_name=u'行经天数', choices=CYCLICITY_SUM, max_length=100)
    blood_cond = models.CharField(verbose_name=u'出血所需卫生巾数', choices=BLOOD_COND, max_length=100)
    blood_color = models.CharField(verbose_name=u'出血颜色', choices=BLOOD_COLOR, max_length=10)
    blood_quality = models.CharField(verbose_name=u'出血质地', choices=BLOOD_QUALITY, max_length=10)
    blood_block = models.CharField(verbose_name=u'血块', choices=BLOOD_BLOCK, max_length=30)
    blood_character = models.CharField(verbose_name=u'出血特点', choices=BLOOD_CHARACTER, max_length=20)

    class Meta:
        verbose_name = u'月经情况'

    def __str__(self):
        return "%d" % self.id


################################################################################
# 三、全身症状
class Symptom(models.Model):
    person = models.OneToOneField(GeneralInfo, related_name='symptom', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='mysymptom', on_delete=models.CASCADE)

    # 全身症状-精神
    # spirit = models.ForeignKey(SymptomSpirit, on_delete=models.CASCADE)
    spirit_jinglichongpei = models.BooleanField(verbose_name=u'精力充沛', default=False)
    spirit_jianwang = models.BooleanField(verbose_name=u'健忘', default=False)
    spirit_jingshenbujizhong = models.BooleanField(verbose_name=u'精神不集中', default=False)
    spirit_shenpifali = models.BooleanField(verbose_name=u'神疲乏力', default=False)
    spirit_yalida = models.BooleanField(verbose_name=u'学习、工作压力大', default=False)
    spirit_jiaodabiangu = models.BooleanField(verbose_name=u'个人/家庭遭遇较大变故', default=False)
    spirit_beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭', default=False)

    # 全身症状-情绪
    # mood = models.ForeignKey(SymptomMood, on_delete=models.CASCADE)
    mood_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    mood_leguankailang = models.BooleanField(verbose_name=u'乐观开朗', default=False)
    mood_silvguodu = models.BooleanField(verbose_name=u'思虑过度', default=False)
    mood_xinuwuchang = models.BooleanField(verbose_name=u'喜怒无常', default=False)
    mood_fanzaoyinu = models.BooleanField(verbose_name=u'烦躁易怒', default=False)
    mood_jiaolv = models.BooleanField(verbose_name=u'焦虑', default=False)
    mood_beishangyuku = models.BooleanField(verbose_name=u'悲伤欲哭', default=False)
    mood_yiyu = models.BooleanField(verbose_name=u'抑郁', default=False)
    mood_duosiduolv = models.BooleanField(verbose_name=u'多思多虑', default=False)
    mood_qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无')

    # 全身症状-寒热
    # chill_fever = models.ForeignKey(SymptomChillFever, on_delete=models.CASCADE)
    chillfever_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    chillfever_weihan = models.BooleanField(verbose_name=u'畏寒', default=False)
    chillfever_wuxinfanre = models.BooleanField(verbose_name=u'五心烦热', default=False)
    chillfever_wuhouchaore = models.BooleanField(verbose_name=u'午后潮热', default=False)
    chillfever_direbutui = models.BooleanField(verbose_name=u'低热不退', default=False)

#--------------------------
    # 全身症状-出汗
    sweat_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    sweat_duohan = models.BooleanField(verbose_name=u'多汗', default=False)
    sweat_mingxian = models.BooleanField(verbose_name=u'稍微活动则汗出明显', default=False)
    sweat_zihan = models.BooleanField(verbose_name=u'自汗', default=False)
    sweat_daohan = models.BooleanField(verbose_name=u'盗汗', default=False)
    sweat_hongre = models.BooleanField(verbose_name=u'烘热汗出', default=False)
    sweat_chaore = models.BooleanField(verbose_name=u'潮热汗出', default=False)

    #全身症状-语音
    sound_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    sound_qiduan = models.BooleanField(verbose_name=u'气短', default=False)
    sound_xitanxi = models.BooleanField(verbose_name=u'喜叹息', default=False)
    sound_shaoqilanyan = models.BooleanField(verbose_name=u'少气懒言', default=False)

    #全身症状-面色
    face_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    face_danbaiwuhua = models.BooleanField(verbose_name=u'淡白无华', default=False)
    face_cangbai = models.BooleanField(verbose_name=u'苍白', default=False)
    face_qingbai = models.BooleanField(verbose_name=u'清白', default=False)
    face_weihuang = models.BooleanField(verbose_name=u'萎黄', default=False)
    face_huangzhong = models.BooleanField(verbose_name=u'黄肿', default=False)
    face_chaohong = models.BooleanField(verbose_name=u'潮红', default=False)
    face_huian = models.BooleanField(verbose_name=u'晦暗', default=False)
    face_baierfuzhong = models.BooleanField(verbose_name=u'白而浮肿', default=False)
    face_baierandan = models.BooleanField(verbose_name=u'白而黯淡', default=False)
    face_mianmulihei = models.BooleanField(verbose_name=u'面目黧黑', default=False)
    face_shaohua = models.BooleanField(verbose_name=u'少华', default=False)
    face_wuhua = models.BooleanField(verbose_name=u'无华', default=False)

    # 全身症状-心
    heart_zhengcheng = models.BooleanField(verbose_name=u'正常', default=False)
    heart_xinfan = models.BooleanField(verbose_name=u'心烦', default=False)
    heart_xinji = models.BooleanField(verbose_name=u'心悸', default=False)

    # 全身症状-乳房
    breast_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    breast_biezhang = models.BooleanField(verbose_name=u'憋胀', default=False)
    breast_citong = models.BooleanField(verbose_name=u'刺痛', default=False)
    breast_zhangtong = models.BooleanField(verbose_name=u'胀痛', default=False)
    breast_chutong = models.BooleanField(verbose_name=u'触痛', default=False)

    # 全身症状-胸胁
    chest_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    chest_zhangmen = models.BooleanField(verbose_name=u'胀闷', default=False)
    chest_yintong = models.BooleanField(verbose_name=u'隐痛', default=False)
    chest_citong = models.BooleanField(verbose_name=u'刺痛', default=False)

    # 全身症状-腰膝
    waist_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    waist_suantong = models.BooleanField(verbose_name=u'酸痛', default=False)
    waist_suanruan = models.BooleanField(verbose_name=u'酸软', default=False)
    waist_suanleng = models.BooleanField(verbose_name=u'酸冷', default=False)
    waist_lengtong = models.BooleanField(verbose_name=u'冷痛', default=False)
    waist_yaotongrushe = models.BooleanField(verbose_name=u'腰痛如折', default=False)

    # 全身症状-腹部
    stomach_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    stomach_zhangtongjuan = models.BooleanField(verbose_name=u'胀痛拒按', default=False)
    stomach_xiaofuzhuizhang = models.BooleanField(verbose_name=u'小腹坠胀', default=False)
    stomach_xiaofubiezhang = models.BooleanField(verbose_name=u'小腹憋胀', default=False)
    stomach_xiaofulengtong = models.BooleanField(verbose_name=u'小腹冷痛', default=False)
    stomach_xiaofuzhuotong = models.BooleanField(verbose_name=u'小腹灼痛', default=False)
    stomach_yintongxian = models.BooleanField(verbose_name=u'隐痛喜按', default=False)
    stomach_dewentongjian = models.BooleanField(verbose_name=u'冷痛，得温痛减', default=False)
    stomach_tongruzhenci = models.BooleanField(verbose_name=u'小腹结块，痛如针刺', default=False)
    stomach_kongzhui = models.BooleanField(verbose_name=u'有空坠感', default=False)
    #---------------------------

    # 全身症状-头
    head_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    head_touyun = models.BooleanField(verbose_name=u'头晕', default=False)
    head_toutong = models.BooleanField(verbose_name=u'头痛', default=False)
    head_touchenzhong = models.BooleanField(verbose_name=u'头沉重', default=False)

    # 全身症状-目
    eyes_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    eyes_muxuan = models.BooleanField(verbose_name=u'目眩', default=False)
    eyes_muse = models.BooleanField(verbose_name=u'目涩', default=False)
    eyes_yanhua = models.BooleanField(verbose_name=u'眼花', default=False)
    eyes_mutong = models.BooleanField(verbose_name=u'目痛', default=False)
    eyes_muyang = models.BooleanField(verbose_name=u'目痒', default=False)
    eyes_chenqifz = models.BooleanField(verbose_name=u'晨起眼睑浮肿', default=False)

    # 全身症状-耳
    ear_erming = models.BooleanField(verbose_name=u'耳鸣', default=False)
    ear_erlong = models.BooleanField(verbose_name=u'耳聋', default=False)
    ear_tinglibq = models.BooleanField(verbose_name=u'听力不清，声音重复', default=False)

    # 全身症状-咽喉
    throat_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    throat_yangan = models.BooleanField(verbose_name=u'咽干', default=False)
    throat_yantong = models.BooleanField(verbose_name=u'咽痛', default=False)
    throat_yanyang = models.BooleanField(verbose_name=u'咽痒', default=False)
    throat_yiwugan = models.BooleanField(verbose_name=u'异物感', default=False)

    # 全身症状-口味
    breath_wuyiwei = models.BooleanField(verbose_name=u'口中无异味', default=False)
    breath_kouku = models.BooleanField(verbose_name=u'口苦', default=False)
    breath_kougan = models.BooleanField(verbose_name=u'口干', default=False)
    breath_koudan = models.BooleanField(verbose_name=u'口淡', default=False)
    breath_kouxian = models.BooleanField(verbose_name=u'口咸', default=False)
    breath_koutian = models.BooleanField(verbose_name=u'口甜', default=False)
    breath_kounian = models.BooleanField(verbose_name=u'口粘', default=False)
    breath_danyuss = models.BooleanField(verbose_name=u'但欲漱水不欲咽', default=False)

    # 全身症状-饮食
    diet_nadaishishao = models.BooleanField(verbose_name=u'纳呆食少', default=False)
    diet_shiyuws = models.BooleanField(verbose_name=u'食欲旺盛，多食易饥', default=False)
    diet_yanshi = models.BooleanField(verbose_name=u'厌食', default=False)
    diet_xireyin = models.BooleanField(verbose_name=u'喜热饮', default=False)
    diet_xilengyin = models.BooleanField(verbose_name=u'喜冷饮', default=False)
    diet_shiyujiantui = models.BooleanField(verbose_name=u'食欲减退，食少', default=False)
    diet_shihoufuzhang = models.BooleanField(verbose_name=u'食后腹胀', default=False)
    diet_shixinla = models.BooleanField(verbose_name=u'喜辛辣', default=False)
    diet_shishengleng = models.BooleanField(verbose_name=u'喜生冷', default=False)
    diet_kebuduoyin = models.BooleanField(verbose_name=u'渴不多饮', default=False)

    # 全身症状-睡眠
    sleep_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    sleep_yiban = models.BooleanField(verbose_name=u'一般', default=False)
    sleep_duomengyixing = models.BooleanField(verbose_name=u'多梦易醒', default=False)
    sleep_nanyirumian = models.BooleanField(verbose_name=u'难以入眠', default=False)
    sleep_cheyebumian = models.BooleanField(verbose_name=u'彻夜不眠', default=False)
    sleep_duomeng = models.BooleanField(verbose_name=u'多梦', default=False)
    sleep_shishui = models.BooleanField(verbose_name=u'嗜睡', default=False)

    # 全身症状-大便
    stool_sehuang = models.BooleanField(verbose_name=u'色黄，通畅，成形不干燥', default=False)
    stool_bianmi = models.BooleanField(verbose_name=u'便秘', default=False)
    stool_zhixi = models.BooleanField(verbose_name=u'质稀', default=False)
    stool_sgsx = models.BooleanField(verbose_name=u'时干时稀', default=False)
    stool_xiexie = models.BooleanField(verbose_name=u'泄泻', default=False)
    stool_tlzqxiexie = models.BooleanField(verbose_name=u'天亮前泄泻', default=False)
    stool_zhinian = models.BooleanField(verbose_name=u'质黏，有排不尽之感', default=False)
    stool_weixiaohua = models.BooleanField(verbose_name=u'大便中夹有未消化食物', default=False)

    # 全身症状-小便
    urine_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    urine_duanchi = models.BooleanField(verbose_name=u'短赤', default=False)
    urine_duanhuang = models.BooleanField(verbose_name=u'短黄', default=False)
    urine_qingchang = models.BooleanField(verbose_name=u'清长', default=False)
    urine_yeniaopin = models.BooleanField(verbose_name=u'夜尿频', default=False)
    urine_xbpinshu = models.BooleanField(verbose_name=u'小便频数', default=False)
    urine_niaoji = models.BooleanField(verbose_name=u'尿急', default=False)
    urine_niaotong = models.BooleanField(verbose_name=u'尿痛', default=False)
    urine_shaoniao = models.BooleanField(verbose_name=u'少尿', default=False)
    urine_yulibujin = models.BooleanField(verbose_name=u'余沥不尽', default=False)

    # 全身症状-四肢
    limb_zhengchang = models.BooleanField(verbose_name=u'正常', default=False)
    limb_wuli = models.BooleanField(verbose_name=u'无力', default=False)
    limb_mamu = models.BooleanField(verbose_name=u'麻木', default=False)
    limb_kunzhong = models.BooleanField(verbose_name=u'困重', default=False)
    limb_zhileng = models.BooleanField(verbose_name=u'肢冷', default=False)
    limb_bingliang = models.BooleanField(verbose_name=u'冰凉', default=False)
    limb_szxinre = models.BooleanField(verbose_name=u'手足心热', default=False)
    limb_fuzhong = models.BooleanField(verbose_name=u'浮肿', default=False)

    # 全身症状-其他
    other_wu = models.BooleanField(verbose_name=u'无', default=False)
    other_czjdanbai = models.BooleanField(verbose_name=u'唇爪甲淡白', default=False)
    other_xyjiantui = models.BooleanField(verbose_name=u'性欲减退', default=False)

    # 全身症状-舌质
    texture_danhong = models.BooleanField(verbose_name=u'淡红', default=False)
    texture_danbai = models.BooleanField(verbose_name=u'淡白', default=False)
    texture_pianhong = models.BooleanField(verbose_name=u'偏红', default=False)
    texture_danan = models.BooleanField(verbose_name=u'淡黯', default=False)
    texture_zian = models.BooleanField(verbose_name=u'紫黯', default=False)
    texture_yudian = models.BooleanField(verbose_name=u'有瘀点或瘀斑', default=False)

    # 全身症状-舌苔
    coating_bai = models.BooleanField(verbose_name=u'白', default=False)
    coating_huang = models.BooleanField(verbose_name=u'黄', default=False)
    coating_ni = models.BooleanField(verbose_name=u'腻', default=False)
    coating_bo = models.BooleanField(verbose_name=u'薄', default=False)
    coating_hou = models.BooleanField(verbose_name=u'厚', default=False)
    coating_run = models.BooleanField(verbose_name=u'润', default=False)
    coating_hua = models.BooleanField(verbose_name=u'滑', default=False)
    coating_hhouni = models.BooleanField(verbose_name=u'黄厚腻', default=False)
    coating_bairun = models.BooleanField(verbose_name=u'白润', default=False)
    coating_huangcao = models.BooleanField(verbose_name=u'黄糙', default=False)
    coating_wutai = models.BooleanField(verbose_name=u'无苔', default=False)
    coating_shaotai = models.BooleanField(verbose_name=u'少苔', default=False)
    coating_huabo = models.BooleanField(verbose_name=u'花剥', default=False)

    # 全身症状-舌体
    tongue_shoubo = models.BooleanField(verbose_name=u'瘦薄', default=False)
    tongue_pangda = models.BooleanField(verbose_name=u'胖大', default=False)
    tongue_bianjianhong = models.BooleanField(verbose_name=u'边尖红', default=False)
    tongue_youchihen = models.BooleanField(verbose_name=u'有齿痕', default=False)
    tongue_zhongyouliewen = models.BooleanField(verbose_name=u'中有裂纹', default=False)

    # 全身症状-脉象
    pulse_shi = models.BooleanField(verbose_name=u'实', default=False)
    pulse_fu = models.BooleanField(verbose_name=u'浮', default=False)
    pulse_chen = models.BooleanField(verbose_name=u'沉', default=False)
    pulse_chi = models.BooleanField(verbose_name=u'迟', default=False)
    pulse_huan = models.BooleanField(verbose_name=u'缓', default=False)
    pulse_xi = models.BooleanField(verbose_name=u'细', default=False)
    pulse_ruo = models.BooleanField(verbose_name=u'弱', default=False)
    pulse_shu = models.BooleanField(verbose_name=u'数', default=False)
    pulse_hua = models.BooleanField(verbose_name=u'滑', default=False)
    pulse_se = models.BooleanField(verbose_name=u'涩', default=False)
    pulse_xian = models.BooleanField(verbose_name=u'弦', default=False)
    pulse_jin = models.BooleanField(verbose_name=u'紧', default=False)
    pulse_kou = models.BooleanField(verbose_name=u'芤', default=False)
    pulse_ru = models.BooleanField(verbose_name=u'濡', default=False)
    pulse_hong = models.BooleanField(verbose_name=u'洪', default=False)
    pulse_youli = models.BooleanField(verbose_name=u'有力', default=False)
    pulse_wuli = models.BooleanField(verbose_name=u'无力', default=False)

    class Meta:
        verbose_name = u'全身症状'


################################################################################
# 四、其它
class Other(models.Model):
    BORNCOND = (
        (u'早产（28周-37周）', u'早产（28周-37周）'),
        (u'足月产', u'足月产'),
        (u'阴道分娩', u'阴道分娩'),
        (u'剖宫产', u'剖宫产'),
    )
    BODYCOND = (
        (u'好', u'好'),
        (u'一般', u'一般'),
        (u'易疲劳乏力', u'易疲劳乏力'),
    )
    CAREERLABOR = (
        (u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）', u'重体力劳动（如：搬运工、清洁工、农场工人、畜牧场工人等）'),
        (u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）', u'中体力劳动（如：家政服务人员、服务生、厨师、护士等）'),
        (u'轻体力劳动（如：教师、美容美发师、批发商、职员等）', u'中体力劳动（如：教师、美容美发师、批发商、职员等）'),
        (u'坐式的工作（如：收银员、出纳员、接线员、秘书等）', u'坐式的工作（如：收银员、出纳员、接线员、秘书等）'),
    )
    POORBLOOD = (
        (u'不详', u'不详'),
        (u'贫血', u'贫血'),
        (u'不贫血', u'不贫血'),
    )
    PHYCIALEXER = (
        (u'无', u'无'),
        (u'很少（≤1次/周）', u'很少（≤1次/周）'),
        (u'偶尔（≤3次/周）', u'偶尔（≤3次/周）'),
        (u'经常（≥4次/周）', u'经常（≥4次/周）'),
        (u'一般（少量出汗，心率≤120次/分）', u'一般（少量出汗，心率≤120次/分）'),
        (u'高强度（大汗淋漓，心率>120次/分）', u'高强度（大汗淋漓，心率>120次/分）'),
    )
    # 一级亲属（母亲、姐妹、女儿）异常子宫出血史
    WOMBBLOOD = (
        (u'无', u'无'),
        (u'有', u'有'),
        (u'不详', u'不详'),
    )
    # 是否为排卵障碍性
    OVULATION = (
        (u'是', u'是'),
        (u'否', u'否'),
        (u'不详', u'不详'),
    )

    person = models.OneToOneField(GeneralInfo, related_name='other', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='myother', on_delete=models.CASCADE)

    person_born = models.CharField(verbose_name=u'出生情况', choices=BORNCOND, max_length=30)

    # 其它 - 特殊嗜好
    # special_hobbies = models.ForeignKey(OtherSpecialHobbies, on_delete=models.CASCADE)
    hobbies_wu = models.BooleanField(verbose_name=u'无', default=False)
    hobbies_xiyan = models.BooleanField(verbose_name=u'吸烟', default=False)
    hobbies_yinjiu = models.BooleanField(verbose_name=u'饮酒', default=False)
    hobbies_qita = models.CharField(verbose_name=u'其它嗜好', max_length=50, default=u'无')

    body_cond = models.CharField(verbose_name=u'体力状况', choices=BODYCOND, max_length=20)
    career_labor = models.CharField(verbose_name=u'职业体力活动', choices=CAREERLABOR, max_length=100)
    poor_blood = models.CharField(verbose_name=u'贫血与否', choices=POORBLOOD, max_length=20)
    phycial_exercise = models.CharField(verbose_name=u'体育锻炼', choices=PHYCIALEXER, max_length=50)

    # 其它-减肥情况
    # reduce_fat = models.ForeignKey(OtherReduceFat, on_delete=models.CASCADE)
    reducefat_ever = models.BooleanField(verbose_name=u'有减肥', default=False)
    reducefat_yundong = models.BooleanField(verbose_name=u'运动减肥', default=False)
    reducefat_jieshi = models.BooleanField(verbose_name=u'节食减肥', default=False)
    reducefat_yaowu = models.BooleanField(verbose_name=u'药物减肥', default=False)
    reducefat_qita = models.CharField(verbose_name=u'其它减肥', max_length=50, default=u'无')
    reducefat_persist = models.IntegerField(verbose_name=u'减肥时长（月）', blank=True, null=True)

    # 其它-经期情况
    # mens_cond = models.ForeignKey(OtherMensCond, on_delete=models.CASCADE)
    CONDCHOICE = (
        (u'有', u'有'),
        (u'偶尔', u'偶尔'),
        (u'经常', u'经常'),
        (u'无', u'无'),
    )
    mens_yundong = models.CharField(verbose_name=u'经期运动', choices=CONDCHOICE, max_length=10)
    mens_ganmao = models.CharField(verbose_name=u'经期感冒', choices=CONDCHOICE, max_length=10)
    mens_tongfang = models.CharField(verbose_name=u'经期同房', choices=CONDCHOICE, max_length=10)
    mens_zhaoliang = models.CharField(verbose_name=u'经期着凉', choices=CONDCHOICE, max_length=10)

    # 其它-平素带下情况
    # leucorrhea = models.ForeignKey(OtherLeucorrhea, on_delete=models.CASCADE)
    leucorrhea_liangshao = models.BooleanField(verbose_name=u'带下量少', default=False)
    leucorrhea_liangke = models.BooleanField(verbose_name=u'带下量可', default=False)
    leucorrhea_liangduo = models.BooleanField(verbose_name=u'带下量多', default=False)
    leucorrhea_sehuang = models.BooleanField(verbose_name=u'带下色黄', default=False)
    leucorrhea_sebai = models.BooleanField(verbose_name=u'带下色白', default=False)
    leucorrhea_selv = models.BooleanField(verbose_name=u'带下色绿', default=False)
    leucorrhea_zhiqingxi = models.BooleanField(verbose_name=u'带下质清稀', default=False)
    leucorrhea_zhinianchou = models.BooleanField(verbose_name=u'带下质粘稠', default=False)

    # 其它-既往病史
    # past_history = models.ForeignKey(OtherPastHistory, on_delete=models.CASCADE)
    pasthistory_wu = models.BooleanField(verbose_name=u'无', default=False)
    pasthistory_yuejingbutiao = models.BooleanField(verbose_name=u'月经不调', default=False)
    pasthistory_yindaoyan = models.BooleanField(verbose_name=u'阴道炎', default=False)
    pasthistory_zigongneimoyan = models.BooleanField(verbose_name=u'子宫内膜炎', default=False)
    pasthistory_zigongneimoyiwei = models.BooleanField(verbose_name=u'子宫内膜异位症', default=False)
    pasthistory_zigongxianjizheng = models.BooleanField(verbose_name=u'子宫腺肌症', default=False)
    pasthistory_penqiangyan = models.BooleanField(verbose_name=u'盆腔炎', default=False)
    pasthistory_zigongjiliu = models.BooleanField(verbose_name=u'子宫肌瘤', default=False)
    pasthistory_luancaonangzhong = models.BooleanField(verbose_name=u'卵巢囊肿', default=False)
    pasthistory_ruxianzengsheng = models.BooleanField(verbose_name=u'乳腺增生', default=False)
    pasthistory_jiazhuangxian = models.BooleanField(verbose_name=u'甲状腺相关疾病', default=False)
    pasthistory_shengzhiyichang = models.BooleanField(verbose_name=u'生殖器官发育异常', default=False)
    pasthistory_naochuitiliu = models.BooleanField(verbose_name=u'脑垂体瘤', default=False)
    pasthistory_feipang = models.BooleanField(verbose_name=u'肥胖', default=False)
    pasthistory_ganyan = models.BooleanField(verbose_name=u'肝炎', default=False)
    pasthistory_jiehe = models.BooleanField(verbose_name=u'结核', default=False)
    pasthistory_qita = models.CharField(verbose_name=u'其它病史', max_length=50, default=u'无')

    ##############################################################################################
    # 其它-月经不调病史
    # past_mens = models.ForeignKey(OtherPastMenstruation, on_delete=models.CASCADE)
    pastmens_zhouqiwenluan = models.BooleanField(verbose_name=u'月经周期紊乱', default=False)
    pastmens_liangduo = models.BooleanField(verbose_name=u'月经量多', default=False)
    pastmens_zhouqisuoduan = models.BooleanField(verbose_name=u'月经周期缩短', default=False)
    pastmens_yanhou = models.BooleanField(verbose_name=u'月经延后', default=False)
    pastmens_yanchang = models.BooleanField(verbose_name=u'行经期延长', default=False)
    pastmens_tingbi = models.BooleanField(verbose_name=u'月经停闭', default=False)
    pastmens_chuxie = models.BooleanField(verbose_name=u'经间期出血', default=False)

    womb_blood = models.CharField(verbose_name=u'一级亲属（母亲、姐妹、女儿）异常子宫出血史', choices=WOMBBLOOD, max_length=10)
    ovulation = models.CharField(verbose_name=u'是否为排卵障碍性', choices=OVULATION, max_length=10)
    # 其它-家族史- 一级亲属（父母、兄弟姐妹、子女）其他疾病史
    # past_family = models.ForeignKey(OtherPastFamily, on_delete=models.CASCADE)
    pastfamily_wu = models.BooleanField(verbose_name=u'无', default=False)
    pastfamily_gaoxueya = models.BooleanField(verbose_name=u'高血压', default=False)
    pastfamily_tangniaobing = models.BooleanField(verbose_name=u'糖尿病', default=False)
    pastfamily_xinzangbing = models.BooleanField(verbose_name=u'心脏病', default=False)
    pastfamily_duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征', default=False)
    pastfamily_buxiang = models.BooleanField(verbose_name=u'不详', default=False)
    pastfamily_qita = models.CharField(verbose_name=u'其它', max_length=50, default=u'无')

    # 其它-孕育史
    # past_preg = models.ForeignKey(OtherPastPregnant, on_delete=models.CASCADE)
    pastpreg_yuncount = models.IntegerField(verbose_name=u'孕次总数')
    pastpreg_pougong = models.IntegerField(verbose_name=u'剖宫产次数', blank=True, null=True)
    pastpreg_shunchan = models.IntegerField(verbose_name=u'顺产次数', blank=True, null=True)
    pastpreg_yaoliu = models.IntegerField(verbose_name=u'药物流产次数', blank=True, null=True)
    pastpreg_renliu = models.IntegerField(verbose_name=u'人工流产次数', blank=True, null=True)
    pastpreg_ziranliu = models.IntegerField(verbose_name=u'自然流产次数', blank=True, null=True)
    pastpreg_shenghuarenshen = models.IntegerField(verbose_name=u'生化妊娠次数', blank=True, null=True)
    pastpreg_yiweirenshen = models.IntegerField(verbose_name=u'异位妊娠次数', blank=True, null=True)
    pastpreg_taitingyu = models.IntegerField(verbose_name=u'胎停育次数', blank=True, null=True)
    pastpreg_qinggongshu = models.IntegerField(verbose_name=u'清宫术次数', blank=True, null=True)

    # 其它-避孕措施
    # prevent_method = models.ForeignKey(OtherPrevent, on_delete=models.CASCADE)
    prevent_jieza = models.BooleanField(verbose_name=u'结扎', default=False)
    prevent_jieyuqi = models.BooleanField(verbose_name=u'宫内节育器', default=False)
    prevent_biyuntao = models.BooleanField(verbose_name=u'避孕套', default=False)
    prevent_biyunyao = models.BooleanField(verbose_name=u'口服避孕药', default=False)

    prevent_biyunyao_time = models.DecimalField(verbose_name=u'末次口服避孕药时间', max_digits=3, decimal_places=1, blank=True,
                                        null=True)  # 距离末次性行为之后多长时间服药
    prevent_mafulong = models.BooleanField(verbose_name=u'去氧孕烯炔雌片（妈富隆）', default=False)
    prevent_daying = models.BooleanField(verbose_name=u'炔雌醇环丙孕酮片（达英-35）', default=False)
    prevent_yousiming = models.BooleanField(verbose_name=u'屈螺酮炔雌醇片（优思明）', default=False)
    prevent_zuoque = models.BooleanField(verbose_name=u'左炔诺孕酮', default=False)
    prevent_fufang = models.BooleanField(verbose_name=u'复方左炔诺孕酮', default=False)
    prevent_qita = models.CharField(verbose_name=u'其它口服', max_length=100, default=u'无')

    # 其它-辅助性检查
    # accessory_check = models.ForeignKey(OtherAccessoryCheck, on_delete=models.CASCADE)
    HGBVALUE = (
        (u'>110', u'>110'),
        (u'91-110', u'91-110'),
        (u'61-90', u'61-90'),
        (u'30-60', u'30-60'),
    )
    accessory_hgb_value = models.CharField(verbose_name=u'血红蛋白值', choices=HGBVALUE, max_length=20, blank=True, null=True)
    accessory_quanxuexibaojishu = models.CharField(verbose_name=u'全血细胞计数', max_length=20, blank=True, null=True)
    accessory_chuxuexingjibing = models.CharField(verbose_name=u'出血性疾病筛查（如女性血管性血友病）', max_length=100, blank=True, null=True)
    accessory_ningxue = models.CharField(verbose_name=u'凝血功能检查', max_length=100, blank=True, null=True)
    accessory_jiazhuangxian = models.CharField(verbose_name=u'甲状腺功能检测', max_length=100, blank=True, null=True)
    accessory_niaorenshen = models.CharField(verbose_name=u'尿妊娠试验', max_length=100, blank=True, null=True)
    accessory_penqiangchaosheng = models.CharField(verbose_name=u'盆腔超声检查', max_length=100, blank=True, null=True)
    accessory_jichutiwen = models.CharField(verbose_name=u'基础体温测定', max_length=100, blank=True, null=True)
    accessory_jisushuiping = models.CharField(verbose_name=u'激素水平测定', max_length=100, blank=True, null=True)
    accessory_guagong = models.CharField(verbose_name=u'诊断性刮宫或宫腔镜下刮宫', max_length=100, blank=True, null=True)
    accessory_qita = models.CharField(verbose_name=u'其它辅助检查', max_length=100, default=u'无', blank=True, null=True)

    class Meta:
        verbose_name = u'其它情况'


################################################################################
# 五、临床诊断
class ClinicalConclusion(models.Model):
    person = models.OneToOneField(GeneralInfo, related_name='clinicalconclusion', on_delete=models.CASCADE)
    owner = models.ForeignKey('myusers.MyUser', related_name='myclinicalconclusion', on_delete=models.CASCADE)

    # 临床诊断-中医诊断
    # chinese_conclusion = models.ForeignKey(ChineseConclusion, on_delete=models.CASCADE)
    benglou = models.BooleanField(verbose_name=u'崩漏', default=False)
    yuejingguoduo = models.BooleanField(verbose_name=u'月经过多', default=False)
    yuejingxianqi = models.BooleanField(verbose_name=u'月经先期', default=False)
    jingqiyanchang = models.BooleanField(verbose_name=u'经期延长', default=False)
    jingjianqichuxie = models.BooleanField(verbose_name=u'经间期出血', default=False)

    # 临床诊断-辩证分型-虚证
    # asthenic = models.ForeignKey(Asthenic, on_delete=models.CASCADE)
    shenyin = models.BooleanField(verbose_name=u'肾阴虚证', default=False)
    shenyang = models.BooleanField(verbose_name=u'肾阳虚证', default=False)
    shenqi = models.BooleanField(verbose_name=u'肾气虚证', default=False)
    piqi = models.BooleanField(verbose_name=u'脾气虚证', default=False)
    qixuxiaxian = models.BooleanField(verbose_name=u'气虚下陷证', default=False)
    xure = models.BooleanField(verbose_name=u'虚热证', default=False)
    xinpiliangxu = models.BooleanField(verbose_name=u'心脾两虚证', default=False)
    pishenyangxu = models.BooleanField(verbose_name=u'脾肾阳虚证', default=False)
    qixuekuixu = models.BooleanField(verbose_name=u'气血亏虚症', default=False)
    ganshenyinxu = models.BooleanField(verbose_name=u'肝肾阴虚证', default=False)
    qita_asthenic = models.CharField(verbose_name=u'其它虚证', max_length=50, default=u'无')

    # 临床诊断-辩证分型-实证
    # demonstration = models.ForeignKey(Demonstration, on_delete=models.CASCADE)
    ganyuxuere = models.BooleanField(verbose_name=u'肝郁血热证', default=False)
    yangshengxuere = models.BooleanField(verbose_name=u'阳盛血热证', default=False)
    ganjingshire = models.BooleanField(verbose_name=u'肝经湿热证', default=False)
    tanreyuzu = models.BooleanField(verbose_name=u'痰热瘀阻证', default=False)
    tanshizuzhi = models.BooleanField(verbose_name=u'痰湿阻滞证', default=False)
    tanyuzuzhi = models.BooleanField(verbose_name=u'痰瘀阻滞证', default=False)
    yurehujie = models.BooleanField(verbose_name=u'瘀热互结证', default=False)
    xueyu = models.BooleanField(verbose_name=u'血瘀证', default=False)
    qizhixueyu = models.BooleanField(verbose_name=u'气滞血瘀证', default=False)
    hanningxueyu = models.BooleanField(verbose_name=u'寒凝血淤症', default=False)
    qita_demonstration = models.CharField(verbose_name=u'其它实证', max_length=50, default=u'无')

    # 临床诊断-辩证分型-虚实夹杂证
    # deficiency_excess = models.ForeignKey(DeficiencyExcess, on_delete=models.CASCADE)
    shenxuxueyu = models.BooleanField(verbose_name=u'肾虚血瘀证', default=False)
    shenxuyure = models.BooleanField(verbose_name=u'肾虚瘀热证', default=False)
    shenxuganyu = models.BooleanField(verbose_name=u'肾虚肝郁证', default=False)
    qixuxueyu = models.BooleanField(verbose_name=u'气虚血瘀证', default=False)
    yinxuxueyu = models.BooleanField(verbose_name=u'阴虚血瘀证', default=False)
    yinxuhuowang = models.BooleanField(verbose_name=u'阴虚火旺证', default=False)
    ganyupixu = models.BooleanField(verbose_name=u'肝郁脾虚证', default=False)
    qita_def_ex = models.CharField(verbose_name=u'其它虚实', max_length=50, default=u'无')

    # 临床诊断-西医诊断
    # west_conclusion = models.ForeignKey(WestConclusion, on_delete=models.CASCADE)
    duonangluanchao = models.BooleanField(verbose_name=u'多囊卵巢综合征', default=False)
    gaomirusu = models.BooleanField(verbose_name=u'高泌乳素血症', default=False)
    dicuxingxianjisu = models.BooleanField(verbose_name=u'低促行线激素疾病', default=False)
    qita_west = models.CharField(verbose_name=u'其它西医诊断', max_length=50, default=u'无')

    class Meta:
        verbose_name = u'临床诊断'

################################################################################
# 六、文件上传
class InvestFileUpload(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=10)
    ivfile = models.FileField(verbose_name=u'文件地址', upload_to='avatars/%Y-%m-%d/%H-%M', default="/avatars/default.xlsx")
    owner = models.ForeignKey('myusers.MyUser', related_name='myinvestfileupload', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'上传文件'

