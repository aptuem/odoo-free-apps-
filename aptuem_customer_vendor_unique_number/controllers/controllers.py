# -*- coding: utf-8 -*-
# from odoo import http


# class AptuemCustomerVendorUniqueNumber(http.Controller):
#     @http.route('/aptuem_customer_vendor_unique_number/aptuem_customer_vendor_unique_number', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aptuem_customer_vendor_unique_number/aptuem_customer_vendor_unique_number/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aptuem_customer_vendor_unique_number.listing', {
#             'root': '/aptuem_customer_vendor_unique_number/aptuem_customer_vendor_unique_number',
#             'objects': http.request.env['aptuem_customer_vendor_unique_number.aptuem_customer_vendor_unique_number'].search([]),
#         })

#     @http.route('/aptuem_customer_vendor_unique_number/aptuem_customer_vendor_unique_number/objects/<model("aptuem_customer_vendor_unique_number.aptuem_customer_vendor_unique_number"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aptuem_customer_vendor_unique_number.object', {
#             'object': obj
#         })

