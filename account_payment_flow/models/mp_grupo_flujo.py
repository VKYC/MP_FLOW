from odoo import fields, models


class MpGrupoFlujo(models.Model):
    _name = 'mp.grupo.flujo'
    _rec_name = "nombre"

    nombre = fields.Char()
    flujo_id = fields.Many2one(comodel_name="mp.flujo")
