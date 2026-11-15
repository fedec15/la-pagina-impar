#!/usr/bin/env python3
"""Revisa el encabezado de cada texto y cada libro antes de publicar.

Uso: python3 scripts/verificar_textos.py
Sale con código 1 si encuentra errores (y el control de GitHub falla).
"""
import datetime
import pathlib
import re
import sys

import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*(\n|\Z)", re.S)

errores, avisos = [], []


def leer(ruta):
    texto = ruta.read_text(encoding="utf-8")
    m = FM.match(texto)
    if not m:
        errores.append(f"{ruta.relative_to(RAIZ)}: no empieza con un encabezado entre líneas '---'.")
        return None
    try:
        datos = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        linea = getattr(e, "context_mark", None) or getattr(e, "problem_mark", None)
        donde = f" (línea {linea.line + 2} del archivo)" if linea else ""
        errores.append(
            f"{ruta.relative_to(RAIZ)}: el encabezado no se puede leer{donde}. "
            "Si un valor ocupa varias líneas, usá '|' y dos espacios de sangría; "
            "si tiene ':' o empieza con comillas o '*', ponelo entre comillas."
        )
        return None
    if not isinstance(datos, dict):
        errores.append(f"{ruta.relative_to(RAIZ)}: el encabezado no tiene el formato 'campo: valor'.")
        return None
    return datos


categorias = {c["slug"] for c in yaml.safe_load((RAIZ / "_data/categorias.yml").read_text(encoding="utf-8"))}
libros = {p.stem for p in (RAIZ / "_libros").glob("*.md")}
hoy = datetime.date.today()

for ruta in sorted((RAIZ / "_textos").glob("*")):
    nombre = ruta.relative_to(RAIZ)
    if ruta.suffix != ".md":
        avisos.append(f"{nombre}: no termina en .md, no se va a publicar.")
        continue
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ruta.stem):
        errores.append(f"{nombre}: el nombre del archivo debe tener solo minúsculas, números y guiones (sin tildes, ñ ni espacios).")
    d = leer(ruta)
    if d is None:
        continue
    if d.get("published") is False:
        avisos.append(f"{nombre}: es un borrador (published: false), no se publica.")
        continue
    for campo in ("title", "category", "date"):
        if not d.get(campo):
            errores.append(f"{nombre}: falta '{campo}'.")
    cat = d.get("category")
    if cat and cat not in categorias:
        errores.append(f"{nombre}: category '{cat}' no existe. Opciones: {', '.join(sorted(categorias))}.")
    fecha = d.get("date")
    if fecha:
        if isinstance(fecha, datetime.datetime):
            fecha = fecha.date()
        if not isinstance(fecha, datetime.date):
            errores.append(f"{nombre}: date '{fecha}' no es una fecha válida (formato AAAA-MM-DD).")
        elif fecha > hoy:
            avisos.append(f"{nombre}: date {fecha} es futura; el texto no aparece hasta esa fecha.")
    anio = d.get("year")
    if anio is not None and not (isinstance(anio, int) and 1900 <= anio <= hoy.year + 1):
        errores.append(f"{nombre}: year '{anio}' debe ser un año de cuatro cifras.")
    libro = d.get("libro")
    if libro and libro not in libros:
        errores.append(f"{nombre}: libro '{libro}' no existe en _libros/.")

for ruta in sorted((RAIZ / "_libros").glob("*.md")):
    d = leer(ruta)
    if d is not None and not d.get("title"):
        errores.append(f"{ruta.relative_to(RAIZ)}: falta 'title'.")

for a in avisos:
    print(f"::warning::{a}" if "GITHUB_ACTIONS" in __import__("os").environ else f"Aviso: {a}")
for e in errores:
    print(f"::error::{e}" if "GITHUB_ACTIONS" in __import__("os").environ else f"Error: {e}")

if errores:
    print(f"\n{len(errores)} error(es). Corregilos antes de publicar.")
    sys.exit(1)
print("Todos los textos están bien.")
