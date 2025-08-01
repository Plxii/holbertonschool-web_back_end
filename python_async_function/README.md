# ⚡ Python – Async

📘 Introduction

La programmation asynchrone permet d’exécuter plusieurs tâches concurrentes sans bloquer l’exécution du programme. Elle est idéale pour les opérations I/O-bound comme les requêtes réseau, les accès disque, ou les appels API.

Python introduit l’asynchrone avec les mots-clés async et await, basés sur le module asyncio.

## 🧠 Pourquoi utiliser l’asynchrone ?

✅ Meilleure performance pour les tâches I/O

✅ Réduction du temps d’attente

✅ Meilleure scalabilité pour les serveurs web ou les bots

✅ Plus simple à lire que les callbacks ou les threads

## 🧪 Syntaxe de base

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())


## 🔄 Exécuter plusieurs coroutines

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay}s")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )

asyncio.run(main())
asyncio.gather() permet d’exécuter plusieurs coroutines en parallèle.

## 🧵 Différence entre sync et async
Aspect		Synchrone		Asynchrone
Exécution	Bloquante		Non bloquante
Concurrence	Threads/processus	Coroutines
Complexité	Simple mais lent	Plus rapide mais nécessite async
Idéal pour	CPU-bound		I/O-bound
