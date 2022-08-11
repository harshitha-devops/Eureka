# -*- coding: utf-8 -*-
{
    'name': "Eureka Extrusions Die Management5",

    'summary': """
        This is Die Management System""",

    'description': """
       For use @ Eureka Extrusions & Finishers
       04/08/2022
    """,

    'author': "Shridhara Metgal",
    'website': "https://myeureka.in",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.2',
    'sequence': '1',
    'installable': True,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
