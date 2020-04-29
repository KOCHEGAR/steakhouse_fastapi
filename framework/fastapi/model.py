from framework.base_schema import AppFramework
from fastapi import FastAPI, APIRouter


GET, POST, PUT, PATCH, DELETE = 'GET', 'POST', 'PUT', 'PATCH', 'DELETE'
METHODS = [GET, POST, PUT, PATCH, DELETE]


class FastApiFramework(AppFramework):
    def __init__(self):
        self.app = FastAPI()
        self.routers = {}

    def http_get(self, *args, **kwargs):
        print('Args -> ', args, ' Kwargs -> ', kwargs)
        url = kwargs.pop('url')
        func = kwargs.pop('func')
        self.app.get(url, response_description='Хей хоп лалалей')(func)

    def http_post(self, *args, **kwargs): pass

    def http_put(self, *args, **kwargs): pass

    def http_patch(self, *args, **kwargs): pass

    def http_delete(self, *args, **kwargs): pass

    def process_request(self, ):
        pass

    def add_route(self, *args, **kwargs):
        method = kwargs.get('method')
        url = kwargs.get('url')
        view_func = kwargs.get('func')
        router_group = kwargs.get('router_group', 'default')
        router = self.routers.setdefault(router_group, APIRouter())
        http_handler = self._resolve_http_method(method, router)
        http_handler(url)(view_func)
        self.app.include_router(router=router, prefix='/api', tags=[f'{router_group} router'])

    # def _configure_api_routes(self):
    #     pass
    #
    # def _map_to_route(self):
    #     pass

    def _resolve_http_method(self, method: str, router):
        if not bool(method):
            raise RuntimeError(f'Http method MUST be specified')
        if not isinstance(method, str):
            raise RuntimeError(f'Http method MUST be string')
        method = method.upper()
        if method not in METHODS:
            raise RuntimeError(f'"{method}" does not allowed')

        # if GET == method:
        #     return self.http_get
        # if POST == method:
        #     return self.http_post
        # if PUT == method:
        #     return self.http_put
        # if PATCH == method:
        #     return self.http_patch
        # if DELETE == method:
        #     return self.http_delete

        if GET == method:
            return router.get
        if POST == method:
            return router.post
        if PUT == method:
            return router.put
        if PATCH == method:
            return router.patch
        if DELETE == method:
            return router.delete
