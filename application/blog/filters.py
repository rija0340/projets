import django_filters
from django import forms
from .models import Article, Author

class ArticleFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )
    
    ordering = django_filters.ChoiceFilter(label='Ordering', choices = CHOICES, method='filter_by_order')
    date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'class': 'datepicker form-control form-control-sm', 'placeholder': 'YYYY-MM-DD'}))
    titre = django_filters.CharFilter(lookup_expr='icontains')
    customer = django_filters.ModelChoiceFilter(queryset=Author.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Article
        fields = ('titre','date','customer',)
        # fields = {
        #     'titre' : ['icontains'],
        #     'contenu' : ['icontains'],
           
        # }
    def filter_by_order(self,queryset, name, value):

        expression = 'id' if value == 'ascending' else '-id'
        return queryset.order_by(expression)

