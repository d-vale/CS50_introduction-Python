# CS50's Introduction to Programming with Python

[![CS50P](https://img.shields.io/badge/CS50P-Harvard-crimson)](https://cs50.harvard.edu/python/)
[![edX](https://img.shields.io/badge/Platform-edX-blue)](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)
[![Progress](https://img.shields.io/badge/Progress-30%25-yellow)](#progression)

## 📖 À propos

Ce repository documente mon parcours d'apprentissage du cours **CS50P** de Harvard, une introduction à la programmation avec **Python** conçue pour les débutants comme pour ceux ayant déjà une expérience préalable. Ce cours gratuit via edX couvre les fondamentaux de la programmation Python à travers des exercices pratiques, des tests, et du débogage.

### 🎯 Mes objectifs

- Approfondir mes connaissances dans un langage central à l'ère de l'**intelligence artificielle**
- Consolider les bases Python nécessaires à mon **travail de bachelor**
- Comprendre les bonnes pratiques : fonctions, tests unitaires, gestion d'exceptions, POO

## 📚 Programme du cours

### **Week 0 - Functions, Variables** 🐍

Introduction à Python : fonctions, variables, types de données, entrées/sorties, f-strings et premiers programmes.

### **Week 1 - Conditionals** 🔀

Structures conditionnelles, expressions booléennes, correspondance de motifs avec `match`, validation d'entrées utilisateur.

### **Week 2 - Loops** 🔄

Boucles `while` et `for`, listes, compréhensions de listes, dictionnaires, manipulation de chaînes de caractères.

### **Week 3 - Exceptions** ⚠️

Gestion d'erreurs avec `try/except`, exceptions personnalisées, validation robuste des données.

### **Week 4 - Libraries** 📚

Bibliothèques standard et tierces, modules `random`, `statistics`, `sys`, `requests`, API externes, paquets PyPI.

### **Week 5 - Unit Tests** 🧪

Tests unitaires avec `pytest`, bonnes pratiques de test, test-driven development (TDD), couverture de code.

### **Week 6 - File I/O** 📁

Lecture et écriture de fichiers, formats CSV et JSON, bibliothèques `csv` et `PIL`, manipulation de données persistantes.

### **Week 7 - Regular Expressions** 🔍

Expressions régulières avec `re`, validation de formats (email, URL, date), extraction et transformation de texte.

### **Week 8 - Object-Oriented Programming** 🏛️

Classes, instances, méthodes, héritage, opérateurs surchargés, décorateurs `@property` et `@classmethod`.

### **Week 9 - Et Cetera** 🏆

Concepts avancés : `set`, compréhensions, générateurs, itérateurs, lambda, `map`, `filter`, et projet final.

## 📈 Progression

### Statut des semaines

| Semaine    | Sujet                   | Exercices réalisés                                                                                                                                                                                                                     | Statut        |
| ---------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Week 0** | Functions, Variables    | [`indoor.py`](week0/indoor.py), [`playback.py`](week0/playback.py), [`faces.py`](week0/faces.py), [`einstein.py`](week0/einstein.py), [`tip.py`](week0/tip.py)                                                                         | ✅ Terminé    |
| **Week 1** | Conditionals            | [`deep.py`](week1/deep.py), [`bank.py`](week1/bank.py), [`extensions.py`](week1/extensions.py), [`interpreter.py`](week1/interpreter.py), [`meal.py`](week1/meal.py)                                                                   | ✅ Terminé    |
| **Week 2** | Loops                   | [`camel.py`](week2/camel.py), [`coke.py`](week2/coke.py), [`twttr.py`](week2/twttr.py), [`plates.py`](week2/plates.py), [`nutrition.py`](week2/nutrition.py)                                                                          | ✅ Terminé    |
| **Week 3** | Exceptions              | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 4** | Libraries               | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 5** | Unit Tests              | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 6** | File I/O                | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 7** | Regular Expressions     | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 8** | Object-Oriented Prog.   | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |
| **Week 9** | Et Cetera / Final Proj. | _À venir_                                                                                                                                                                                                                              | ⏳ À venir    |

## 🛠️ Détail des exercices

### Week 0 - Functions, Variables

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/0/](https://cs50.harvard.edu/python/2022/psets/0/)

| Exercice           | Description                                                       | Fichier                            | Difficulté |
| ------------------ | ----------------------------------------------------------------- | ---------------------------------- | ---------- |
| **Indoor Voice**   | Convertit une chaîne de caractères en minuscules                  | [`indoor.py`](week0/indoor.py)     | ⭐         |
| **Playback Speed** | Joint les mots d'une phrase avec `...` pour simuler un ralenti    | [`playback.py`](week0/playback.py) | ⭐         |
| **Making Faces**   | Remplace `:)` et `:(` par des emojis 🙂🙁                         | [`faces.py`](week0/faces.py)       | ⭐         |
| **Einstein**       | Calcule l'énergie E=mc² à partir d'une masse donnée               | [`einstein.py`](week0/einstein.py) | ⭐⭐       |
| **Tip Calculator** | Calcule le montant du pourboire selon le repas et le pourcentage  | [`tip.py`](week0/tip.py)           | ⭐⭐       |

### Week 1 - Conditionals

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/1/](https://cs50.harvard.edu/python/2022/psets/1/)

| Exercice                      | Description                                                                | Fichier                                  | Difficulté |
| ----------------------------- | -------------------------------------------------------------------------- | ---------------------------------------- | ---------- |
| **Deep Thought**              | Vérifie si la réponse à "la Grande Question" est 42                        | [`deep.py`](week1/deep.py)               | ⭐         |
| **Home Federal Savings Bank** | Détermine les frais bancaires selon la formule de salutation               | [`bank.py`](week1/bank.py)               | ⭐⭐       |
| **File Extensions**           | Identifie le type MIME d'un fichier d'après son extension                  | [`extensions.py`](week1/extensions.py)   | ⭐⭐       |
| **Math Interpreter**          | Évalue des expressions arithmétiques simples (+, -, *, /)                  | [`interpreter.py`](week1/interpreter.py) | ⭐⭐       |
| **Meal Time**                 | Détecte le repas correspondant à une heure donnée (breakfast/lunch/dinner) | [`meal.py`](week1/meal.py)               | ⭐⭐       |

### Week 2 - Loops

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/2/](https://cs50.harvard.edu/python/2022/psets/2/)

| Exercice            | Description                                                         | Fichier                                  | Difficulté |
| ------------------- | ------------------------------------------------------------------- | ---------------------------------------- | ---------- |
| **camelCase**       | Convertit du snake_case en camelCase                                | [`camel.py`](week2/camel.py)             | ⭐⭐       |
| **Coke Machine**    | Simule un distributeur qui accepte les pièces de monnaie            | [`coke.py`](week2/coke.py)               | ⭐⭐       |
| **twttr**           | Supprime les voyelles d'un texte comme sur Twitter (sms era)        | [`twttr.py`](week2/twttr.py)             | ⭐         |
| **Vanity Plates**   | Valide des plaques d'immatriculation personnalisées selon des règles | [`plates.py`](week2/plates.py)           | ⭐⭐⭐     |
| **Nutrition Facts** | Affiche les calories d'un aliment à partir d'une base de données    | [`nutrition.py`](week2/nutrition.py)     | ⭐       |

### Week 3 - Exceptions

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/3/](https://cs50.harvard.edu/python/2022/psets/3/)

| Exercice              | Description                                                          | Fichier   | Difficulté |
| --------------------- | -------------------------------------------------------------------- | --------- | ---------- |
| **Fuel Gauge**        | Affiche le niveau de carburant en pourcentage avec gestion d'erreurs | _À venir_ | —          |
| **Felipe's Taqueria** | Système de commande d'une taqueria avec gestion des entrées invalides | _À venir_ | —          |
| **Grocery List**      | Gère une liste de courses triée et en majuscules                     | _À venir_ | —          |
| **Outdated**          | Convertit des dates en format ISO 8601 avec validation               | _À venir_ | —          |

### Week 4 - Libraries

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/4/](https://cs50.harvard.edu/python/2022/psets/4/)

| Exercice                | Description                                                        | Fichier   | Difficulté |
| ----------------------- | ------------------------------------------------------------------ | --------- | ---------- |
| **Emojize**             | Convertit des codes texte en emojis avec la bibliothèque `emoji`   | _À venir_ | —          |
| **Frank, Ian and Glen** | Génère du texte en ASCII art avec la bibliothèque `pyfiglet`       | _À venir_ | —          |
| **Adieu, Adieu**        | Formate une liste de noms avec la bonne conjonction grammaticale   | _À venir_ | —          |
| **Guessing Game**       | Jeu de devinette avec `random` et validation des entrées           | _À venir_ | —          |
| **Little Professor**    | Générateur de quiz de maths pour enfants avec `random`             | _À venir_ | —          |
| **Bitcoin Price Index** | Récupère le prix du Bitcoin via l'API CoinDesk avec `requests`     | _À venir_ | —          |

### Week 5 - Unit Tests

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/5/](https://cs50.harvard.edu/python/2022/psets/5/)

| Exercice                         | Description                                                   | Fichier   | Difficulté |
| -------------------------------- | ------------------------------------------------------------- | --------- | ---------- |
| **Testing my twttr**             | Tests unitaires pour le programme de suppression de voyelles  | _À venir_ | —          |
| **Back to the Bank**             | Tests pour le programme de frais bancaires selon la salutation | _À venir_ | —          |
| **Re-requesting a Vanity Plate** | Tests pour la validation des plaques d'immatriculation        | _À venir_ | —          |
| **Refueling**                    | Tests pour le programme de jauge de carburant                 | _À venir_ | —          |

### Week 6 - File I/O

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/6/](https://cs50.harvard.edu/python/2022/psets/6/)

| Exercice          | Description                                                                 | Fichier   | Difficulté |
| ----------------- | --------------------------------------------------------------------------- | --------- | ---------- |
| **Lines of Code** | Compte les lignes de code Python d'un fichier (sans commentaires ni blancs) | _À venir_ | —          |
| **Pizza Py**      | Génère un tableau ASCII d'une carte de pizza à partir d'un CSV              | _À venir_ | —          |
| **Scourgify**     | Reformate un fichier CSV (nom/prénom) vers un nouveau format                | _À venir_ | —          |
| **CS50 P-Shirt**  | Superpose un t-shirt CS50 sur une photo avec `Pillow`                       | _À venir_ | —          |

### Week 7 - Regular Expressions

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/7/](https://cs50.harvard.edu/python/2022/psets/7/)

| Exercice                     | Description                                                           | Fichier   | Difficulté |
| ---------------------------- | --------------------------------------------------------------------- | --------- | ---------- |
| **NUMB3RS**                  | Valide des adresses IPv4 avec des expressions régulières              | _À venir_ | —          |
| **Watch on YouTube**         | Extrait l'URL d'intégration d'une vidéo YouTube depuis un iframe HTML | _À venir_ | —          |
| **Working 9 to 5**           | Valide et convertit des horaires de travail en format standard        | _À venir_ | —          |
| **Regular, um, Expressions** | Supprime les hésitations ("um") d'une phrase avec `re`                | _À venir_ | —          |
| **Response Validation**      | Valide les réponses Oui/Non d'un utilisateur de façon flexible        | _À venir_ | —          |

### Week 8 - Object-Oriented Programming

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/8/](https://cs50.harvard.edu/python/2022/psets/8/)

| Exercice              | Description                                                        | Fichier   | Difficulté |
| --------------------- | ------------------------------------------------------------------ | --------- | ---------- |
| **Seasons of Love**   | Calcule et affiche en lettres le nombre de minutes depuis une date | _À venir_ | —          |
| **Cookie Jar**        | Implémente une classe `Jar` pour gérer un pot à biscuits           | _À venir_ | —          |
| **CS50 Shirtificate** | Génère un PDF personnalisé avec un t-shirt CS50 en utilisant `fpdf2` | _À venir_ | —        |

### Week 9 - Et Cetera / Projet final

**📝 Final Project :** [https://cs50.harvard.edu/python/2022/project/](https://cs50.harvard.edu/python/2022/project/)

| Projet            | Description                         | Repository | Difficulté |
| ----------------- | ----------------------------------- | ---------- | ---------- |
| **Final Project** | Projet personnel Python — À venir   | _À venir_  | —          |

## 🔗 Ressources

- [**Cours CS50P**](https://cs50.harvard.edu/python/) - Site officiel
- [**edX Platform**](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) - Plateforme d'apprentissage
- [**CS50.dev**](https://cs50.dev/) - Environnement de développement cloud
- [**Documentation Python**](https://docs.python.org/3/) - Référence officielle
- [**PyPI**](https://pypi.org/) - Index des bibliothèques Python

## 💡 Compétences développées

### Fondamentaux Python

- **Fonctions et variables** : Définition, arguments, valeurs de retour, portée
- **Types de données** : `str`, `int`, `float`, `bool`, listes, dictionnaires, tuples
- **Entrées/sorties** : `input()`, `print()`, f-strings, formatage
- **Modules** : Import, création et réutilisation de modules

### Structures de contrôle

- **Conditionnelles** : `if/elif/else`, expressions booléennes, `match/case`
- **Boucles** : `while`, `for`, `break`, `continue`, compréhensions de listes
- **Validation d'entrées** : Boucles de validation robuste, gestion des cas limites

### Gestion des erreurs

- **Exceptions** : `try/except/else/finally`, exceptions intégrées Python
- **Exceptions personnalisées** : Création et levée d'exceptions métier
- **Robustesse** : Écriture de code résistant aux entrées invalides

### Bibliothèques et APIs

- **Bibliothèques standard** : `random`, `statistics`, `sys`, `re`, `csv`
- **Bibliothèques tierces** : `requests`, `emoji`, `pyfiglet`, `Pillow`, `fpdf2`
- **APIs REST** : Requêtes HTTP, parsing JSON, intégration de services externes

### Tests unitaires

- **pytest** : Écriture de tests, assertions, organisation des suites de tests
- **Test-Driven Development** : Approche par les tests, couverture de code
- **Régression** : Détection précoce des bugs par les tests automatisés

### Manipulation de fichiers

- **Fichiers texte** : Lecture, écriture, modes d'ouverture
- **CSV** : Parsing et génération avec le module `csv`
- **Images** : Manipulation avec `Pillow` (PIL), composition d'images
- **PDF** : Génération de documents avec `fpdf2`

### Expressions régulières

- **Patterns** : `.`, `*`, `+`, `?`, `[]`, `^`, `$`, groupes de capture
- **Module `re`** : `search`, `match`, `findall`, `sub`, flags
- **Applications** : Validation d'emails, URLs, formats de dates, nettoyage de texte

### Programmation orientée objet

- **Classes et instances** : Attributs, méthodes, `__init__`, `self`
- **Héritage** : Sous-classes, `super()`, polymorphisme
- **Propriétés** : `@property`, getters/setters, encapsulation
- **Méthodes spéciales** : `__str__`, `__repr__`, `__len__`, surcharge d'opérateurs

---

_Dernière mise à jour : Février 2026_
