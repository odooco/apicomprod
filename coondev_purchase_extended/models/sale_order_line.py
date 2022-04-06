from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    supplier_id = fields.Many2one('res.partner',string="Proveedor",tracking=True)

