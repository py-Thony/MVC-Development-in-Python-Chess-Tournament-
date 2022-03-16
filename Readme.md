En cours de rédaction

    Un modèle (Model) contient les données à afficher.
    Une vue (View) contient la présentation de l'interface graphique.
    Un contrôleur (Controller) contient la logique concernant les actions effectuées par l'utilisateur.

Modèle
    Élément qui contient les données ainsi que de la logique en rapport avec les données : validation, lecture et enregistrement. Il peut, dans sa forme la plus simple, contenir uniquement une simple valeur, ou une structure de données plus complexe. 
    Le modèle représente l'univers dans lequel s'inscrit l'application.
    Par exemple pour une application de banque, le modèle représente:
        - des comptes, 
        - des clients,
        - les opérations telles que dépôt et retraits,
        - vérifie que les retraits ne dépassent pas la limite de crédit.
Vue
    Partie visible d'une interface graphique. 
    La vue se sert du modèle, et peut être un diagramme, un formulaire, des boutons, etc. 
    Une vue contient des éléments visuels ainsi que la logique nécessaire pour afficher les données provenant du modèle. 
    Dans une application de bureau classique, la vue obtient les données nécessaires à la présentation du modèle en posant des questions. Elle peut également mettre à jour le modèle en envoyant des messages appropriés. 
    Dans une application web une vue contient des balises HTML.
Contrôleur
    Module qui traite les actions de l'utilisateur, modifie les données du modèle et de la vue.Flux de traitement

En résumé, lorsqu'un client envoie une requête à l'application :
    - la requête envoyée depuis la vue est analysée par le contrôleur (via par exemple un handler ou callback).
    - le contrôleur demande au modèle approprié d'effectuer les traitements et notifie à la vue que la requête est traitée.
    - la vue notifiée fait une requête au modèle pour se mettre à jour (par exemple affiche le résultat du traitement via le modèle).

