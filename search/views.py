from django.contrib.auth.models import User
from django.shortcuts import render
from django_filters.views import FilterView

from search.filters import UserFilter


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})


class SearchView(FilterView):
    filterset_class = UserFilter
    template_name = 'search/user_list.html'
