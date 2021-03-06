# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb

def salvar(firstname, lastname, sex, country, state, city, address, zipcode, phone, email, password):
    curso = Curso(firstname=firstname, lastname=lastname, sex=sex, country=country, state=state, city=city,
                  address=address, zipcode=zipcode, phone=phone, email=email, password=password)
    curso.put()

def listar(_resp):
    query = Curso.query().order(-Curso.firstname, -Curso.lastname, -Curso.sex, -Curso.country, -Curso.state,
                                -Curso.city, -Curso.address, -Curso.zipcode, -Curso.phone, -Curso.email,
                                -Curso.password)

    def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

    lista_de_cursos = [to_dict(c) for c in query.fetch()]
    lista_de_cursos = json.dumps(lista_de_cursos)
    _resp.write(lista_de_cursos)