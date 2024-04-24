from odoo import models, fields, api, _


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    account_move_id = fields.Many2one(comodel_name='account.move', string='Factura')
