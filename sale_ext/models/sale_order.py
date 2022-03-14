from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
     
    user_comercial_id = fields.Many2one(string="Vendedor Asignado",related="partner_id.user_id")