# -*- coding: utf-8 -*-
# Copyright 2017 Linserv (<http://www.linserv.se>)
# See LICENSE file for full copyright and licensing details.
{
    'name': "Bring Shipping",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Linserv Consulting AB",
    'website': "http://www.linserv.se",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Warehouse',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['delivery', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/delivery_bring_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
