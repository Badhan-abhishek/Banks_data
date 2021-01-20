from rest_framework import serializers
from .models import Branches, Banks

# Bank model serializer
class BanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['name', 'id']

# Branch model serializer
class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state']


