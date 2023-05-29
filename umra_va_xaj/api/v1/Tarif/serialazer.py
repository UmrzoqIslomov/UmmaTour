from rest_framework import serializers

from umravaxajapp.models import SubCategory


class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    def create(self, validated_data):
        validated_data['ctg_id'] = validated_data.pop('ctg')
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

