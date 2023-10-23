from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    mp_flujo_id = fields.Many2one(comodel_name="mp.flujo")
    mp_grupo_flujo_id = fields.Many2one(comodel_name="mp.grupo.flujo")
