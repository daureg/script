#! /usr/bin/python2
# vim: set fileencoding=utf-8
# pylint: disable=C0103
"""Lit un fichier de configuration et crée le document latex correspondant"""
import subprocess as sp
def get_source(project_name):
    """Récupère les sources sur github dans le dossier 'project_name'"""
    cmd = "git clone git@github.com:daureg/texplate.git {}".format(project_name)
    sp.call(cmd, shell=True)

import ConfigParser as cp
def read_config(filename=None):
    """Lit les options dans 'filename' ou "info.cfg" par défaut."""
    safe = cp.SafeConfigParser()
    if (filename == None):
        filename = "info.cfg"

    safe.read(filename)
    #os.remove(filename)
    return safe

def sed(filename, avant, apres, pattern=None):
    """Change 'avant' en 'apres' dans 'filename' avec la commande sed,
    éventuellement pour les seules lignes qui contiennent 'pattern'."""
    if (pattern != None):
        pattern = "/{}/ ".format(pattern)
    else:
        pattern = ""

    apres = apres.replace('\\', '\\\\\\')
    apres = apres.replace('"', '\\"')
    cmd = """sed -i "{}s/{}/{}/g" {}""".format(pattern, avant, apres, filename)
    sp.call(cmd, shell=True)

def auteurs(config, latex=True):
    """Prend le fichier de config et renvoie une liste d'auteurs sous forme
    approprié pour Latex ou pdfauthor."""
    plain = config.get('info', 'auteurs')
    aut = [i.strip() for i in plain.split('&')]
    res = []
    for auteur in aut:
        nom = auteur.split(',')[0].strip()
        prenom = auteur.split(',')[1].strip()
        if latex:
            nom = "\\bsc{%s}" % nom

        res.append(prenom + " " + nom)

    if latex:
        return " \\and ".join(res)
    else:
        return ", ".join(res)

def mots_cles(config):
    """Retourne la liste formatée des mots clés dans 'config'"""
    keywords = ["{%s, }" % i.strip() for i in \
                config.get('info', 'mots_cles').split(',')]
    keywords[-1] = keywords[-1].replace(", ", "")
    return "".join(keywords)

def get(config, option):
    """Renvoie une option dans le config parser"""
    return config.get("info", option).strip()

import sys, os
if __name__ == "__main__":
    conf = read_config(None if len(sys.argv)<=1 else sys.argv[1])
    if (conf.getboolean("info", "from_git")):
        get_source(get(conf, "nom"))
        os.chdir(get(conf, "nom"))

    titre = get(conf, "titre")
    ptitre = get(conf, "titre_simple")
    sed("info.tex", "PTITRE", ptitre)
    sed("info.tex", "TITRE", titre)
    if (len(ptitre) < 40):
        sed("header.tex", "FTITRE", titre)
    else:
        sed("header.tex", "FTITRE", "")

    sed("info.tex", "SUBJECT", get(conf, "sujet"))
    sed("info.tex", "KEYS", mots_cles(conf))
    sed("info.tex", "PAUTHORS", auteurs(conf, False))
    sed("info.tex", "AUTHORS", auteurs(conf))
    sed("header.tex", "FAUTHORS", auteurs(conf).split("\\and")[0].strip())

    gloss = conf.getboolean("info", "gloss")
    bib = conf.getboolean("info", "biblio")

    if not (gloss or bib):
        sed("rapport.tex", "^\\\\\\appendix", "%&")

    if not bib:
        sed("rapport.tex", "^", "%", "%biblio")

    sed("rapport.tex", "%biblio", "")

    if not gloss:
        sed("rapport.tex", "^", "%", "%gloss")

    sed("rapport.tex", "%gloss", "")



