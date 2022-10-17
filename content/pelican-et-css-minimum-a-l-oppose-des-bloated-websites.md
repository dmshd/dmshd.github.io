Title: Pelican et CSS minimum à l'opposé des bloated websites
Date: 2020-10-17 21:02
Category: Les États
status: draft

Je ne sais pas si vous connaissez ou avez déjà employé Pelican  https://docs.getpelican.com/en/latest/ 
J'aime beaucoup ce générateur de sites statiques. On peut héberger un site gratuitement sur GitHub Pages avec.
C'est un peu "pain in the ass" pour assembler tous les morceaux et avoir un process fluide (build en local, push sur une branch gh-pages, avoir un CNAME qui ne disparait pas pour un custom domain (autre chose que [wathever].github.io. Mais une fois que tout est setup, c'est top !
C'est en python, mais au final la rédaction se fera en Markdown ou RST.
Le statique assure un score de dingue dans les audits lighthouse et donc on part déjà gagnants pour le référencement !

J'ai combiné ça avec le thème par défaut nettoyé de tout le superflu en CSS, un vieux thème de 2009 par Smashing Magazine... J'y ai greffé les 200 bytes de CSS mentionnés ici : https://chat.imio.be/imio/pl/gxsgbnxzxpny885wq5ktx6xnhy
Et le résultat est top, à l'extrême opposé de ce qui est bloated websites, et ça c'est cool.