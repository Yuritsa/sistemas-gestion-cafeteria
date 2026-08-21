import time

class AuditoriaSeguridadMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Código ejecutado antes de la vista
        start_time = time.time()
        
        response = self.get_response(request)
        
        # Código ejecutado después de la vista (Inspección y Cookies seguras)
        duration = time.time() - start_time
        response['X-Process-Time'] = str(duration)
        return response