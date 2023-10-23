from odoo import fields, models, api
from odoo.exceptions import UserError


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    mp_flujo_id = fields.Many2one(comodel_name="mp.flujo")
    mp_grupo_flujo_ids = fields.One2many(related="mp_flujo_id.grupo_flujo_ids")
    mp_grupo_flujo_id = fields.Many2one(comodel_name="mp.grupo.flujo", domain="[('id', 'in', mp_grupo_flujo_ids)]")

    @api.onchange("mp_flujo_id")
    def _onchange_mp_flujo_id(self):
        for register_id in self:
            register_id.mp_grupo_flujo_id = self.env['mp.grupo.flujo']

    def action_create_payments(self):
        if not self.mp_flujo_id and not self.mp_grupo_flujo_id:
            raise UserError("Debe de tener almenos un flujo o un grupo de flujos seleccionado")
        res = super(AccountPaymentRegister, self).action_create_payments()
        return res

    def _init_payments(self, to_process, edit_mode=False):
        if to_process[0] and to_process[0]['create_vals']:
            to_process[0]['create_vals']['mp_flujo_id'] = self.mp_flujo_id.id
            to_process[0]['create_vals']['mp_grupo_flujo_id'] = self.mp_grupo_flujo_id.id
        res = super(AccountPaymentRegister, self)._init_payments(to_process, edit_mode)
        return res
