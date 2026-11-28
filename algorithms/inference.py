"""Punto 5. Inferencia mediante encadenamiento hacia adelante."""
from models.logic import match_premises, substitute


def forward_chain(kb):
    """Retorna una tupla con los hechos originales y derivados, sin duplicados.

    Cada ronda usa los hechos disponibles al comenzarla. La base de entrada
    debe conservarse.
    kb.facts contiene objetos Atom; kb.rules contiene objetos Rule con los
    atributos premises y conclusion. Los hechos se comparan directamente.

    Tips:
    - match_premises(regla.premises, hechos) genera (sustitución, hechos usados).
      Si no hay coincidencias, no genera resultados. La sustitución es un
      diccionario, por ejemplo {'?p': 'ana'}.
    - substitute(regla.conclusion, sustitución) retorna un nuevo objeto Atom
      con las variables reemplazadas por los valores de la sustitución.
    """
    known = list(dict.fromkeys(kb.facts))
    seen = set(known)

    while True:
        snapshot = tuple(known)
        new_facts = []
        for rule in kb.rules:
            for substitution, _used in match_premises(rule.premises, snapshot):
                conclusion = substitute(rule.conclusion, substitution)
                if conclusion not in seen and conclusion not in new_facts:
                    new_facts.append(conclusion)

        if not new_facts:
            break

        for fact in new_facts:
            seen.add(fact)
            known.append(fact)

    return tuple(known)
