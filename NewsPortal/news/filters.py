from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Author


class PostFilter(FilterSet):
    author__user = ModelChoiceFilter(
        field_name='author__user',
        queryset=Author.objects.all(),
        label='Author',
        empty_label='All'
    )
    time_in = DateFilter(lookup_expr='gt', widget=DateInput(attrs={'type': 'date'}), label='Date')

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            # 'type': ['exact'],
            # 'author__user': ['exact'],
            # 'time_in': ['gt'],
        }
