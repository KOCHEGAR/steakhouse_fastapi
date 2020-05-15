from fastapi import APIRouter

types_router = APIRouter()


@types_router.get('/types')
def get_types():
    pass


@types_router.post('/types')
def create_type():
    pass


@types_router.get('/types/{type_id}')
def get_type(type_id):
    pass


@types_router.put('/types/{type_id}')
def update_type(type_id):
    pass


@types_router.delete('/types/{type_id}')
def delete_type(type_id):
    pass
