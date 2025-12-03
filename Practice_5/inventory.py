#!/usr/bin/env python3
"""
Ürün Envanter Sistemi
- inventory: {sku: {'name':..., 'price':..., 'stock':...}}
- Fonksiyonlar: add_product, update_stock, search_by_name, get_product
"""
from typing import Dict, Any, List

inventory: Dict[str, Dict[str, Any]] = {}


def add_product(sku: str, name: str, price: float, stock: int = 0):
    if sku in inventory:
        raise KeyError('SKU zaten mevcut')
    inventory[sku] = {'name': name, 'price': float(price), 'stock': int(stock)}


def update_stock(sku: str, delta: int):
    if sku not in inventory:
        raise KeyError('SKU bulunamadı')
    inventory[sku]['stock'] = int(inventory[sku]['stock']) + int(delta)
    return inventory[sku]['stock']


def search_by_name(query: str) -> List[Dict[str, Any]]:
    q = query.lower()
    return [ {'sku': sku, **data} for sku, data in inventory.items() if q in data['name'].lower() ]


def get_product(sku: str) -> Dict[str, Any]:
    return inventory.get(sku)


if __name__ == '__main__':
    print('Envanter demo: örnek ürünler ekleniyor')
    add_product('SKU001','Kalem',2.5,100)
    add_product('SKU002','Defter',10.0,50)
    print('Arama: "kalem" =>', search_by_name('kalem'))
    print('Güncelle: SKU001 stok -10 =>', update_stock('SKU001', -10))
