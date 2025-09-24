# Fichier : __manifest__.py carte d'identité
{
    'name': "Module Achat",
    'version': '1.0',
    'depends': ['base','product','mail'],
    'icon':'bon_commande/static/description/purchase.png',
    'data': [
        'security/bon_commande_security.xml',
        'security/ir.model.access.csv',
        'views/bon_commande_report.xml',
        'views/bon_commande_sequence.xml',
        'views/bon_commande_view.xml',
        'views/bon_commande_menu.xml',
    ],
    'installable': True,
    'application': True,
}