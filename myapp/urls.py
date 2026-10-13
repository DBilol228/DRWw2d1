from django.urls import path
from .views import *

#urlpatterns = [
#    #path('',ProductList.as_view()),
#    #path('create/',ProductCreate.as_view()),
#    #path('update/<int:pk>',ProductUpdate.as_view()),
#    #path('delete/<int:pk>',ProductDestroy.as_view()),
#    #path('detail/<int:pk>',ProductDetail.as_view())
#    
#    #path('',ProductListCreate.as_view()),
#    #path('rud/<int:pk>',ProductRUD.as_view()),
#]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products/',ProductCRUD)

urlpatterns = router.urls