# Cafetería Yuri — Sistema de Gestión y Comandas en Tiempo Real

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-red?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Passed_100%25-brightgreen?style=for-the-badge)

Un sistema integral de punto de venta (POS) y gestión de pedidos desarrollado con **Django** y **Django REST Framework**. La solución separa estrictamente las operaciones de negocio de la persistencia mediante una **arquitectura DAO (Data Access Object)**, e integra un flujo dinámico para la toma de comandas, monitoreo en cocina y administración del catálogo.

---

## Características Principales

* **Menú Web Interactivo:** Catálogo público con validaciones en tiempo real para la toma de pedidos.
* **Tablero de Cocina:** Pantalla interactiva con actualización automatizada para el seguimiento del estado de comandas (`PENDIENTE` ➔ `EN_PREPARACION` ➔ `ENTREGADO`).
* **API RESTful (DRF):** Endpoints JSON estandarizados para integración de clientes o aplicaciones externas.
* **Cargue Masivo CSV:** Módulo administrativo integrado en Django Admin para importar inventarios masivos.
* **Arquitectura Robustecida:** Uso de patrón **DAO** en la capa de persistencia para mantener lógica limpia de acoplamiento.
* **Garantía de Calidad:** Suite automatizada de pruebas unitarias cubriendo operaciones DAO y comunicación de endpoints.

---

##  Arquitectura del Sistema

```text
  [ Cliente Web ]          [ Cliente API / Móvil ]
         │                            │
         ▼                            ▼
  [ Views (Web) ]           [ REST ViewSets (DRF) ]
         │                            │
         └─────────────┬──────────────┘
                       │
                       ▼
              [ Capa DAO (cafedao) ]
                       │
                       ▼
               [ ORM / SQLite ]
