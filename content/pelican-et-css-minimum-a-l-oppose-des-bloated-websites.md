Title: Pelican et CSS minimum à l'opposé des bloated websites
Tags: python, ssg, pelican, css, article en français, GitHug Pages, SEO, référencement, impavide, impavi.de, héberger son site internet gratuitement en 2022
Slug: pelican-et-css-minimum-a-l-oppose-des-bloated-websites
Author: Daniel Muyshond
Summary: J'ai hébergé ce site statique gratuitement à l'aide de Pelican et GitHub Pages. J'utilise un CSS minimum pour ne pas avoir un site bloated.
Date: 2020-10-17 21:02
Category: Les états « Dan » (états d'âme) (blog)
lang: fr
status: Published
Translation: false

# Pelican et CSS minimum à l'opposé des bloated websites

## Introduction

Je ne sais pas si vous connaissez ou avez déjà employé Pelican  https://docs.getpelican.com/en/latest/
J'aime beaucoup ce générateur de sites statiques. On peut héberger un site gratuitement sur GitHub Pages avec.

## Particularités de Pelican et du setup actuel de ce site

C'est un générateur de sites statiques en Python. Je le build en local et push le résultat sur une branch `gh-pages` de mon repository paramétré pour être employé avec Github Pages. J'ai donc un site statique hébergé gratuitement en 2022, sur Github Pages.

C'est un peu "pain in the ass" pour assembler tous les morceaux et avoir un process fluide (build en local, push sur une branch gh-pages, avoir un CNAME qui ne disparait pas pour un custom domain (autre chose que [wathever].github.io. Mais une fois que tout est setup, c'est top !
C'est en python, mais au final la rédaction se fera en Markdown ou RST.
Le statique assure un score de dingue dans les audits lighthouse et donc on part déjà gagnants pour le référencement !

## CSS Minimum pour un résultat lisible et ultra rapide

J'ai combiné ça avec le thème par défaut nettoyé de tout le superflu en CSS, un vieux thème de 2009 par Smashing Magazine... J'y ai greffé les 200 bytes de CSS mentionnés ici : https://www.swyx.io/css-100-bytes

## Conclusion

Le résultat est top, à l'extrême opposé de ce qui est bloated websites. C'est léger, lisible, ça charge hyper rapidement, et ça c'est cool. J'ai bon espoir d'acquérir à terme un bon positionnement dans Google sur ces articles, grâce, notamment, à la particularité du statique, car je pense que le critère de vitesse de chargement est un critère de référencement important.
