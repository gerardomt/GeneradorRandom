#!/usr/bin/env python3

"""
API para trabajar con la generación de números random
"""


import random


def genera_entero_random(lim_inf, lim_sup):
    """Devuelve un número al azar entre lim_inf y lim_sup incluyendo ambos
    números

    """
    return random.randint(lim_inf, lim_sup)


def choose_from_list(rows):
    return random.choice(rows)
