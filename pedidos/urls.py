from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/productos', views.ProductoViewSet, basename='api_productos')
router.register(r'api/pedidos', views.PedidoViewSet, basename='api_pedidos')

urlpatterns = [
    # Rutas Web (HTML)
    path('', views.menu_view, name='menu'),
    path('cocina/', views.cocina_view, name='cocina'),
    path('pedido/nuevo/', views.crear_pedido_action, name='crear_pedido'),
    path('pedido/<int:pedido_id>/estado/', views.cambiar_estado_action, name='cambiar_estado'),
    
    # Rutas API
    path('', include(router.urls)),
]