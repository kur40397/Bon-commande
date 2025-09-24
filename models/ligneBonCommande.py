from odoo import fields, models, api


class LigneBonCommande(models.Model):
    _name = 'bon_commande.ligne_bon_commande'
    _description = 'ligne de bon de commande'
    reference=fields.Char("Reference")
    product_id=fields.Many2one("product.product","Produit")
    quantite=fields.Integer("Quantite")
    prix_unitaire=fields.Float("prix unitaire")
    prix_total_ligne=fields.Float("prix total de la ligne",compute="_compute_prix_total_ligne",store=True)
    bon_commande_id=fields.Many2one("bon_commande.bon_commande")

    @api.depends("quantite","prix_unitaire")
    def _compute_prix_total_ligne(self):
        for rec in self:
           rec.prix_total_ligne=rec.prix_unitaire*rec.quantite


