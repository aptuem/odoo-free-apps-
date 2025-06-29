# -*- coding: utf-8 -*-

#############################################################################
#
#    Aptuem solutions.
#
#    Copyright (C) 2025-TODAY Aptuem solutions(<https://aptuem.com>)
#    Author: Gamal Ashraf, Aptuem solutions (<https://aptuem.com>)
#
#    You can't modify this app under any circumstances.
#
#############################################################################

{
    'name': 'Unique Customer & Vendor (Mobile and  Phone) Validator',
    'version': '18.0.1.0.0',
    'module_type': 'official',
    'icon': './static/description/icon.png',
    'images': ['static/description/banner.gif'],
    'price': "10",
    'currency': "USD",
    'summary': "Prevent duplicate phone numbers across customers in Odoo. Keywords: Odoo, contact, search, phone, number, CRM, contact, management, search app, Odoo module, customer, data, phone lookup, business efficiency.",

    'description': """
        This module enforces data integrity by ensuring that phone numbers assigned
        to partners (customers or vendors) are unique in the system.

        ✅ Prevents saving duplicate phone numbers
        ✅ Raises a clear validation error with the conflicting partner's name
        ✅ Helps maintain clean and consistent contact records

        Benefits:
        - Avoids confusion during sales, support, or invoicing due to duplicated phone entries.
    """,

    'author': 'Gamal Ashraf, Aptuem solutions',
    'website': "https://www.aptuem.com",
    'category': "Contacts",
    'license': 'OPL-1',  # Odoo Proprietary License (suitable for paid modules)
    'depends': ['base'],
    'data': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    # Price: $29 USD (Informational only; pricing is handled in the app store or invoice)
}
