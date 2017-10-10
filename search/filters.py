from django import forms
from django.contrib.auth.models import User, Group
import django_filters


class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr="icontains")
    year_joind = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    year_joind_gt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__gt')
    year_joind_lt = django_filters.NumberFilter(name='date_joined', lookup_expr='year__lt')
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'groups']
