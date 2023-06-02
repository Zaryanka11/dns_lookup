from django.contrib import admin
from market.models import Provider, Customer, Category, Product, Store, Delivery, OrderProduct

class ProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Provider, ProviderAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag']
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Delivery, DeliveryAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(OrderProduct, OrderProductAdmin)

