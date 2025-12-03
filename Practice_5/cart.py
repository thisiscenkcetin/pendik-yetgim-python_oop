"""
E-Ticaret Sepeti
"""
from typing import Dict, Any, List

cart: Dict[str, Dict[str, Any]] = {}


def add_item(sku: str, name: str, price: float, qty: int = 1):
    if sku in cart:
        cart[sku]['qty'] += qty
    else:
        cart[sku] = {'name': name, 'price': float(price), 'qty': int(qty)}


def remove_item(sku: str):
    return cart.pop(sku, None)


def update_qty(sku: str, qty: int):
    if sku not in cart:
        raise KeyError('Ürün sepetinde yok')
    cart[sku]['qty'] = int(qty)


def total_price() -> float:
    return sum(item['price'] * item['qty'] for item in cart.values())


def list_items() -> List[Dict[str, Any]]:
    return [ {'sku': sku, **item} for sku, item in cart.items() ]


if __name__ == '__main__':
    print('Sepet demo: ürün ekleniyor')
    add_item('SKU001','Kalem',2.5,3)
    add_item('SKU002','Defter',10.0,1)
    print('Sepet:', list_items())
    print('Toplam:', total_price())
