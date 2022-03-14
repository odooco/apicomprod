##########################################################################################
#
# Ing.Luis Felipe Paternina
#
# correo: lfpaternina93@gmail.com
#
# +573215062353
#
# Bogota, Colombia
#
############################################################################################


{
    'name': 'Sale order Sannic',

    'version': '14',

    'author': "Luis Felipe Paternina",

    'website': "",

    'category': 'learning',

    'depends': [
        'base', 
        'base_address_city',
        'sale_management',
        'crm',
        'sale_margin',
        'sale_approval_co'
    ],

    'data': [

        'views/sale_order.xml',
        'views/crm_lead.xml',
        'views/sale_order_freigth.xml',
        'views/purchase_order.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
              
    ],
    'installable': True
}