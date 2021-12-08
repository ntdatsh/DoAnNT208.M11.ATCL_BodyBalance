from decimal import Decimal
from django.conf import settings

from catagories.models import whey, Product, PT

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, qty):
        # Thêm hoặc cập nhật session của giỏ hàng

        # pr_id = str(product)
        pr_id = str(product.whey_id)
        # pro_id = str(product.pr_id)
        # pt_id = str(product.pt_id)
        # self.cart[pr_id] = pr_id
        
        # if pro_id in self.cart:
        #     self.cart[pro_id]["qty"] = qty
        # else:
        #     self.cart[pro_id] = {"price": str(product.pr_price), "qty": qty}
        

        # if pr_id in self.cart:
        #     self.cart[pt_id]["qty"] = qty
        # else:
        #     self.cart[pt_id] = {"price": str(product.pt_price), "qty": qty}

        if pr_id in self.cart:
            self.cart[pr_id]["qty"] = qty
        else:
            self.cart[pr_id] = {"price": str(product.whey_price), "qty": qty}
        self.save()

    def add1(self, product1, qty):
        pro_id = str(product1.pr_id)

        if pro_id in self.cart:
            self.cart[pro_id]["qty"] = qty
        else:
            self.cart[pro_id] = {"price": str(product1.pr_price), "qty": qty}
        self.save()

    def __iter__(self):
        # Lấy product_id trong session để query dữ liệu trong database
        product_ids = self.cart.keys()
        products = whey.objects.filter(whey_id__in=product_ids)
        product1 = Product.objects.filter(pr_id__in=product_ids)
        # product2 = PT.objects.filter(pt_id__in=product_ids)
        cart = self.cart.copy()

        for product in product1:
            cart[str(product.pr_id)]["product"] = product

        # for product in product2:
        #     cart[str(product.pt_id)]["PT"] = product

        for product in products:
            cart[str(product.whey_id)]["whey"] = product

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
    #     Lấy dữ liệu giỏ hàng và đếm số lượng sản phẩm ở trong đó
        return 1
        # sum(item["qty"] for item in self.cart.values())

    # def get_qty(self):
    #     count = 0
    #     cart = self.cart.copy()
    #     if cart.values() != 0:
    #         for item in cart.values():
    #             count +=1
    #     return count
    
    # def update(self, product, qty):
    #     # Cập nhật giá trị session giỏ hàng

    #     product_id = str(product)
    #     if product_id in self.cart:
    #         self.cart[product_id]["qty"] = qty
    #     self.save()

    # Hàm này để tính trước giá trước khi có giao hàng, nhưng chưa có giao hàng nên để qua 1 bên
    # def get_subtotal_price(self):
    #     return sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    # def get_delivery_price(self):
    #     newprice = 0.00

    #     if "purchase" in self.session:
    #         newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

    #     return newprice

    # def get_total_price(self):
    #     newprice = 0.00
    #     subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())

    #     if "purchase" in self.session:
    #         newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

    #     total = subtotal + Decimal(newprice)
    #     return total

    # def delete(self, product):
    #     # Xóa sản phẩm trong session 

    #     product_id = str(product)

    #     if product_id in self.cart:
    #         del self.cart[product_id]
    #         self.save()

    # def clear(self):
    #     # Xóa luôn giỏ hàng
    #     del self.session[settings.CART_SESSION_ID]
    #     del self.session["address"]
    #     del self.session["purchase"]
    #     self.save()

    def save(self):
        self.session.modified = True
    
    # def cart_update_delivery(self, deliveryprice=0):
    #     subtotal = sum(Decimal(item["price"]) * item["qty"] for item in self.cart.values())
    #     total = subtotal + Decimal(deliveryprice)
    #     return total

