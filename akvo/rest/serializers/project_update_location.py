# -*- coding: utf-8 -*-
"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the Akvo RSR module.
For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.
"""

from rest_framework import serializers
from akvo.rsr.models import ProjectUpdateLocation
from ..fields import Base64ImageField
from .rsr_serializer import BaseRSRSerializer


class ProjectUpdateLocationSerializer(BaseRSRSerializer):

    class Meta:
        model = ProjectUpdateLocation


class ProjectUpdateLocationExtraSerializer(ProjectUpdateLocationSerializer):

    class Meta(ProjectUpdateLocationSerializer.Meta):
        depth = 2


class MapProjectUpdateSerializer(serializers.Serializer):

    """To serialize the update field of the update map resource."""

    id = serializers.IntegerField()
    title = serializers.CharField()
    url = serializers.URLField(source='get_absolute_url')
    photo = Base64ImageField(required=False, allow_empty_file=True)
    video = serializers.CharField(required=False)


class MapProjectUpdateLocationSerializer(serializers.Serializer):

    """To serialize the update map resource."""

    id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    update = MapProjectUpdateSerializer(source='location_target')
