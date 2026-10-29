
from rest_framework import serializers
from evaluation.models import Submission

class SubmissionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
        read_only_fields = [fields]

    # def get_fields(self):

    #     fields = super().get_fields()
    #     for field in fields.values():
    #         field.read_only = True

    #     return fields
