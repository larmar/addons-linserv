# -*- coding: utf-8 -*-
# Copyright 2017 Linserv (<http://www.linserv.se>)
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class ProviderBring(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(selection_add=[('bring', 'Bring')])
    # Fields Needed to create shipment in Bring
    bring_api_key = fields.Char(string="Api Key")
    bring_api_uid = fields.Char(string="Api Uid")
    bring_client_url = fields.Char(string="Client URL")

    product_id = fields.Selection([
        ('BUSINESS_PARCEL', 'BUSINESS PARCEL'),
        ('PICKUP_PARCEL', 'PICKUP_PARCEL'),
        ('BUSINESS_PALLET', 'BUSINESS_PALLET')
    ], String="Product id")
    customerNumber = fields.Char(string="Customer Number")

    def bring_rate_shipment(self, order):
        return {'success': True,
                'price': price,
                'error_message': False,
                'warning_message': False}

    def bring_send_shipping(self,picking):
        res = []

        shiping_data = {'exact_price': 15.0,
                        'tracking_number': "12345"}
        res = res + [shiping_data]

        return res

    def bring_get_tracking_link(self, picking):
        return 'https://www.linserv.se'

    def bring_cancel_shipment(self, picking):
        raise UserError(_("You can not cancel a Bring shipment when a shipping label has already been generated."))


