from django.db import models
from django.utils.translation import gettext_lazy as _




class Category(models.Model):
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,verbose_name=_("parent"))
    title = models.CharField(_("Category Title"),max_length=100)
    description=models.TextField(_("Description"),blank=True)
    avatar=models.ImageField(_("avatar"),upload_to="category/", blank=True)
    is_enable=models.BooleanField(_("is enable"),default=True)
    created_time=models.DateTimeField(_("created time"),auto_now_add=True)
    updated_time=models.DateTimeField(_("updated time"),auto_now_add=True)
    
    
    
    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        
    

    def __str__(self):
        return self.title
    
    
    class Product(models.Model):
        categories=models.ManyToManyField("Category",verbose_name=_("categories"),blank=True)
        title = models.CharField(_("Product Title"),max_length=100)
        description=models.TextField(_("Description"),blank=True)
        avatar=models.ImageField(_("avatar"),upload_to="product/", blank=True)
        is_enable=models.BooleanField(_("is enable"),default=True)
        created_time=models.DateTimeField(_("created time"),auto_now_add=True)
        updated_time=models.DateTimeField(_("updated time"),auto_now_add=True)



        class Meta:
            db_table = "products"
            verbose_name = _("product")
            verbose_name_plural = _("products")



        def __str__(self):
            return self.title
        

class File(models.Model):
    
    
    product=models.ForeignKey("Product",on_delete=models.CASCADE,verbose_name=_("product"))
    title=models.CharField(_("Title"),max_length=50,blank=True)
    file=models.FileField(_("file"),upload_to="files/%Y/%m/%d/")
    is_enable=models.BooleanField(_("is enable"),default=True)
    created_time=models.DateTimeField(_("created time"),auto_now_add=True)
    updated_time=models.DateTimeField(_("updated time"),auto_now_add=True)

    class Meta:
        db_table = "files"
        verbose_name = _("file")
        verbose_name_plural = _("files")


    def __str__(self):
        return self.title