# -*- coding: utf-8 -*-
from odoo import http

# class DeliveryBring(http.Controller):
#     @http.route('/delivery_bring/delivery_bring/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_bring/delivery_bring/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_bring.listing', {
#             'root': '/delivery_bring/delivery_bring',
#             'objects': http.request.env['delivery_bring.delivery_bring'].search([]),
#         })

#     @http.route('/delivery_bring/delivery_bring/objects/<model("delivery_bring.delivery_bring"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_bring.object', {
#             'object': obj
#         })