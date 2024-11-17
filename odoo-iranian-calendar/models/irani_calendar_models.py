# models/irani_calendar_models.py
from odoo import models, api
from convertdate import iranian
from datetime import datetime

class Iranians(models.Model):
    _name = 'iranians.tools'
    
    @api.model
    def to_persian_date(self, date):
        """تبدیل تاریخ میلادی به شمسی"""
        if not date:
            return ""
        
        # تاریخ میلادی را به شمسی تبدیل می‌کنیم
        date_persian = iranian.from_gregorian(date.year, date.month, date.day)
        return f'{date_persian[0]}-{date_persian[1]:02d}-{date_persian[2]:02d}'
    