from odoo import fields, models


class MpFlujo(models.Model):
    _name = 'mp.flujo'
    _rec_name = "codigo"

    codigo = fields.Char()
    grupo_flujo_ids = fields.One2many(comodel_name="mp.grupo.flujo", inverse_name="flujo_id")
    decripcion = fields.Text()
