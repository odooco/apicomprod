
from odoo import models, fields, api
import logging

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    saleorder_id = fields.Many2one('sale.order',string="Orden de Venta")

    @api.onchange('saleorder_id')
    def _related_sale_order(self):
        sale_obj = self.env['sale.order'].search([('name', '=', self.saleorder_id.name)])
        logging.info("--------------------------------Objeto----------------------------------")
        logging.info(sale_obj)
        if sale_obj:
            sale_obj.purchaseorder = self.name
            logging.info("********************Entra y actualiza el campo en SO*********************************")
        else:
            sale_obj.purchaseorder = self.name

    @api.model
    def create(self,vals):
        rec = super(PurchaseOrder, self).create(vals)
        logging.info("++++++++++++++++++++++++++++++++Actualizo el campo en el CREATE+++++++++++++++++++++++++++++++++++++++++++")
        if vals.get('saleorder_id'):
            sale_obj = self.env['sale.order'].search([('name', '=', self.saleorder_id.name)])
            logging.info("Trajo el objeto en el CREATE")
            logging.info(sale_obj)
            if sale_obj:
                sale_obj.purchaseorder = self.name
                logging.info("================CAMPO ACTUALIZADO========================================================================")
            else:
                sale_obj.purchaseorder = self.name
        return rec
