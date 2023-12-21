# SAE-Cryptographie

## Sommaire

- [SAE-Cryptographie](#sae-cryptographie)
  - [Sommaire](#sommaire)
  - [Structure du projet](#structure-du-projet)
  - [Exécution des programmes](#exécution-des-programmes)
    - [Jupyter](#jupyter)
    - [Python](#python)
    - [Exécution des expérimentations](#exécution-des-expérimentations)

## Structure du projet

Le projet est composé de 3 dossiers principaux :
- `data` : contient les données utilisées pour les exécutions de base
- `jupyter` : contient les notebooks jupyter eux-mêmes contenant les différents algorithmes
- `python` : contient les fichiers python eux-mêmes contenant les différents algorithmes

Dans les dossiers jupyter et python, on retrouve un notebook `main.ipynb` et un fichier `main.py` qui permettent de lancer les différents algorithmes à la suite et d'afficher les résultats. Ces fichiers utilisent des données de base qui sont contenues dans le dossier `data`, des données générées aléatoirement et des données arbitraires.

## Création d'un environnement virtuel

Pour exécuter les programmes, il est nécessaire de créer un environnement virtuel python. Le fichier `requirements.txt` contient la liste des dépendances nécessaires à l'exécution des programmes.

Pour installer les dépendances, il suffit d'exécuter la commande suivante :
```bash
pip install -r requirements.txt
```

## Exécution des programmes

### Jupyter

Pour exécuter tous les programmes à la suite des différents notebooks jupyter, il suffit de lancer le notebook `main.ipynb` et d'exécuter toutes les cellules.
Sinon, il est possible d'ouvrir les notebooks correspondant à l'algorithme souhaité et d'exécuter les cellules correspondantes en rajoutant les appels de fonctions nécessaires.

### Python

Pour exécuter tous les programmes à la suite des différents fichiers python, il suffit de lancer le fichier `main.py` avec la commande suivante :
```bash
python main.py
```
Sinon, il est possible d'ouvrir les fichiers correspondant à l'algorithme souhaité et d'exécuter les fonctions correspondantes en rajoutant les appels de fonctions nécessaires.

### Exécution des expérimentations

Pour exécuter les expérimentations, il suffit d'exécuter le notebook `experiences.ipynb` ou le fichier `experiences.py` en suivant les mêmes instructions que pour les programmes précédents.
Ces expérimentations permettent de comparer les différents algorithmes entre eux.