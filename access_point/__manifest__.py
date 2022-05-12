# -*- coding: utf-8 -*-
{
    'name': "Access Point",

    'summary': """
         Module extension that creates a restful endpoint on Odoo modules and records.""",

    'description': """
        Module extension that creates a restful endpoint on Odoo modules and records  
        """,

    'author': "housemateguy",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
               "views/ir_model.xml",
                "views/res_users.xml",
                "security/ir.model.access.csv"
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
