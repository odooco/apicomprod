from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_comodin = fields.Boolean(string="Is Comodin")
    product_brand_id = fields.Many2one('product.brand',string="Marca producto")


