# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DieMaster(models.Model):
    _name = 'die.master'
    _description = 'Die Master'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'die_number'

    die_number = fields.Char(string='Die Number', required=True)
    image = fields.Binary(string='Picture', store=True)
    die_type = fields.Selection([('port_hole', 'Port Hole'),
                                 ('solid_lip', 'Solid LIP SET'),
                                 ('sob', 'SOB'),
                                 ('shut', 'Shut Off'),
                                 ('insert', 'Insert Type'),
                                 ('stone', 'Stone'),
                                 ('other', 'Other'),
                                 ], string='Die Type')
    number_of_cavity = fields.Integer(string='Number of Cavity', default=1)
    die_size = fields.Char(string='Die Size')
    bolster_no = fields.Char(string='Bolster No')
    supplier_name_id = fields.Many2one("dm.supplier", string='Die Supplier')
    base_price = fields.Float(string='Base Price (Ex-Works)')
    tax_gst = fields.Float(string='Tax_GST')
    frieght = fields.Float(string='Frieght')
    total_price = fields.Float(string='Total Price', compute="_compute_total", store=True)
    lot_no = fields.Char(string='Lot No')
    status = fields.Selection([('running', 'Running'),
                               ('hold', 'Hold'),
                               ('scrap', 'Scrap')],string='Status',default='running')
    lead_plate = fields.Char(string='Lead Plate')
    backer = fields.Char(string='Backer')
    Standard = fields.Char(string='Standard')
    physical_location = fields.Char(string='Physical Location')
    die_converted_from = fields.Char(string='Die Converted From')
    die_converted_to = fields.Char(string='Die Converted To')
    money_paid_by_eureka = fields.Float(string='Money Paid by Eureka')
    money_paid_by_customer = fields.Float(string='Money Paid By Customer')
    payment_returnable = fields.Boolean(string='Payment Returnable')
    customer_name_id = fields.Many2one('dm.customer', string='Profile Customer Name')
    order_date = fields.Date(string='Order Date')
    landed_date = fields.Date(string='Landed Date', default=fields.Date.today)
    lead_time_days = fields.Integer(string='Lead Time in Days', compute="_days_difference", store=True)
    hardness_die_plate = fields.Float(string='Hardness Die Plate')
    hardness_mand_feeder = fields.Float(string='Hardness Mand/Feeder')
    ordered_die_weight = fields.Float(string='Ordered Die weight', digits=[4, 3])
    weight_code = fields.Char(string='Weight Code')

    @api.depends('base_price', 'tax_gst', 'frieght')
    def _compute_total(self):
        for record in self:
            record.total_price = record.base_price + record.tax_gst + record.frieght

    @api.constrains('order_date', 'landed_date', 'days_diff')
    def _days_difference(self):
        for record in self:
            if record.order_date > record.landed_date:
               raise ValidationError('Order date should not greater than landed date.')
            else:
               record.lead_time_days = (record.landed_date - record.order_date).days
