
from fastapi import APIRouter

subtypes_router = APIRouter()


@subtypes_router.get('/subtypes')
def get_subtypes():
    pass


@subtypes_router.post('/subtypes')
def create_subtype():
    pass


@subtypes_router.get('/subtypes/{subtype_id}')
def get_subtype(subtype_id):
    pass


@subtypes_router.put('/subtypes/{subtype_id}')
def update_subtype(subtype_id):
    pass


@subtypes_router.delete('/subtypes/{subtype_id}')
def delete_subtype(subtype_id):
    pass
