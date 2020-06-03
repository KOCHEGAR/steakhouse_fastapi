from .models import Cart
from app.utils.mongoengine_helpers import get_model_by_id_or_raise
from app.products.models import Product
from app.ordered_product.models import OrderedProduct
from app.ordered_product.schemes import OrderedProduct as OrderedProductSchema
from app.products.schemes import ProductForOrder


def create_cart(**kwargs):
    return {'id': Cart().save().id}


def get_cart(**kwargs):
    return get_model_by_id_or_raise(Cart, kwargs['id'], include_nested=True, nested_deep=2)


def add_to_cart(**kwargs):
    # kwargs = {'cart_id': cart_id, 'product_id': product_id, 'quantity': quantity}
    cart_id: str = kwargs['cart_id']
    product_id: str = kwargs['product_id']
    qty: int = kwargs['quantity']

    cart: Cart = get_model_by_id_or_raise(Cart, cart_id, include_nested=True, nested_deep=2)
    product: Product = get_model_by_id_or_raise(Product, product_id)

    # if not cart.is_product_in_cart(product_id):
    #     product_dict = dict(ProductForOrder.from_orm(product))
    #     ordered_product: OrderedProduct = OrderedProduct(amount_total=qty, product=product_dict).save()
    #     cart.add_new_ordered_product(ordered_product)
    #     print(dict(OrderedProductSchema.from_orm(ordered_product)))
    # else:
    #     pass
        # cart.modify_ordered_product()




def remove_from_cart(**kwargs):
    pass


def delete_cart(**kwargs):
    cart = get_model_by_id_or_raise(Cart, kwargs['id'])
    cart.delete()
