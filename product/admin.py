from django.contrib import admin
from product.models import Category, Product, Images, Comment, Order
from mptt.admin import DraggableMPTTAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title']
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug':('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_cumulative_count',
            cumulative=True
        )

        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False
        )
        return qs
    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'
    def related_products_cumulative_count(self,instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
########################################################################################################################
########################################################################################################################
########################################################################################################################

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5
########################################################################################################################
########################################################################################################################
########################################################################################################################


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag',  'price']
    list_filter = ['category']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}

########################################################################################################################
########################################################################################################################
########################################################################################################################
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','phone', 'comment',  'create_at']
    readonly_fields = ('name','phone', 'comment', 'ip',  'product', )



class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'amount', 'category', 'food', 'address','ip',]
    list_filter = ['status']


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Order, OrderAdmin)