from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Producto, Pedido

class SmokeTests(TestCase):
    def setUp(self):
        """Configuración de datos iniciales para la prueba"""
        self.producto = Producto.objects.create(
            nombre="Café Americano",
            precio=45.00,
            categoria="BEBIDA",
            disponible=True
        )
        self.user = User.objects.create_superuser(
            username='admin_test',
            email='admin@test.com',
            password='password123'
        )

    def test_creacion_producto(self):
        """Verifica que el producto se guarde correctamente en la base de datos"""
        self.assertEqual(Producto.objects.count(), 1)
        self.assertEqual(self.producto.nombre, "Café Americano")

    def test_creacion_pedido(self):
        """Verifica la creación de un pedido asociado a un cliente y producto"""
        pedido = Pedido.objects.create(
            cliente_nombre="Yuri Paez",
            producto=self.producto,
            estado="PENDIENTE",
            total=45.00
        )
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(pedido.cliente_nombre, "Yuri Paez")

    def test_acceso_admin_importar_csv(self):
        """Verifica que la vista del cargue masivo responda correctamente (HTTP 200)"""
        self.client.login(username='admin_test', password='password123')
        response = self.client.get('/admin/pedidos/producto/importar-csv/')
        self.assertEqual(response.status_code, 200)