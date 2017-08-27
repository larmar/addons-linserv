# -*- coding: utf-8 -*-
# Copyright 2017 Linserv (<http://www.linserv.se>) 
# See LICENSE file for full copyright and licensing details.

from odoo import models, api

class ProductProduct(models.Model):
    _inherit = "product.product"

    _sql_constraints = [
        ('default_code_unique', 'unique (default_code)', 'Product Internal Reference must be unique!'),
    ]
