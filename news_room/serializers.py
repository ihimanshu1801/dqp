from rest_framework import serializers
from . models import ParentInfograph, Infograph, InfographCategory, MasterTopics,Topics

class ParentInfographSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ParentInfograph
        fields = ('p_id', 'name', 'description', 'date_created')
        read_only_fields = ('date_created',)


class InfographSerializer(serializers.ModelSerializer):

    class Meta:
        model = Infograph
        fields = ('i_id', 'name', 'description', 'date_created','parentinfograph',"internal_url","external_url")
        read_only_fields = ('date_created',)


class TopicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = ('t_id', 'mt_id', 'topic_code', 'topic_description','mastertopics')
        read_only_fields = ('topic_description',)


# class InfographCategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = InfographCategory
#         fields = ('c_id', 'category')

# class MasterTopicsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = MasterTopics
#         fields = ( 'mt_id', 'master_topic_code', 'master_topic')

#
# class TopicsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Topics
#         fields = ('t_id', 'mt_id', 'topic_code', 'topic_description', 'master_topics')
