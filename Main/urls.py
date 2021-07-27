from django.urls import path
from .views import index, item, record

urlpatterns = [
	path('', index, name='index'),
	path('/item', item, name='item'),
	path('/record', record, name='record')
]