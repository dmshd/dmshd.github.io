Title: Articles en français · Comment personnaliser le menu du backoffice dans Publik ?
Date: 2022-10-16 11:27
Modified: 2022-10-16 11:27
Category: Articles en français · Publik · Le connecteur citoyen
Tags: UX, UI, publik, administrateur fonctionnel, menu, backoffice
Slug: comment-personnaliser-le-menu-du-backoffice-dans-publik
Author: Daniel Muyshond
Summary: Comment personnaliser le menu du backoffice dans Publik ?
Lang: fr
Translation: false
Status: published

## Comment personnaliser le menu du backoffice dans Publik ?

Le menu standard peut être optimisé en fonction des besoins de l'administration. Il est possible de personnaliser le menu du backoffice dans Publik.
Cela permettra de simplifier l'accès aux fonctionnalités les plus utilisées par les agents en fonction de leur(s) rôle(s).

### Prérequis

- Avoir un compte administrateur fonctionnel sur Publik
- Être à même de modifier le contenu des portails, des pages, de définir des rôles et la visibilité des pages et contenu en fonction de ces derniers.

### Procédure

Je ne vais pas réécrire ici ce qui figure dans [la documentation de Publik à ce sujet](https://doc-publik.entrouvert.com/admin-fonctionnel/modifier-le-contenu-des-portails/creer-un-menu-personnalise/#creer-un-menu-personnalise) (pas totalement ou sous une forme légèrement différente). Je vous invite à consulter la documentation officielle de Publik pour plus d'informations.

Sachez simplement qu'il vous faudra créer autant de pages de la portail agent que d'éléments que vous souhaitez voir apparaître dans le menu.

![Pages d'un portail agent dans Publik](/images/personnalisation_menu_publik_apercu_pages_portail_agent.jpg)


Il vous faudra initier une variable système qui activera cette fonction et avoir veillé à définir soigneusement les pages et leur rôle avant de l'activer, sans quoi vous risquez de vous retrouver avec un menu vide.

![Définition de la visibilité et inclusion dans les menus](/images/personnalisation_menu_publik_apercu_paramètres_pages.jpg)
![Variable système pour activer la personnalisation du menu](/images/personnalisation_menu_publik_variable_hobo_a_definir.jpg)



### Ma suggestion en terme d'expérience utilisateur

J'ai choisi de regrouper les éléments différemment et en trois catégories :

* Agents (Saisie, Traitement, Finances, Utilisateurs)
* Studio (Rôles, Formulaires, Workflows, Fiches, Modèles de fiche, Agendas, Édition « Portail agent », Édition « portail citoyen », Statistiques)
* Système (Identités, Services web, Paramètres).

La détail apporté à la définition des rôles et visibilité de page permettre une granularité dans ce qui sera affiché à chaque profil d'agent·e.

### Conclusion

L'optimisation de l'expérience utilisateur est un enjeu majeur pour les administrations. Que ce soit pour les agents ou les usagers, il est important de faciliter l'accès aux fonctionnalités les plus utilisées.

Cela représentera un gain de temps pour les agents avec pour finalité, une meilleure expérience utilisateur de ces derniers, ainsi que par ruissellement, pour les usagers finaux des services d'une administration.


### Références
[Modifier le contenu des portails (documentation officielle Publik)](https://doc-publik.entrouvert.com/admin-fonctionnel/modifier-le-contenu-des-portails/creer-un-menu-personnalise/#creer-un-menu-personnalise)
[Personnaliser le menu du backoffice dans Publik](https://doc-publik.entrouvert.com/admin-fonctionnel/modifier-le-contenu-des-portails/creer-un-menu-personnalise/#creer-un-menu-personnalise)