
from odoo import models, fields, api

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Marca producto'

    name =  fields.Char(string="Nombre")
    product_brand_id = fields.Many2one('product.brand',string="Marca producto")
   

