from django.contrib import admin
from .models import pet
from cart.models import Cart 
from orders.models import Orders,Payment,OrderPet
from django.utils.html import format_html

class orderAdmin(admin.ModelAdmin):
    list_display = ['user','status']
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','payment_id','status']
    


class CustomAdmin(admin.ModelAdmin):
    list_display = ['name','breed','gender','age','description','img_display','price']
    list_filter = ['gender','animal_type']
    search_fields = ['species']
    
    def img_display(self,obj):
        return format_html('<img src="{}"width="70" height="80"/>',obj.image.url)

# Register your models here.

admin.site.register(pet,CustomAdmin)
admin.site.register(Cart)
admin.site.register(Orders,orderAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(OrderPet)
admin.site.site_header = "Pet Store Admin Panel"
admin.site.site_title = "Welcome To Pet Store"
admin.site.index_title = "Pet App Admin"
