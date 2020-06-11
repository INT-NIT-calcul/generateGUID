#!/usr/bin/python
# -*- coding: utf-8 -*-

from generateGUID.strip_accents import text_to_id, format_age
import hashlib
import re

def generate_GUID(keyInput, truncate = 12):
    keygood = text_to_id(keyInput)
    GUID = hashlib.sha256(keygood.encode('utf-8')).hexdigest()

    if truncate < len(GUID):
        GUID = GUID[:truncate]
    return GUID

# flake8: noqa: C901
def generate_GUID2(nom, prenom, age, sexe):
        age = format_age(age)
        key = nom + prenom + age + sexe
        return generate_GUID(key)

