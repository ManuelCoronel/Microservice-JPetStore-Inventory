from django.urls import path
from apps.inventory.api.api import category_api_view,category_detail_view, product_api_view, product_detail_view,item_api_view,item_detail_view,Count_products, Count_items,Count_categorys

urlpatterns = [
    path('category/',category_api_view,name='categoria_api'),
    path('Count_products/',Count_products.as_view(),name='Count_products'),
    path('Count_items/',Count_items.as_view(),name='Count_items'),
    path('Count_categorys/',Count_categorys.as_view(),name='Count_categorys'),
    path('category/<int:pk>/',category_detail_view,name='categoria_detail_api'),
    path('product/',product_api_view ,name='producto_api'),
    path('product/<int:pk>/',product_detail_view,name='producto_detail_api'),
    path('item/',item_api_view ,name='producto_api'),
    path('item/<int:pk>/',item_detail_view,name='producto_detail_api'),
    
  #  path('item/',ItemAPIView.as_view(),name='categoria_api'),
]
