Ce projet simule la gestion d'un hôtel, intégrant plusieurs classes (Hôtel, Chambre, Client, Réservation) en utilisant la programmation orientée objet en SQL et python. L'application permet de gérer les chambres, les réservations et les clients d'un hôtel, tout en offrant un suivi des disponibilités et des réservations effectuées.

## Fonctionnalités principales

- **Gestion des hôtels** : Chaque hôtel a un nom, une adresse, un nombre d'étoiles, et une liste de chambres.
- **Gestion des chambres** : Les chambres ont un numéro, un prix, une disponibilité et équipées de Wi-Fi.
- **Gestion des clients** : Un client a un nom, un prénom, un téléphone et une date de naissance.
- **Gestion des réservations** : Un client peut effectuer des réservations de chambres sur une période donnée.
- **Affichage des réservations** : Les réservations des clients et des hôtels peuvent être affichées avec le montant total à payer.

## Classes

1. **Hotel** : Gère les informations et la liste des chambres, ainsi que les réservations associées à l'hôtel.
2. **Chambre** : Représente une chambre d'hôtel avec son prix, son statut (disponible ou réservé) et services (Wi-Fi).
3. **Client** : Représente un client avec ses coordonnées et ses réservations.
4. **Reservation** : Gère les réservations d'une chambre par un client sur une période définie.

## Technologies utilisées

- pyhton
- SQL 