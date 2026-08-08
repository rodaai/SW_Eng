from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم الفئة")
    code = models.CharField(max_length=20, unique=True, verbose_name="كود الفئة (مثل: drinks, sweets, fast_food)")

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="الفئة")
    name_ar = models.CharField(max_length=100, verbose_name="الاسم بالعربي")
    name_en = models.CharField(max_length=100, verbose_name="الاسم بالإنجليزي")
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10, verbose_name="السعر")
    calories = models.IntegerField(verbose_name="السعرات الحرارية")
    details = models.TextField(verbose_name="الوصف التفصيلي")
    ingredients = models.TextField(help_text="أدخل المكونات مفصولة بفواصل (مثال: قهوة, حليب, سكر)", verbose_name="المكونات")
    in_stock = models.BooleanField(default=True, verbose_name="متوفر بالمخزون")

    def get_ingredients_list(self):
        return [i.strip() for i in self.ingredients.split(',') if i.strip()]

    def __str__(self):
        return self.name_ar