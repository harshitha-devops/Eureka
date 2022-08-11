# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DieHistory(models.Model):
    _name = 'die.history'
    _inherit = ['die.master', 'mail.thread', 'mail.activity.mixin']
    _description = 'Die History'

    die_number = fields.Many2one("die.master", string='Die Number')
    image = fields.Many2one("die.master", string='Picture')
    die_type = fields.Many2one(string='Die Type')
    number_of_cavity = fields.Many2one("die.master", string='Number of Cavity')
    die_size = fields.Many2one("die.master", string='Die Size')
    bolster_no = fields.Many2one("die.master", string='Bolster No')
    die_supplier = fields.Many2one("die.master", string='Die Supplier')
    # nitriding_date = fields.Many2one("die.nitriding", string='Nitriding Date')
# inherited fields from die management ends here

    production_date = fields.Date(string='Production Date')
    input1 = fields.Float(string='Input(Kg)', digits=[4, 3], default=0.0001)
    output1 = fields.Float(string='Output(Kg)', digits=[4, 3], default=0.0001)
    recovery = fields.Float(string='Recovery %', compute="_compute_recovery", store=True)
    productivity = fields.Float(string='Productivity (kg/Hr)')
    run_wtpm = fields.Float(string="Actual Wt/meter", digits=[4, 3], default=1.0)
    unload_code = fields.Selection([('die line', 'Die Line'),
                                    ('order completed', 'Order Completed'),
                                    ('plan completed', 'Plan Completed'),
                                    ('flow defect', 'Flow Defect'),
                                    ('breakage', 'Breakage'),
                                    ('breakdown', 'Breakdown'),
                                    ('power failure', 'Power Failure'),
                                    ('rough surface', 'Rough Surface'),
                                    ('weight out of range', 'Weight Out of Range'),
                                    ], string='Unload Code', default='plan completed')


    @api.depends('input1', 'output1')
    def _compute_recovery(self):
        for record in self:
            record.recovery = (record.output1) * 100 / record.input1


class DieNitriding(models.Model):
    _name = 'die.nitriding'
    _inherit = ['die.master', 'mail.thread', 'mail.activity.mixin']
    _description = 'Die Nitriding'

    die_number = fields.Many2one("die.master", string='Die Number')
    nitriding_date = fields.Date(string='Nitriding Date')
    batch_num = fields.Char(string='Batch Num')
    operator = fields.Char(string='Operator')
