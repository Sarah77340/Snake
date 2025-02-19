# Snake - Clone du jeu classique

Ce projet consiste à recréer une version améliorée du jeu **Snake** en Python. Il propose plusieurs **modes de jeu**, un **menu interactif**, ainsi qu’une **progression de la difficulté** à mesure que le joueur avance dans la partie.  

**Objectifs principaux :**
- Reprendre un programme de base `snake.py` et le modifier pour inclure de nouvelles fonctionnalités.
- Ajouter des **modes de jeu avancés** :
  - Mode **classique** : le jeu s'arrête si le serpent touche les bords de l'écran.
  - Mode **arène torique** : en sortant d’un côté de l’écran, le serpent réapparaît de l’autre (comme dans Pac-Man).
  - Mode **multijoueur** : deux joueurs s'affrontent avec des serpents ayant une longueur infinie.
- Intégrer un **système d'obstacles** générés aléatoirement pour ajouter du challenge.
- Implémenter une **accélération progressive** du jeu après un certain score.

---

## Fonctionnalités du jeu

- **Déplacement fluide du serpent** (ne peut pas reculer)  
- **Apparition aléatoire des pommes** (et disparition lorsqu’elles sont mangées)  
- **Augmentation de la taille du serpent** à chaque pomme mangée  
- **Affichage du score en direct** et message de fin de partie  
- **Mode avec obstacles** : fin de partie si le serpent percute un obstacle  
- **Accélération progressive** à partir d'un score de 5  
- **Mode arène torique** : le serpent traverse les bords de l'écran  
- **Mode multijoueur** : deux joueurs peuvent jouer en même temps  
- **Menu interactif** : choix du mode de jeu ou possibilité de quitter  

---

## Documentation utilisateur

### Comment jouer ?
1. **Lancer le jeu** (`python snake.py`)
2. **Naviguer dans le menu** :
   - **Jouer (mode classique)** : solo avec règles standards.
   - **Mods** : choisir entre **Arène torique** et **Multijoueur**.
   - **Quitter** : fermer le jeu.
3. **Commandes** :
   - **Joueur 1** (mode solo & multijoueur) : `Flèches directionnelles`  
   - **Joueur 2** (mode multijoueur) : `Z Q S D`
4. **Objectif** : manger **30 pommes** pour gagner ! 
   - Évitez les obstacles.
   - En multijoueur, essayez de faire en sorte que l’adversaire touche votre serpent.

---

## Documentation technique

### Bibliothèques utilisées :
- `random` : Génération des **positions aléatoires** pour les pommes et obstacles.
- `time` : Gestion du **délai** entre les mouvements du serpent.
- `doctest` : Tests unitaires pour vérifier certaines **fonctions**.
- `upemtk` : Création de la **fenêtre graphique**, affichage des éléments du jeu et gestion des **événements clavier**.

### Principales fonctions :
| Fonction                | Rôle |
|-------------------------|------|
| `case_vers_pixel()`     | Convertit des coordonnées **de grille** en **pixels**. |
| `affiche_pommes()`      | Affiche les **pommes** sur la fenêtre. |
| `affiche_serpent()`     | Dessine le **serpent** sur l’écran. |
| `affiche_obstacles()`   | Place les **obstacles** aléatoires. |
| `ajoute_pommes()`       | Génère une nouvelle **pomme** après qu'une ait été mangée. |
| `ajoute_obstacles()`    | Ajoute des **obstacles** au fil du jeu. |
| `change_direction()`    | Modifie la direction du **serpent 1** (flèches). |
| `change_direction_2()`  | Modifie la direction du **serpent 2** (`Z Q S D`). |
| `fonction_serpent()`    | Gère **le déplacement**, la **collision**, l’évolution du **score** et l’application des règles des **différents modes**. |

---

### Prérequis :
- **Python** doit être installé.
- La bibliothèque **upemtk** (bibliothèque académique de l'université Gustave Eiffel) doit être installée.

## Auteurs
- **Mohamed Alla**  
- **Sarah Nguyen**  

---
