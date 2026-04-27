# CS50's Introduction to Programming with Python

[![CS50P](https://img.shields.io/badge/CS50P-Harvard-crimson)](https://cs50.harvard.edu/python/)
[![edX](https://img.shields.io/badge/Platform-edX-blue)](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python)
[![Progress](https://img.shields.io/badge/Progress-100%25-brightgreen)](#progression)

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
| **Week 3** | Exceptions              | [`fuel.py`](week3/fuel.py), [`taqueria.py`](week3/taqueria.py), [`grocery.py`](week3/grocery.py), [`outdated.py`](week3/outdated.py)                                                                                                   | ✅ Terminé    |
| **Week 4** | Libraries               | [`emojize.py`](week4/emojize.py), [`figlet.py`](week4/figlet.py), [`adieu.py`](week4/adieu.py), [`game.py`](week4/game.py), [`professor.py`](week4/professor.py), [`bitcoin.py`](week4/bitcoin.py)                                    | ✅ Terminé    |
| **Week 5** | Unit Tests              | [`test_twttr.py`](week5/test_twttr/test_twttr.py), [`test_bank.py`](week5/test_bank/test_bank.py), [`test_plates.py`](week5/test_plates/test_plates.py), [`test_fuel.py`](week5/test_fuel/test_fuel.py)                               | ✅ Terminé    |
| **Week 6** | File I/O                | [`lines.py`](week6/lines.py), [`pizza.py`](week6/pizza.py), [`scourgify.py`](week6/scourgify.py), [`shirt.py`](week6/shirt.py)                                                                                                        | ✅ Terminé    |
| **Week 7** | Regular Expressions     | [`numb3rs.py`](week7/numb3rs/numb3rs.py), [`watch.py`](week7/watch/watch.py), [`working.py`](week7/working/working.py), [`um.py`](week7/um/um.py), [`response.py`](week7/response/response.py)                                        | ✅ Terminé    |
| **Week 8** | Object-Oriented Prog.   | [`seasons.py`](week8/seasons/seasons.py), [`jar.py`](week8/jar/jar.py), [`shirtificate.py`](week8/shirtificate/shirtificate.py)                                                                                                        | ✅ Terminé    |
| **Week 9** | Et Cetera / Final Proj. | [`project.py`](week9/project.py), [`test_project.py`](week9/test_project.py), package [`immoscope/`](week9/immoscope/)                                                                                                                 | ✅ Terminé    |

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

| Exercice              | Description                                                          | Fichier                                    | Difficulté |
| --------------------- | -------------------------------------------------------------------- | ------------------------------------------ | ---------- |
| **Fuel Gauge**        | Affiche le niveau de carburant en pourcentage avec gestion d'erreurs | [`fuel.py`](week3/fuel.py)                 | ⭐⭐       |
| **Felipe's Taqueria** | Système de commande d'une taqueria avec gestion des entrées invalides | [`taqueria.py`](week3/taqueria.py)         | ⭐⭐       |
| **Grocery List**      | Gère une liste de courses triée et en majuscules                     | [`grocery.py`](week3/grocery.py)           | ⭐         |
| **Outdated**          | Convertit des dates en format ISO 8601 avec validation               | [`outdated.py`](week3/outdated.py)         | ⭐⭐⭐     |

### Week 4 - Libraries

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/4/](https://cs50.harvard.edu/python/2022/psets/4/)

| Exercice                | Description                                                        | Fichier                                      | Difficulté |
| ----------------------- | ------------------------------------------------------------------ | -------------------------------------------- | ---------- |
| **Emojize**             | Convertit des codes texte en emojis avec la bibliothèque `emoji`   | [`emojize.py`](week4/emojize.py)             | ⭐         |
| **Frank, Ian and Glen** | Génère du texte en ASCII art avec la bibliothèque `pyfiglet`       | [`figlet.py`](week4/figlet.py)               | ⭐⭐       |
| **Adieu, Adieu**        | Formate une liste de noms avec la bonne conjonction grammaticale   | [`adieu.py`](week4/adieu.py)                 | ⭐⭐       |
| **Guessing Game**       | Jeu de devinette avec `random` et validation des entrées           | [`game.py`](week4/game.py)                   | ⭐⭐       |
| **Little Professor**    | Générateur de quiz de maths pour enfants avec `random`             | [`professor.py`](week4/professor.py)         | ⭐⭐⭐     |
| **Bitcoin Price Index** | Récupère le prix du Bitcoin via une API externe avec `requests`    | [`bitcoin.py`](week4/bitcoin.py)             | ⭐⭐⭐     |

### Week 5 - Unit Tests

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/5/](https://cs50.harvard.edu/python/2022/psets/5/)

| Exercice                         | Description                                                    | Fichier                                                    | Difficulté |
| -------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- | ---------- |
| **Testing my twttr**             | Tests unitaires pour le programme de suppression de voyelles   | [`test_twttr.py`](week5/test_twttr/test_twttr.py)         | ⭐       |
| **Back to the Bank**             | Tests pour le programme de frais bancaires selon la salutation | [`test_bank.py`](week5/test_bank/test_bank.py)            | ⭐       |
| **Re-requesting a Vanity Plate** | Tests pour la validation des plaques d'immatriculation         | [`test_plates.py`](week5/test_plates/test_plates.py)      | ⭐     |
| **Refueling**                    | Tests pour le programme de jauge de carburant                  | [`test_fuel.py`](week5/test_fuel/test_fuel.py)            | ⭐       |

### Week 6 - File I/O

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/6/](https://cs50.harvard.edu/python/2022/psets/6/)

| Exercice          | Description                                                                 | Fichier   | Difficulté |
| ----------------- | --------------------------------------------------------------------------- | --------- | ---------- |
| **Lines of Code** | Compte les lignes de code Python d'un fichier (sans commentaires ni blancs) | [`lines.py`](week6/lines.py)       | ⭐⭐       |
| **Pizza Py**      | Génère un tableau ASCII d'une carte de pizza à partir d'un CSV              | [`pizza.py`](week6/pizza.py)       | ⭐⭐       |
| **Scourgify**     | Reformate un fichier CSV (nom/prénom) vers un nouveau format                | [`scourgify.py`](week6/scourgify.py) | ⭐⭐     |
| **CS50 P-Shirt**  | Superpose un t-shirt CS50 sur une photo avec `Pillow`                       | [`shirt.py`](week6/shirt.py)       | ⭐⭐⭐     |

### Week 7 - Regular Expressions

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/7/](https://cs50.harvard.edu/python/2022/psets/7/)

| Exercice                     | Description                                                           | Fichier                                                          | Difficulté |
| ---------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------- |
| **NUMB3RS**                  | Valide des adresses IPv4 avec des expressions régulières              | [`numb3rs.py`](week7/numb3rs/numb3rs.py)                        | ⭐⭐       |
| **Watch on YouTube**         | Extrait l'URL d'intégration d'une vidéo YouTube depuis un iframe HTML | [`watch.py`](week7/watch/watch.py)                               | ⭐⭐       |
| **Working 9 to 5**           | Valide et convertit des horaires de travail en format standard        | [`working.py`](week7/working/working.py)                         | ⭐⭐⭐     |
| **Regular, um, Expressions** | Supprime les hésitations ("um") d'une phrase avec `re`                | [`um.py`](week7/um/um.py)                                        | ⭐⭐       |
| **Response Validation**      | Valide les réponses Oui/Non d'un utilisateur de façon flexible        | [`response.py`](week7/response/response.py)                      | ⭐         |

### Week 8 - Object-Oriented Programming

**📝 Problem Set :** [https://cs50.harvard.edu/python/2022/psets/8/](https://cs50.harvard.edu/python/2022/psets/8/)

| Exercice              | Description                                                          | Fichier                                                                | Difficulté |
| --------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- |
| **Seasons of Love**   | Calcule et affiche en lettres le nombre de minutes depuis une date   | [`seasons.py`](week8/seasons/seasons.py)                               | ⭐⭐⭐     |
| **Cookie Jar**        | Implémente une classe `Jar` pour gérer un pot à biscuits             | [`jar.py`](week8/jar/jar.py)                                           | ⭐⭐       |
| **CS50 Shirtificate** | Génère un certificat PDF personnalisé avec `fpdf2`                   | [`shirtificate.py`](week8/shirtificate/shirtificate.py)                | ⭐⭐       |

### Week 9 - Et Cetera / Projet final

**📝 Final Project :** [https://cs50.harvard.edu/python/2022/project/](https://cs50.harvard.edu/python/2022/project/)

| Projet            | Description                                                                                                                  | Fichier                                  | Difficulté |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ---------- |
| **ImmoScope**     | Outil d'analyse de portefeuille immobilier (KPI financiers, détection d'anomalies, dashboard `rich` et rapport PDF)          | [`week9/`](week9/)                       | ⭐⭐⭐⭐   |

#### 🏢 ImmoScope — analyse de portefeuille immobilier suisse

ImmoScope est un outil en ligne de commande qui analyse un portefeuille immobilier exporté
depuis l'ERP **Quorum** (format Excel multi-feuilles), calcule les KPI financiers utiles aux
régies, détecte les anomalies et produit à la fois un **dashboard terminal** coloré et un
**rapport PDF** prêt à archiver.

Le projet répond à un besoin réel rencontré dans le cadre de mon **travail de bachelor** chez
**Bobst Régie Immobilière** (Yverdon-les-Bains) : remplacer une analyse manuelle longue et
sujette aux erreurs par un script reproductible en moins de trois secondes.

**🎬 Vidéo de démonstration :** disponible sur demande — contactez-moi en privé.

**Fonctionnalités clés**

- **Ingestion** Excel multi-feuilles (Immeubles / Lots / Baux / Transactions) avec validation de schéma (`pandas` + `openpyxl`)
- **KPI** : revenus annuels, NOI, rendements brut/net, taux de vacance, loyer moyen au m² par ville, classements top/bottom des immeubles
- **Détection d'anomalies** : loyer sous le marché, charges excessives, vacance prolongée, loyer mensuel manquant — avec validation regex des identifiants de lot (`^LOT-\d{3}-\d{2}$`)
- **Dashboard terminal** rendu avec `rich` (panneaux, tableaux, codes couleurs par sévérité)
- **Rapport PDF** paginé avec `reportlab` + `matplotlib` (page de garde, synthèse, graphiques, tableau d'anomalies)
- **Formatage suisse** des montants (`CHF 1'850.00`)
- **Données de démo** générées avec `faker` (anomalies plantées) pour permettre une exécution sans données réelles

**Démarrage rapide**

```bash
cd week9
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Génère un portefeuille de démo
python project.py --generate-sample data/portfolio_demo.xlsx

# Lance l'analyse complète (dashboard + PDF)
python project.py data/portfolio_demo.xlsx

# Tests unitaires
pytest -v
```

📚 Documentation détaillée : [`week9/README.md`](week9/README.md)

## 🔗 Ressources

- [**Cours CS50P**](https://cs50.harvard.edu/python/) - Site officiel
- [**edX Platform**](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python) - Plateforme d'apprentissage
- [**CS50.dev**](https://cs50.dev/) - Environnement de développement cloud
- [**Documentation Python**](https://docs.pyt