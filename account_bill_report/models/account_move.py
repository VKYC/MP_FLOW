
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_repr


class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_ids = fields.One2many(
        comodel_name='account.payment',
        inverse_name='account_move_id',
        string='Debitos conciliar',
        compute='_compute_debit_amount_reconcile'
    )

    def _compute_debit_amount_reconcile(self):
        for move_id in self:
            payment_ids = self.env['account.payment'].search([
                ('partner_id', '=', move_id.partner_id.id),
                ('is_reconciled', '=', False),
                ('is_matched', '=', False),
            ])
            move_id.payment_ids = payment_ids
