# pages/templatetags/cafe_filters.py
from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='yemeni_currency')
def yemeni_currency(value, symbol="ر.ي"):
    """
    1. فلتر العملة والأسعار:
    يقوم بتنسيق السعر وتفنيط الألف، وإضافة عملة الريال أو أي عملة تحددينها.
    الاستخدام: {{ product.price|yemeni_currency }}
    """
    try:
        val = float(value)
        return f"{val:,.0f} {symbol}"
    except (ValueError, TypeError):
        return value


@register.filter(name='discount_price')
def discount_price(value, percentage=10):
    """
    2. فلتر حساب الخصومات والعروض:
    يحسب السعر بعد الخصم مباشرة تلقائياً (الافتراضي 10%).
    الاستخدام: {{ product.price|discount_price:20 }}  (لخصم 20%)
    """
    try:
        val = float(value)
        discount = val * (float(percentage) / 100)
        new_price = val - discount
        return f"{new_price:,.0f} ر.ي"
    except (ValueError, TypeError):
        return value


@register.filter(name='yemeni_status')
def yemeni_status(text):
    """
    3. فلتر تحويل المصطلحات إلى اللهجة المحلية/العامية اليمنية:
    يحول كلمات المنيو أو النصوص إلى طابع يمني محلي جذاب للمحل.
    الاستخدام: {{ item.name|yemeni_status }}
    """
    if not isinstance(text, str):
        text = str(text)
    
    dict_map = {
        "شاي": "شاهي خادر",
        "قهوة": "بن يمني فاخر",
        "ماء": "ماي بارد",
        "كيك": "حالي / حلى الكافيه",
        "جديد": "جديدنا اليوم",
        "متوفر": "موجود",
        "غير متوفر": "ما بش",
    }
    
    for word, replacement in dict_map.items():
        text = text.replace(word, replacement)
    return text


@register.filter(name='cafe_badge')
def cafe_badge(is_hot):
    """
    4. فلتر إضافة إيموجي وشارات للمشروبات (ساخن / بارد):
    يعرض أيقونة مناسبة بحسب نوع المشروب.
    الاستخدام: {{ product.is_hot|cafe_badge }}
    """
    if is_hot:
        return "🔥 ساخن"
    return "❄️ بارد"