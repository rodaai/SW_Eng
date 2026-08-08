from django.shortcuts import render
from datetime import datetime
from django.db.models import Q
from products.models import Product

def home(request):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    # جلب مدخلات البحث إن وجدت
    query = request.GET.get('q', '').strip()

    # الاستعلام من قاعدة البيانات المحلية
    if query:
        db_products = Product.objects.filter(
            Q(name_ar__icontains=query) |
            Q(name_en__icontains=query) |
            Q(details__icontains=query)
        )
    else:
        db_products = Product.objects.all()

    # تحويل كائنات المودل لشكل قاموس ليتوافق تماماً مع home.html
    menu_items = []
    for item in db_products:
        menu_items.append({
            "id": item.id,
            "category": item.category.code,
            "name_ar": item.name_ar,
            "name_en": item.name_en,
            "price": item.price,
            "calories": item.calories,
            "details": item.details,
            "in_stock": item.in_stock,
            "ingredients": item.get_ingredients_list()
        })

    context = {
        "cafe_name": "roda cafe",
        "description": "welcome to roda cafe for best coffee in ibb",
        "menu_items": menu_items,
        "theme": theme,
        "query": query,
    }
    return render(request, "pages/home.html", context)


def detail(request, item_id):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    # جلب المنتجات من قاعدة البيانات لتهيئة القالب
    all_products = Product.objects.all()
    all_items = []
    selected_item = None

    for item in all_products:
        item_dict = {
            "id": item.id,
            "category": item.category.code,
            "name_ar": item.name_ar,
            "name_en": item.name_en,
            "price": item.price,
            "calories": item.calories,
            "details": item.details,
            "in_stock": item.in_stock,
            "ingredients": item.get_ingredients_list()
        }
        all_items.append(item_dict)
        if item.id == item_id:
            selected_item = item_dict

    # جلب المنتجات المقترحة من نفس الفئة
    related_items = []
    if selected_item:
        related_items = [
            i for i in all_items 
            if i["category"] == selected_item["category"] and i["id"] != item_id
        ]

    context = {
        "item": selected_item,
        "item_id": item_id,
        "related_items": related_items,
        "all_items": all_items,
        "discount_code": None,
        "theme": theme,
    }
    return render(request, "pages/detail.html", context)


def about(request):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    context = {
        "title": "about roda cafe",
        "manager": "Eng. Roda",
        "phone": "777 777 777",
        "working_hours": "8:00 AM - 11:00 PM",
        "theme": theme,
    }
    return render(request, "pages/about.html", context)