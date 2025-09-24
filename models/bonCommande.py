from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import UserError


class BonCommande(models.Model):
  _name = 'bon_commande.bon_commande'
  _description = 'bon_commande.bon_commande'
  #Un mixin en Odoo (et en programmation objet) est une classe qu’on ajoute à une autre
  # pour lui donner des fonctionnalités supplémentaires, sans tout réécrire
  _rec_name = 'reference'
  _inherit = ['mail.thread','mail.activity.mixin']

  reference=fields.Char("Reference",readonly=True, copy=False)
  fournisseur=fields.Many2one("res.partner","Fournisseur")
  date_commande=fields.Date(string="Date commande")
  date_reception=fields.Date(string="Date reception")
  currency_id=fields.Many2one("res.currency",default=lambda self: self.env.user.company_id.currency_id.id)
  total_ht=fields.Monetary(string="Total HT",compute="_compute_total_ht",store=True,currency_field="currency_id")
  total_ttc=fields.Monetary(string="Total TTC",compute="_compute_total_ht",store=True,currency_field="currency_id")
  etat=fields.Selection(
    [
      ("draft","brouillon"),
      ("valide","validé"),
    ],default="draft"
  )
  commentaire=fields.Text("Commentaire")
  ligne_bon_commande_ids=fields.One2many("bon_commande.ligne_bon_commande","bon_commande_id")

  @api.depends("ligne_bon_commande_ids")
  def _compute_total_ht(self):
    self.total_ht=sum(self.ligne_bon_commande_ids.mapped("prix_total_ligne"))
    self.total_ttc= self.total_ht*0.2

  def methode_changer_state(self):
    self.write({
      'etat':'valide',
      # cherche le prochain numéro dans la sequence
      'reference':self.env['ir.sequence'].next_by_code("bon_commande.bon_commande")
    })
    if not (self.fournisseur and self.date_reception and self.date_commande and self.ligne_bon_commande_ids):
      raise UserError("Essaye de remplir tous les champs")
    elif self.date_reception < self.date_commande:
      raise UserError("la date de reception est supérieur a la date de commande")



    self.message_post(body="un bon de commande a été ajouté",subject="Validation de bon de commande")
  # bon_commande_id =>

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

