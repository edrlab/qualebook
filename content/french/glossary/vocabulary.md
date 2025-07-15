---
title: Glossaire 
detail: 
abstract: 
categories: 
description: ""
layout: blog
date: 2024-09-18
---
# Glossaire

## Vocabulaire
<dl>
<dt id="metadata">Métadonnée</dt>
<dd>
Dans le monde de l'édition, il s'agit d'informations détaillées sur le livre qui sont transmises aux partenaires pour leur permettre d'avoir des informations sans disposer du livre. Les métadonnées les plus connues sont le titre et l'auteur.
Dans le cas du livre numérique, ces informations permettent aussi aux dispositifs de lecture de restituer correctement le contenu.
</dd>
<dl>
<dt id="landmarks">Landmarks (points de repère)</dt>
<dd>
Les points de repère sont des endroits clés d'une publication auxquels un utilisateur est susceptible de vouloir accéder rapidement. Ils comprennent la table des matières, les glossaires, les bibliographies et d'autres aides à la navigation et à l'information.

ARIA et EPUB définissent tous deux des méthodes pour exprimer les points de repère&nbsp;:
* Les repères ARIA sont exprimés à l'aide du rôle attibute et n'existent que dans le document dans lequel ils sont définis (voir les repères ARIA pour plus d'informations).
* EPUB utilise une aide à la navigation spéciale dans le document de navigation pour définir où se trouvent les points de repère, car ceux-ci sont généralement répartis dans de nombreux documents (voir les points de repère EPUB pour plus d'informations).
Voir [EPUB 3.3 section 7.4.4 The landmarks nav element](https://www.w3.org/TR/epub-33/#sec-nav-landmarks)
</dd>
<dt id="contentdocument">Content Document (Fichier de contenu)</dt>
<dd>
Un EPUB contient plusieurs dossiers et fichiers. Parmi eux, on appelle fichier de contenu (Content Document) les fichiers XHTML qui contiennent tout ou partie de la publication, c'est-à-dire le texte lui-même et les éventuels appels de ressources (image, audio, vidéo...). Ces fichiers de contenu peuvent être référencés dans le fichier OPF pour être atteignables via le sommaire de l'application de lecture.

Voir [EPUB 3.3 section 6. EPUB content documents](https://www.w3.org/TR/epub-33/#sec-contentdocs).
</dd> 
<dt id="CSS">CSS</dt>
    <dd>Les feuilles de style en cascade (CSS) sont un langage de feuille de style utilisé pour décrire la présentation d'un document écrit en HTML ou en XML (y compris les dialectes XML tels que SVG, MathML ou XHTML). Les CSS décrivent comment les éléments doivent être rendus sur l'écran, sur papier, en audio, ou sur d'autres supports.</dd> 
<dt id="Scripts">Scripts</dt>
    <dd>ensemble d'instructions ou de commandes exécutées par un programme.</dd> 
<dt id="Codesource">Code source</dt>
    <dd>texte brut d'un programme écrit dans un langage de programmation.</dd> 
<dt id="tocncx">Fichier toc.ncx</dt>
    <dd>fichier XML qui définit la table des matières d'un EPUB.</dd> 
<dt id="opf">Fichier opf</dt>
    <dd>fichier XML central d'un EPUB, contenant les métadonnées et la structure du livre.</dd> 
<dt id="Fallback">Fallback (chaîne de repli) (Cf. Règle 026)</dt>
    <dd>contenu alternatif affiché si le contenu principal n'est pas pris en charge ou disponible.</dd> 
<dt id="Repli">Repli intrinsèques (Cf. Règle 026)</dt>
    <dd>mécanisme de repli intégré à un élément HTML ou CSS.</dd> 
<dt id="Minification">Minification (Cf. Règle 067)</dt>
    <dd>processus de suppression des caractères inutiles dans le code source pour réduire la taille des fichiers.</dd> 
<dt id="couverture">Métadonnées de couverture (Cf. Règle 086)</dt>
    <dd>informations descriptives associées à l'image de couverture d'un livre numérique.</dd> 
<dt id="Mediaqueries">Media queries (Cf. Règle 086)</dt>
    <dd>règles CSS qui permettent d'appliquer des styles différents en fonction des caractéristiques de l'appareil (taille d'écran, orientation, etc.).</dd> 
<dt id="Ancre">Ancre (Cf. Règle 059)</dt>
    <dd>lien interne qui renvoie à une section spécifique d'une page.</dd> 
<dt id="balisesemantique">Balise de structuration / balise sémantique (Cf. Règle 058)</dt>
    <dd>balise HTML qui donne un sens au contenu qu'elle englobe (ex: `<header>`, `<article>`, `<footer>`).</dd> 
<dt id="Linearisation">Linéarisation (Cf. Règle 077)</dt>
    <dd>présentation séquentielle du contenu, souvent utilisée pour l'accessibilité ou l'impression.</dd> 
<dt id="Listesdedefinitions">Listes de définitions (Cf. Règle 073)</dt>
    <dd>listes HTML (`<dl>`, `<dt>`, `<dd>`) utilisées pour définir des termes.</dd> 
<dt id="Attributcharset">Attribut charset (jeu de caractères) (Cf. Règles 070 et 071)</dt>
    <dd>attribut spécifiant l'encodage des caractères d'un document HTML.</dd> 
<dt id="Balisemeta">Balise meta (balise de métadonnées) (Cf. Règles 070 et 071)</dt>
    <dd>balise HTML utilisée pour fournir des métadonnées sur la page (description, mots-clés, etc.).</dd> 
<dt id="Dechargementale">Décharge mentale (Cf. Règle 057)</dt>
    <dd>principe de conception visant à réduire la charge cognitive de l'utilisateur.</dd> 
<dt id="Registredessous-tagsdelangue ">Registre des sous-tags de langue (Cf. Règle 036)</dt>
    <dd>liste normalisée des sous-tags utilisés pour spécifier des variantes linguistiques (ex: `fr-CA` pour le français canadien).</dd> 
<dt id="canvas">Éléments canvas (Cf. Règle 026, Règle 023)</dt>
    <dd>élément HTML5 (`<canvas>`) permettant de dessiner des graphiques et des animations via JavaScript.</dd> 
<dt id="Manifest">Manifest (Cf. Règle 026)</dt>
    <dd>fichier JSON ou XML décrivant les ressources d'une application web progressive (PWA).</dd> 
<dt id="Argumentsdesimages">Arguments des images (Cf. Règle 022)</dt>
    <dd>attributs HTML (ex: `alt`, `title`, `width`, `height`) qui fournissent des informations supplémentaires sur une image.</dd> 
<dt id="RolesARIA">Rôles ARIA (Cf. Règle 020)</dt>
    <dd>attributs qui définissent la nature sémantique des éléments HTML, améliorant l'accessibilité pour les technologies d'assistance.</dd> 
<dt id="TypesEPUB">Types EPUB (Cf. Règle 020)</dt>
    <dd>cela signifie qu'il faut spécifier les valeurs ou les options possibles pour l'attribut `epub:type`. En d'autres termes, il s'agit de lister les différentes catégories ou fonctions qu'un élément peut avoir dans un EPUB, en utilisant cet attribut.</dd> 
<dt id="TDM">Text and Data Mining (TDM) (Cf. Règle 017)</dt>
    <dd>techniques d'analyse automatique de grandes quantités de texte et de données.</dd> 
<dt id="XMP">XMP (Extensible Metadata Platform) (Cf. Règle 017)</dt>
    <dd>norme de métadonnées utilisée pour intégrer des informations descriptives dans des fichiers numériques.</dd> 
<dt id="accessibilitysummary">Élément accessibility summary (Cf. Règle 014)</dt>
    <dd>résumé textuel des caractéristiques d'accessibilité d'un document.</dd> 
<dt id="FicheONIX">Fiche ONIX (Cf. Règle 012)</dt>
    <dd>format standardisé d'échange de métadonnées pour l'industrie du livre.</dd> 
<dt id="Tooltip">Tooltip (Cf. Règle 007)</dt>
    <dd>petit texte d'aide qui apparaît lorsque l'utilisateur survole un élément.</dd> 

    <!-- 
    <dt id=""></dt>
    <dd></dd> 
    -->

</dl>


## Référentiels

* [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/)
     * ["[Web Content Accessibility Guidelines (WCAG) 1.3.1 Info and Relationships Level A](https://www.w3.org/TR/WCAG22/#info-and-relationships)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 1.1.1 Non-text Content (Level A)](https://www.w3.org/TR/WCAG22/#non-text-content)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 2.5.8  Target Size (Minimum) (Level AA)](https://www.w3.org/TR/WCAG22/#target-size-minimum)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 1.3.2 Meaningful Sequence (Level A)](https://www.w3.org/TR/WCAG22/#meaningful-sequence)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 1.3.3 Sensory Characteristics (Level A)](https://www.w3.org/TR/WCAG22/#sensory-characteristics)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 1.4.3 Contrast (Minimum) (Level AA)](https://www.w3.org/TR/WCAG22/#contrast-minimum)"]
     * ["[Web Content Accessibility Guidelines (WCAG)  1.4.1 Use of Color (Level A)](https://www.w3.org/TR/WCAG22/#use-of-color)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 3.2.3 Consistent Navigation (Level AA)](https://www.w3.org/TR/WCAG22/#consistent-navigation)"]
     * ["[Web Content Accessibility Guidelines (WCAG) Keyboard Accessible ](https://www.w3.org/TR/WCAG22/#keyboard-accessible)"]
     * ["[Web Content Accessibility Guidelines (WCAG)  (Level A)]()"]
     * ["[Web Content Accessibility Guidelines (WCAG) (Level A)]()"]
     * ["[Web Content Accessibility Guidelines (WCAG)  (Level A)]()"]
     * ["[Web Content Accessibility Guidelines (WCAG) (Level A)]()"]
     * ["[Web Content Accessibility Guidelines (WCAG)  (Level A)]()"]
     * ["[Web Content Accessibility Guidelines (WCAG) 2.4.4 Link Purpose (In Context) (Level A)](https://www.w3.org/TR/WCAG22/#link-purpose-in-context)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 3.1.2 Language of Parts (Level A)](https://www.w3.org/TR/WCAG22/#language-of-parts)"]
     * ["[Web Content Accessibility Guidelines (WCAG) 3.1.1 Language of Page (Level A)](https://www.w3.org/TR/WCAG22/#language-of-page)"]

     
*  ["[HTML5 Specification](https://html.spec.whatwg.org/)", 
* "[Extensible Markup Language (XML)](https://www.w3.org/TR/xml/)"]

* [EPUB Type and ARIA Role Authoring guide](https://w3c.github.io/epub-specs/epub33/epub-aria-authoring/)
* [EPUB Accessibility 1.1](https://www.w3.org/TR/epub-a11y-11/)
* [EPUB 3 Specification](https://www.w3.org/publishing/epub3/)

* [Dublin Core Metadata Initiative (DCMI)](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)

* [TDM Reservation Protocol (TDMRep)](https://w3c.github.io/cg-reports/tdmrep/CG-FINAL-tdmrep-20240510/)

* ONIX
  * [liste 196, code 51](https://ns.editeur.org/onix/en/196/51)
  * [liste 196, code 52](https://ns.editeur.org/onix/en/196/52)

* [Web Sustainability Guidelines (WSG)](https://w3c.github.io/sustyweb/#minify-your-html-css-and-javascript"), 

* [Référentiel général de l’écoconception des services numériques](https://www.arcep.fr/uploads/tx_gspublication/consultation-referentiel-ecoconception-services-numeriques_091023.pdf) 