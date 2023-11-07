from odoo import fields, models


class MpFlujo(models.Model):
    _name = 'mp.flujo'
    _rec_name = "codigo"

    codigo = fields.Char()
    grupo_flujo_ids = fields.Many2many(comodel_name="mp.grupo.flujo", relation="mp_flujo_grupo_rel", column1="flujo_id",
                                       column2="grupo_flujo_id")
    decripcion = fields.Text()
