from rest_framework import serializers

from myusers.models import MyUser
from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import InvestFileUpload

#######################################################################
class MyUserGenInfoDetailSerializer(serializers.ModelSerializer):
    # generalinfo = serializers.HyperlinkedRelatedField(many=True, view_name='generalinfo-detail', read_only=True)
    # mygi = serializers.StringRelatedField(many=True)
    mygi = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='generalinfo-detail'
    )

    class Meta:
        model = MyUser
        fields = ('url', 'email', 'user_name','mygi')

#######################################################################
class GeneralInfoListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'serial', 'name', 'age', 'height', 'weight', 'blood_type', 'nation')

class GeneralInfoCreateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'recdate', 'serial', 'hospital', 'expert', 'title', 'name', 'telephone', 'age',
                  'height', 'weight', 'blood_type', 'nation', 'career',
                  'gaokong', 'diwen', 'zaosheng', 'fushe', 'huagongyinran', 'julieyundong', 'qiyou', 'wu',
                  'address', 'entrance', 'culture', 'marriage',
                  'wuteshu', 'sushi', 'suan', 'tian', 'xian', 'xinla', 'you', 'shengleng', 'kafei', 'qita')

class GeneralInfoDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    menstruation = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='menstruation-detail'
    )

    symptom = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='symptom-detail'
    )

    other = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='other-detail'
    )

    clinicalconclusion = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='clinicalconclusion-detail'
    )

    class Meta:
        model = GeneralInfo
        fields = ('url', 'owner', 'id', 'recdate', 'serial', 'hospital', 'expert', 'title', 'name', 'telephone', 'age',
                  'height', 'weight', 'blood_type', 'nation', 'career',
                  'gaokong', 'diwen', 'zaosheng', 'fushe', 'huagongyinran', 'julieyundong', 'qiyou', 'wu',
                  'address', 'entrance', 'culture', 'marriage',
                  'wuteshu', 'sushi', 'suan', 'tian', 'xian', 'xinla', 'you', 'shengleng', 'kafei', 'qita',
                  'menstruation', 'symptom', 'other', 'clinicalconclusion')

    # def create(self, validated_data):
    #     gispecenv_data = validated_data.pop('gispecenv')
    #     gieathobbies_data = validated_data.pop('gieathobbies')
    #     gi = GeneralInfo.objects.create(**validated_data)
    #     GeneralSpecEnv.objects.create(person=gi, **gispecenv_data)
    #     GeneralEatHobbies.objects.create(person=gi, **gieathobbies_data)
    #     return gi


#######################################################################
class MenstruationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menstruation
        fields = "__all__"

#######################################################################
class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = "__all__"

#######################################################################
class OtherSerializer(serializers.ModelSerializer):
    HGBVALUE = [
        u'>110',u'91-110',u'61-90',u'30-60'
    ]
    # accessory_hgb_value = serializers.ChoiceField(choices=HGBVALUE, help_text=u'血红蛋白值')
    # accessory_hgb_value = serializers.CharField(help_text=u'血红蛋白值')
    class Meta:
        model = Other
        fields = "__all__"

#######################################################################
class ClinicalConclusionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalConclusion
        fields = "__all__"

#######################################################################
class InvestFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestFileUpload
        fields = "__all__"
