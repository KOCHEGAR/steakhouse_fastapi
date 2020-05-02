from starlette.status import HTTP_201_CREATED
from app.helpers import DocInfo


doc_create_order = DocInfo(
    descr='Операция создания заказа в системе. Формат времени order_time: ',
    summ='Создание заказа',
    res_descr='Заказ создан успешно',
    status_code=HTTP_201_CREATED,
).__dict__


doc_get_order_by_id = DocInfo(
    descr='Получение заказа по ID',
    summ='Получение заказа по ID',
    res_descr='Заказ',
).__dict__


allowed_fields_to_update = [
    'on_site', 'order_status'
]

doc_update_order = DocInfo(
    descr=f'Обновление заказа по ID. Обновлять можно только поля: {allowed_fields_to_update}',
    summ='Обновление заказа',
    res_descr='Заказ обновлен'
).__dict__


doc_delete_order = DocInfo(
    descr='Удаление заказа по ID',
    summ='Удаление заказа',
    res_descr='Заказ удалён'
).__dict__
