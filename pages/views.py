from django.shortcuts import render
from datetime import datetime

# قائمة البيانات الشاملة (MENU_DATA) مع أسماء عربية وإنجليزية لكل صنف
MENU_DATA = [
    # ☕ قسم المشروبات
    {
        "id": 1, 
        "category": "drinks", 
        "name_ar": "شاي عدني خادر", 
        "name_en": "adenese tea with milk", 
        "price": 400, 
        "calories": 120, 
        "details": "شاي فاخر مطبوخ على النار الهادئة مع الحليب المكثف والبهارات العدنية الأصيلة", 
        "in_stock": True, 
        "ingredients": ["شاي ممتاز", "حليب مكثف", "هيل", "قرفة"]
    },
    {
        "id": 2, 
        "category": "drinks", 
        "name_ar": "إسبريسو سينجل", 
        "name_en": "espresso single shot", 
        "price": 800, 
        "calories": 10, 
        "details": "جرعة قهوة مركزة ومستخلصة غنية بالكريمة الذهبية من أجوَد حبوب البن المحمصة", 
        "in_stock": True, 
        "ingredients": ["بن يمني محمص 100%"]
    },
    {
        "id": 3, 
        "category": "drinks", 
        "name_ar": "سبانيش لاتيه بارد", 
        "name_en": "iced spanish latte", 
        "price": 1500, 
        "calories": 280, 
        "details": "مزيج منعش من قهوة الإسبريسو والحليب البارد مع الحليب المكثف المحلى وقطع الثلج", 
        "in_stock": True, 
        "ingredients": ["إسبريسو", "حليب بارد", "حليب مكثف", "ثلج"]
    },

    # 🍰 قسم الحلويات
    {
        "id": 4, 
        "category": "sweets", 
        "name_ar": "تشيز كيك توت", 
        "name_en": "blueberry cheesecake", 
        "price": 1800, 
        "calories": 450, 
        "details": "طبقة كريمة جبن غنية وناعمة على قاعدة بسكويت هش يعلوها صوص التوت الطبيعي", 
        "in_stock": True, 
        "ingredients": ["جبن كريمي", "بسكويت دايجستف", "صوص توت"]
    },
    {
        "id": 5, 
        "category": "sweets", 
        "name_ar": "وافل بالشوكولاتة", 
        "name_en": "nutella belgian waffle", 
        "price": 1600, 
        "calories": 520, 
        "details": "وافل بلجيكي مقرمش من الخارج وهش من الداخل يقدم مع شوكولاتة نوتيلا وموز", 
        "in_stock": False, 
        "ingredients": ["عجين الوافل", "نوتيلا", "شرائح موز"]
    },

    # 🍔 قسم الوجبات السريعة
    {
        "id": 6, 
        "category": "fast_food", 
        "name_ar": "برجر دجاج كريسبي", 
        "name_en": "crispy chicken burger", 
        "price": 2200, 
        "calories": 680, 
        "details": "صدر دجاج مقرمش ذهبي مع جبنة شيدر سائبة وصوص الكافيه المميز في خبز بريوش", 
        "in_stock": True, 
        "ingredients": ["دجاج مقرمش", "خبز بريوش", "جبنة شيدر", "خس"]
    },

    # 🍕 قسم المأكولات
    {
        "id": 7, 
        "category": "food", 
        "name_ar": "بيتزا مارجريتا إيطالية", 
        "name_en": "italian margarita pizza", 
        "price": 2800, 
        "calories": 720, 
        "details": "عجينة إيطالية رقيقة مع صوص الطماطم الطازج وجبنة الموزاريلا الفاخرة وأوراق الريحان", 
        "in_stock": True, 
        "ingredients": ["عجينة بيتزا", "صلصة طماطم", "جبنة موزاريلا"]
    },
]


def home(request):
    # تحديد الثيم تلقائياً حسب الوقت (نهاري بين 6 صباحاً و 6 مساءً)
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    context = {
        "cafe_name": "roda cafe",
        "description": "welcome to roda cafe for best coffee in ibb",
        "menu_items": MENU_DATA,
        "theme": theme,
    }
    return render(request, "pages/home.html", context)


def detail(request, item_id):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    # البحث عن الصنف المختار
    selected_item = next((item for item in MENU_DATA if item["id"] == item_id), None)
    
    # جلب أصناف مشابهة من نفس القسم
    related_items = [i for i in MENU_DATA if selected_item and i["category"] == selected_item["category"] and i["id"] != item_id]

    context = {
        "item": selected_item,
        "item_id": item_id,
        "related_items": related_items,
        "all_items": MENU_DATA,      # لتشغيل فلتر length
        "discount_code": None,        # لتشغيل فلتر default (لأنه فارغ None)
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