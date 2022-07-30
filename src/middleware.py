import threading 
request_cfg = threading.local()


class TenantRequestRouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client = request.get_host().split('.')
        if len(client)>1:
            request_cfg.cfg = client[0]
        response = self.get_response(request)
        return response

    def process_response(self, request, response):
        if hasattr( request_cfg, 'cfg' ):
            del request_cfg.cfg
        return response
