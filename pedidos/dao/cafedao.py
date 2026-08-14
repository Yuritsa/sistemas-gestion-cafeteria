from typing import List, Optional
from pedidos.models import Producto, Pedido

class ProductoDAO:
    """Capa DAO para operaciones de Productos"""
    
    @staticmethod
    def obtener_todos() -> List[Producto]:
        return Producto.objects.all()

    @staticmethod
    def obtener_disponibles() -> List[Producto]:
        return Producto.objects.filter(disponible=True)

    @staticmethod
    def obtener_por_id(producto_id: int) -> Optional[Producto]:
        try:
            return Producto.objects.get(id=producto_id)
        except Producto.DoesNotExist:
            return None


class PedidoDAO:
    """Capa DAO para operaciones de Pedidos"""

    @staticmethod
    def obtener_todos() -> List[Pedido]:
        return Pedido.objects.all().order_by('-fecha')

    @staticmethod
    def crear_pedido_con_producto(cliente_nombre: str, producto_id: int) -> Optional[Pedido]:
        producto = ProductoDAO.obtener_por_id(producto_id)
        if producto:
            return Pedido.objects.create(
                cliente_nombre=cliente_nombre,
                total=producto.precio
            )
        return None

    @staticmethod
    def cambiar_estado(pedido_id: int, nuevo_estado: str) -> Optional[Pedido]:
        try:
            pedido = Pedido.objects.get(id=pedido_id)
            pedido.estado = nuevo_estado
            pedido.save()  # Ejecuta la consulta UPDATE en la BD
            return pedido
        except Pedido.DoesNotExist:
            return None