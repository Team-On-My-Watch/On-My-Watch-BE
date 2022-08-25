import django_filters
from .models import Recommendation


class TagFilter(django_filters.FilterSet):
    tag = django_filters.CharFilter(
        name='tag__tags',
        lookup_type='contains',
    )

    class Meta:
        model = Recommendation
        fields = ('title', 'tag')
