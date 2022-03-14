from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    is_comodin = fields.Boolean(string="Is Comodin",related="product_id.is_comodin")
    vendors_id = fields.Many2one('res.partner',string="Proveedor",tracking=True)

