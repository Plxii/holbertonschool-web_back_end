# 🌀 Python - Async Comprehension

## 📘 Description

Ce projet explore les **compréhensions asynchrones** en Python, une fonctionnalité puissante introduite avec `async for` et les générateurs asynchrones. Elle permet de traiter des flux de données asynchrones de manière élégante et efficace.

---

## 🚀 Objectifs

- Comprendre les générateurs asynchrones (`async def`, `yield`)
- Utiliser `async for` pour consommer des données asynchrones
- Implémenter des **list comprehensions** asynchrones
- Gérer la concurrence avec `asyncio`

---

## 🧠 Concepts clés

### 🔹 Générateur asynchrone

```python
import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

