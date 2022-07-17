#!/usr/bin/env python3

"""
Facade desing pattern that provides a simplified version of the build-in pyton library, random
"""

import random


def genera_entero_random(lim_inf, lim_sup):
    """Devuelve un número al azar entre lim_inf y lim_sup incluyendo ambos
    números
    """
    return random.randint(lim_inf, lim_sup)


def choose_from_list(rows):
    """Return a random element from rows
    """
    return random.choice(rows)
