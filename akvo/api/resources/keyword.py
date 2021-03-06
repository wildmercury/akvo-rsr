# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from tastypie.constants import ALL

from akvo.rsr.models import Keyword

from .resources import ConditionalFullResource


class KeywordResource(ConditionalFullResource):

    class Meta:
        max_limit = 10
        allowed_methods = ['get']
        queryset = Keyword.objects.all()
        resource_name = 'keyword'
        fields = [
            'id',
            'label',
        ]
        filtering = dict(
            label = ALL,
        )
