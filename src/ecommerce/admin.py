from django.contrib import admin

# Register your models here.

from .models import Merchant,Shopper,Order,Disbursements
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MerchantResource(resources.ModelResource):
   class Meta:
      model = Merchant
class MerchantAdmin(ImportExportModelAdmin):
   resource_class = MerchantResource

class ShopperResource(resources.ModelResource):
   class Meta:
      model = Shopper
class ShopperAdmin(ImportExportModelAdmin):
   resource_class = ShopperResource


class OrderResource(resources.ModelResource):
   class Meta:
      model = Order
      widgets = {
                'Completed': {'format': '%d/%m/%Y %H:%M:%S'},
                'Created': {'format': '%d/%m/%Y %H:%M:%S'},
                }
class OrderAdmin(ImportExportModelAdmin):
   resource_class = OrderResource

admin.site.register(Merchant,MerchantAdmin)
admin.site.register(Shopper,ShopperAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Disbursements)