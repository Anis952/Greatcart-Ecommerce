from django.contrib import admin
from .models import Category


class categoryAdmin(admin.ModelAdmin):
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        self.slug = slugify(self.category_name)
        super(categoryAdmin, self).save(*args, **kwargs)

        
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category,categoryAdmin)

