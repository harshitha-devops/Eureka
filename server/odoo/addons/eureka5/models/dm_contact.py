# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DmCustomer(models.Model):
    _name = 'dm.customer'
    _description = 'Profile Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'customer_name_id'

    customer_name_id = fields.Char(string='Customer Name')
    addressline1 = fields.Char(string='Addressline1')
    addressline2 = fields.Char(string='Addressline2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')

class DmSupplier(models.Model):
    _name = 'dm.supplier'
    _description = 'Die Supplier'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'supplier_name_id'

    supplier_name_id = fields.Char(string='Supplier Name')
    addressline1 = fields.Char(string='Addressline1')
    addressline2 = fields.Char(string='Addressline2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')