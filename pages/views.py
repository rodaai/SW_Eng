from django.shortcuts import render
from datetime import datetime

def home(request):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    context = {
        "cafe_name": "Roda Cafe",
        "description": "welcome to roda cafe for best coffee in ibb",
        "branch_number": 1,
        "is_open": True,
        "theme": theme,
        "current_hour": current_hour,
        "student": {
            "name": "Roda",
            "level": "الرابع",
            "grade": 98
        },
        "cafe_info": {
            "owner": "Roda",
            "city": "إب - اليمن",
            "rating": 4.9
        },
        "drinks": [
            {
                "name": "لاتيه", 
                "desc": "قهوة بالحليب بطعم غني.", 
                "price": 900, 
                "image": "https://images.unsplash.com/photo-1511920170033-f8396924c348"
            },
            {
                "name": "كابتشينو", 
                "desc": "نكهة كلاسيكية برغوة كريمية.", 
                "price": 1000, 
                "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
            },
            {
                "name": "إسبريسو", 
                "desc": "قهوة مركزة لعشاق المذاق القوي.", 
                "price": 800, 
                "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93"
            },
            {
                "name": "موكا", 
                "desc": "مزيج القهوة مع الشوكولاتة.", 
                "price": 1100, 
                "image": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735"
            },
        ]
    }
    return render(request, "pages/home.html", context)


def about(request):
    current_hour = datetime.now().hour
    theme = "day" if 6 <= current_hour < 18 else "night"

    context = {
        "title": "about roda cafe",
        "manager": "Eng. Roda",
        "phone": "777 777 777",
        "working_hours": "8:00 AM - 11:00 PM",
        "show_contact": True,
        "theme": theme,
        "current_hour": current_hour
    }
    return render(request, "pages/about.html", context)