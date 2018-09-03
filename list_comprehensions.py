def main():
    products = [["thing", 340, False], ["ting", 300, True], ["thingy", 350, True]]
    get_sale_products(products)


def get_sale_products(products):
    on_sale_products = [product[1] for product in products if product[2]]
    print(on_sale_products)
    # could use for pg number


main()
