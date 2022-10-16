Title: Comment afficher la date et l'heure de façon optimale dans Publik ?
Date: 2022-10-16 15:22
Category: Articles en français · Publik · Le connecteur citoyen
Tags: UX, UI, publik, administrateur fonctionnel, gabarits django, expérience utilisateur
Slug: comment-afficher-la-date-et-l-heure-de-facon-optimale-dans-publik
Author: Daniel Muyshond
Summary: Afficher la date et l'heure de façon plus optimale et lisible dans Publik améliore l'expérience utilisateur
Lang: fr
Translation: false
Status: published

## Comment afficher la date et l'heure de façon optimale dans Publik ?

Publik utilise le format de date et d'heure suivant : `2022-10-16 15:25:00`. C'est un format qui est utilisé par les développeurs et qui est facile à trier. Cependant, ce format n'est pas très lisible pour les utilisateurs. Il est donc préférable de l'afficher de façon plus optimale et lisible.

### Afficher la date et l'heure dans un gabarit Django


Dans un gabarit Django, il est possible d'afficher la date et l'heure de façon plus optimale et lisible. Par exemple, pour afficher la date et l'heure de la variable `form_var_date` issue d'un formulaire, il suffit d'utiliser le filtre `|date` de Django :

    Votre rendez vous à été confirmé le `{{ form_workflow_data_reservation_response_datetime|date:"l d F"}}` à `{{ form_workflow_data_reservation_response_datetime|date:"G\hH"}}`.

### Signification des valeurs de formatage passées au filtre `|date`

Le filtre `|date:"l d F"` appliqué à une variable permet d'afficher la date en français (exemple : dimanche 16 octobre).

Le filtre `|date:"G\hH"` permet d'afficher l'heure à la française (exemple : 13h30).

Vous avez un profil de technicien et vous souhaitez connaître le pourquoi du comment ? Retrouvez le détail du filtre `|date` dans la documentation de Django, dans les références de cet article (en bas de la page, après la conclusion).

## Conclusion

Appliquer cette astuce [dans un mail](https://doc-publik.entrouvert.com/admin-fonctionnel/fabrique-de-workflows/les-actions-de-workflow/elements_envoyer-un-email/#envoyer-un-courriel), [une action de workflow « Alerte »](https://doc-publik.entrouvert.com/admin-fonctionnel/fabrique-de-workflows/les-actions-de-workflow/elements_afficher-un-message/#alerte) ou un une [action de workflow « Message dans l'historique »](https://doc-publik.entrouvert.com/admin-fonctionnel/fabrique-de-workflows/les-actions-de-workflow/elements_enregistrer-dans-le-journal/#enregistrer-un-message-dans-lhistorique) permet de rendre l'expérience utilisateur plus agréable pour les utilisateurs, que ce soit les administrateurs ou les citoyens.

Une expérience utilisateur soignée et optimale est un facteur clé de succès pour tout projet de numérisation de processus.

### Références
* [Publik, le connecteur citoyen](https://publik.entrouvert.com/)
* [Documentation de Publik · Utiliser les filtres](https://doc-publik.entrouvert.com/admin-fonctionnel/parametrage-avance/utiliser-les-filtres/#utiliser-les-filtres)
* [Documentation de Publik · Filtre sur les dates](https://doc-publik.entrouvert.com/admin-fonctionnel/parametrage-avance/utiliser-les-filtres/#filtres-sur-les-dates)
* [Documentation Django : Filtre date](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#date)
