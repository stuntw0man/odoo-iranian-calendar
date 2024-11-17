# __manifest__.py
{
    'name': 'Odoo Iranian Calendar',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Your Name',
    'depends': ['base', 'calendar'],
    'data': [
        'views/calendar_views.xml',  # فایلی که تغییرات را برای تقویم اعمال می‌کند
    ],
    'installable': True,
    'application': False,
}