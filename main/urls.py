from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('add/<int:item_id>/',add_amount, name='add_amount'),
    path('delete/<int:item_id>/',delete_amount, name='delete_amount'),
    path('remove/<int:item_id>/',remove_item, name='remove_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('html/', show_html, name='show_html'), 
    path('json/', show_json, name='show_json'), 
    path('register/', register, name='register'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('html/<int:id>/', show_html_by_id, name='show_html_by_id'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
]