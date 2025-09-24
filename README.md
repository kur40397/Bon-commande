# Bon-commande
bon de commande
Module de Bon de Commande
Description
Ce module Odoo a été développé pour gérer l'ensemble du processus des bons de commande, de leur création à leur impression. Il offre une solution complète et intuitive pour le suivi des achats, en automatisant plusieurs tâches clés et en améliorant l'efficacité du flux de travail.

Fonctionnalités Clés
Modèle de données complet : Gestion des bons de commande et de leurs lignes de produits associées.

Automatisation du flux de travail : Les bons de commande passent par différents états (brouillon, validé) gérés par une logique métier.

Champs calculés : Calcul automatique des totaux hors taxes (HT) et toutes taxes comprises (TTC) sur le document.

Génération de rapports : Création d'un rapport PDF professionnel au format A4 avec l'en-tête et le pied de page de l'entreprise.

Sécurité et Droits d'Accès : Création d'un groupe d'utilisateurs dédié pour gérer les permissions d'accès au module.

Widgets avancés :

statusbar : Affiche la progression des états de manière visuelle et cliquable.

many2many_tags : Permet d'ajouter des étiquettes colorées pour une classification facile.

monetary : Affiche les champs de montant avec le symbole de la devise correct.

badge : Utilise des étiquettes colorées dans la vue en liste pour une identification rapide des statuts.

Numérotation automatique : Le module génère une référence unique pour chaque nouveau bon de commande.

Structure du Module
Le module est organisé de manière standard pour un projet Odoo :

__manifest__.py : Fichier de manifeste du module, définissant ses métadonnées, ses dépendances, son icône et la liste des fichiers à charger.

models/ : Contient les modèles Python (bon_commande et bon_commande.line) et la logique métier.

views/ : Contient les vues XML (formulaire, liste, recherche) et les actions de menu.

security/ : Contient les fichiers XML et CSV pour la définition des groupes et des droits d'accès.

report/ : Contient le modèle QWeb pour la génération du rapport PDF.

static/ : Contient les assets du module, comme l'icône de l'application.

Installation
Placez le dossier bon_commande dans le répertoire des modules d'Odoo.

Dans Odoo, activez le mode développeur.

Allez dans l'application "Applications", cliquez sur "Mettre à jour la liste des applications".

Recherchez "Bon de Commande" et cliquez sur "Installer".

Utilisation
Une fois le module installé, un nouveau menu "Bon de Commande" sera disponible. Vous pouvez l'utiliser pour créer, suivre et imprimer vos documents.
