from django import forms
from django.contrib.auth.models import User, Group
import django_filters


class UserFilter(django_filters.FilterSet):
    """
    django-filters를 활용하여 User 모델 검색 필터셋을 생성한다.
    """
    # first_name = django_filters.CharFilter(lookup_expr="icontains")
    # year_joind = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    # year_joind_gt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__gt')
    # year_joind_lt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__lt')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    first_name = django_filters.CharFilter(lookup_expr='icontains')
    year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'year_joined', 'groups']
        # fields = {
        #     'username': ['exact'],
        #     'first_name': ['icontains'],
        #     'last_name': ['exact'],
        #     'date_joined': ['year', 'year__gt', 'year__lt'],
        #     'groups': ['exact']
        # }
