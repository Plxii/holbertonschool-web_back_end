# 🐍 Python – Variable Annotations

📘 Introduction

Les annotations de variables en Python permettent d’indiquer le type attendu d’une variable sans imposer de vérification stricte. Elles sont principalement utilisées pour améliorer la lisibilité du code, faciliter l’auto-complétion, et permettre des outils comme mypy ou Pyright de faire de l’analyse statique.

Introduites avec PEP 526, les annotations sont disponibles depuis Python 3.6.

## 🧠 Pourquoi utiliser les annotations ?

✅ Meilleure documentation du code

✅ Aide à la détection d’erreurs avec des outils de type-checking

✅ Facilite la collaboration dans les projets

✅ Compatible avec les IDE modernes pour l’auto-complétion

## 🧪 Syntaxe de base

age: int = 25
name: str = "Alice"
height: float
is_active: bool = True


## 🧰 Typage avancé avec typing

Pour des structures plus complexes, on utilise le module typing.

from typing import List, Dict, Tuple, Optional, Union

names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
coordinates: Tuple[float, float] = (48.8566, 2.3522)
nickname: Optional[str] = None
value: Union[int, float] = 3.14


## 🧬 Fonctions avec annotations

def greet(name: str) -> str:
    return f"Hello, {name}"


