<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="generator" content="Docutils 0.13.1: http://docutils.sourceforge.net/" />
<title></title>
<style type="text/css">

/*
:Author: David Goodger (goodger@python.org)
:Id: $Id: html4css1.css 7952 2016-07-26 18:15:59Z milde $
:Copyright: This stylesheet has been placed in the public domain.

Default cascading style sheet for the HTML output of Docutils.

See http://docutils.sf.net/docs/howto/html-stylesheets.html for how to
customize this style sheet.
*/

/* used to remove borders from tables and images */
.borderless, table.borderless td, table.borderless th {
  border: 0 }

table.borderless td, table.borderless th {
  /* Override padding for "table.docutils td" with "! important".
     The right padding separates the table cells. */
  padding: 0 0.5em 0 0 ! important }

.first {
  /* Override more specific margin styles with "! important". */
  margin-top: 0 ! important }

.last, .with-subtitle {
  margin-bottom: 0 ! important }

.hidden {
  display: none }

.subscript {
  vertical-align: sub;
  font-size: smaller }

.superscript {
  vertical-align: super;
  font-size: smaller }

a.toc-backref {
  text-decoration: none ;
  color: black }

blockquote.epigraph {
  margin: 2em 5em ; }

dl.docutils dd {
  margin-bottom: 0.5em }

object[type="image/svg+xml"], object[type="application/x-shockwave-flash"] {
  overflow: hidden;
}

/* Uncomment (and remove this text!) to get bold-faced definition list terms
dl.docutils dt {
  font-weight: bold }
*/

div.abstract {
  margin: 2em 5em }

div.abstract p.topic-title {
  font-weight: bold ;
  text-align: center }

div.admonition, div.attention, div.caution, div.danger, div.error,
div.hint, div.important, div.note, div.tip, div.warning {
  margin: 2em ;
  border: medium outset ;
  padding: 1em }

div.admonition p.admonition-title, div.hint p.admonition-title,
div.important p.admonition-title, div.note p.admonition-title,
div.tip p.admonition-title {
  font-weight: bold ;
  font-family: sans-serif }

div.attention p.admonition-title, div.caution p.admonition-title,
div.danger p.admonition-title, div.error p.admonition-title,
div.warning p.admonition-title, .code .error {
  color: red ;
  font-weight: bold ;
  font-family: sans-serif }

/* Uncomment (and remove this text!) to get reduced vertical space in
   compound paragraphs.
div.compound .compound-first, div.compound .compound-middle {
  margin-bottom: 0.5em }

div.compound .compound-last, div.compound .compound-middle {
  margin-top: 0.5em }
*/

div.dedication {
  margin: 2em 5em ;
  text-align: center ;
  font-style: italic }

div.dedication p.topic-title {
  font-weight: bold ;
  font-style: normal }

div.figure {
  margin-left: 2em ;
  margin-right: 2em }

div.footer, div.header {
  clear: both;
  font-size: smaller }

div.line-block {
  display: block ;
  margin-top: 1em ;
  margin-bottom: 1em }

div.line-block div.line-block {
  margin-top: 0 ;
  margin-bottom: 0 ;
  margin-left: 1.5em }

div.sidebar {
  margin: 0 0 0.5em 1em ;
  border: medium outset ;
  padding: 1em ;
  background-color: #ffffee ;
  width: 40% ;
  float: right ;
  clear: right }

div.sidebar p.rubric {
  font-family: sans-serif ;
  font-size: medium }

div.system-messages {
  margin: 5em }

div.system-messages h1 {
  color: red }

div.system-message {
  border: medium outset ;
  padding: 1em }

div.system-message p.system-message-title {
  color: red ;
  font-weight: bold }

div.topic {
  margin: 2em }

h1.section-subtitle, h2.section-subtitle, h3.section-subtitle,
h4.section-subtitle, h5.section-subtitle, h6.section-subtitle {
  margin-top: 0.4em }

h1.title {
  text-align: center }

h2.subtitle {
  text-align: center }

hr.docutils {
  width: 75% }

img.align-left, .figure.align-left, object.align-left, table.align-left {
  clear: left ;
  float: left ;
  margin-right: 1em }

img.align-right, .figure.align-right, object.align-right, table.align-right {
  clear: right ;
  float: right ;
  margin-left: 1em }

img.align-center, .figure.align-center, object.align-center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}

table.align-center {
  margin-left: auto;
  margin-right: auto;
}

.align-left {
  text-align: left }

.align-center {
  clear: both ;
  text-align: center }

.align-right {
  text-align: right }

/* reset inner alignment in figures */
div.align-right {
  text-align: inherit }

/* div.align-center * { */
/*   text-align: left } */

.align-top    {
  vertical-align: top }

.align-middle {
  vertical-align: middle }

.align-bottom {
  vertical-align: bottom }

ol.simple, ul.simple {
  margin-bottom: 1em }

ol.arabic {
  list-style: decimal }

ol.loweralpha {
  list-style: lower-alpha }

ol.upperalpha {
  list-style: upper-alpha }

ol.lowerroman {
  list-style: lower-roman }

ol.upperroman {
  list-style: upper-roman }

p.attribution {
  text-align: right ;
  margin-left: 50% }

p.caption {
  font-style: italic }

p.credits {
  font-style: italic ;
  font-size: smaller }

p.label {
  white-space: nowrap }

p.rubric {
  font-weight: bold ;
  font-size: larger ;
  color: maroon ;
  text-align: center }

p.sidebar-title {
  font-family: sans-serif ;
  font-weight: bold ;
  font-size: larger }

p.sidebar-subtitle {
  font-family: sans-serif ;
  font-weight: bold }

p.topic-title {
  font-weight: bold }

pre.address {
  margin-bottom: 0 ;
  margin-top: 0 ;
  font: inherit }

pre.literal-block, pre.doctest-block, pre.math, pre.code {
  margin-left: 2em ;
  margin-right: 2em }

pre.code .ln { color: grey; } /* line numbers */
pre.code, code { background-color: #eeeeee }
pre.code .comment, code .comment { color: #5C6576 }
pre.code .keyword, code .keyword { color: #3B0D06; font-weight: bold }
pre.code .literal.string, code .literal.string { color: #0C5404 }
pre.code .name.builtin, code .name.builtin { color: #352B84 }
pre.code .deleted, code .deleted { background-color: #DEB0A1}
pre.code .inserted, code .inserted { background-color: #A3D289}

span.classifier {
  font-family: sans-serif ;
  font-style: oblique }

span.classifier-delimiter {
  font-family: sans-serif ;
  font-weight: bold }

span.interpreted {
  font-family: sans-serif }

span.option {
  white-space: nowrap }

span.pre {
  white-space: pre }

span.problematic {
  color: red }

span.section-subtitle {
  /* font-size relative to parent (h1..h6 element) */
  font-size: 80% }

table.citation {
  border-left: solid 1px gray;
  margin-left: 1px }

table.docinfo {
  margin: 2em 4em }

table.docutils {
  margin-top: 0.5em ;
  margin-bottom: 0.5em }

table.footnote {
  border-left: solid 1px black;
  margin-left: 1px }

table.docutils td, table.docutils th,
table.docinfo td, table.docinfo th {
  padding-left: 0.5em ;
  padding-right: 0.5em ;
  vertical-align: top }

table.docutils th.field-name, table.docinfo th.docinfo-name {
  font-weight: bold ;
  text-align: left ;
  white-space: nowrap ;
  padding-left: 0 }

/* "booktabs" style (no vertical lines) */
table.docutils.booktabs {
  border: 0px;
  border-top: 2px solid;
  border-bottom: 2px solid;
  border-collapse: collapse;
}
table.docutils.booktabs * {
  border: 0px;
}
table.docutils.booktabs th {
  border-bottom: thin solid;
  text-align: left;
}

h1 tt.docutils, h2 tt.docutils, h3 tt.docutils,
h4 tt.docutils, h5 tt.docutils, h6 tt.docutils {
  font-size: 100% }

ul.auto-toc {
  list-style-type: none }

</style>
</head>
<body>
<div class="document">


<p>import numpy as np
import math
from PIL import Image
from scipy import interpolate
from scipy import stats
from PIL import ImageOps
import cv2
import list
import threading
# import pyopencl as cl</p>
<dl class="docutils">
<dt>def echantillonageRadial(image, beamNumber, pxPerBeam, angle, height, dmin, dmax):</dt>
<dd><p class="first">longeur, largeur = image.size
image = list(image.getdata())
image = [image[i * largeur:(i + 1) * largeur] for i in range(longeur)]
# Base sortie
imageSortie = np.zeros((longeur, largeur))
i = (3 * math.pi - angle) / 2
while i &lt; (3 * math.pi + angle) / 2:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 20)</p>
Unexpected indentation.</div>
<blockquote>
<p>j = dmin
while j &lt; dmax:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 22)</p>
Unexpected indentation.</div>
<blockquote>
<p>x = j * math.cos(i) + largeur / 2
y = -j * math.sin(i) + height
x = int(x)
y = int(y)
imageSortie[x][y] = image[x][y]</p>
<p>j += (((3 * math.pi + angle) / 2) - ((3 * math.pi - angle) / 2)) / (pxPerBeam - 1)</p>
</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 29)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>i += (dmax - dmin) / (beamNumber - 1)</p>
</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 30)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p class="last">return imageSortie</p>
</dd>
<dt>def echantillonageRect(npimage, longeur, largeur, nbPointAbscisse, nbpointOrdonnee):</dt>
<dd><p class="first"># Image base sortie :
imageSortie = np.ones((longeur, largeur))-2
y = 0
while y &lt; largeur:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 38)</p>
Unexpected indentation.</div>
<blockquote>
<p>x=0
while x &lt; longeur:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 40)</p>
Unexpected indentation.</div>
<blockquote>
imageSortie[int(x)][int(y)] = npimage[int(x)][int(y)]
x += largeur</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 42)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>y += longeur/ nbpointOrdonnee</p>
</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 43)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p class="last">return imageSortie</p>
</dd>
<dt>def echantillonageRect2(npimage,nbPoint):</dt>
<dd><p class="first">&quot;&quot;&quot;</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field"><th class="field-name">param npimage:</th><td class="field-body">Image Ã&nbsp; echantilloner en format numpy</td>
</tr>
<tr class="field"><th class="field-name">param nbPoint:</th><td class="field-body">Ratio des points que l'on veut garder : 1 sur nbpoint</td>
</tr>
<tr class="field"><th class="field-name">return:</th><td class="field-body">Image echantillonÃ©e sous forme de tableau numpy</td>
</tr>
</tbody>
</table>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 52)</p>
Field list ends without a blank line; unexpected unindent.</div>
<p>&quot;&quot;&quot;
longeur,largeur = npimage.shape
y = 0
while y &lt; int(largeur/nbPoint):</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 56)</p>
Unexpected indentation.</div>
<blockquote>
<p>again = 1
while again &lt; nbPoint:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 58)</p>
Unexpected indentation.</div>
<blockquote>
npimage = np.delete(npimage,(y),axis=1)
again += 1</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 60)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>y += 1</p>
</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 61)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>x = 0
while x &lt; int(longeur/nbPoint):</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 63)</p>
Unexpected indentation.</div>
<blockquote>
<p>again = 1
while again &lt; nbPoint:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 65)</p>
Unexpected indentation.</div>
<blockquote>
npimage = np.delete(npimage,(x),axis=0)
again += 1</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 67)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>x += 1</p>
</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 68)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p class="last">return npimage</p>
</dd>
<dt>def AjoutSpeckel( img, borneInf, borneSup, ecartTypeGauss, u):</dt>
<dd><p class="first">longeur,largeur = img.shape
#matrices de vecteurs gaussiens
beta = 8
alpha = 1.98
# matrixGauss = stats.gennorm.rvs(beta,scale=alpha,loc=0,size=longeur*longeur*u).reshape(longeur, largeur, u)
# matrixGauss2 =  stats.gennorm.rvs(beta,scale=alpha,loc=0,size=longeur*longeur*u).reshape(longeur, largeur, u)
# matrixGauss = (stats.levy_stable_gen.rvs(alpha, 0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
# matrixGauss2 = (stats.levy_stable_gen.rvs(alpha,0,size = longeur*largeur*u,scale=gama).reshape(longeur, largeur, u))
matrixGauss = np.random.randn(longeur * largeur, u).reshape(longeur, largeur, u)
matrixGauss2 = np.random.randn(longeur * largeur, u).reshape(longeur, largeur, u)
imgRetour = np.sqrt(img + 0j)
i = 0
while i &lt; u-1:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 85)</p>
Unexpected indentation.</div>
<blockquote>
imgRetour += (matrixGauss[:,:,i]) + (matrixGauss2[:,:,i]*1j)
i += 1</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 87)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p class="last">img = np.square(imgRetour.real) + np.square(imgRetour.imag)
return img</p>
</dd>
<dt>def interpolation(img):</dt>
<dd>&quot;&quot;&quot;
Interpolation bicubique
:param img: Image Ã&nbsp; interpoler sous forme de tableau numpy
:return: Fonction d'interpoaltion de l'image
&quot;&quot;&quot;
img = np.zeros(img.shape) + img
l,L = img.shape
x = np.arange(0,l,1)
y = np.arange(0, L, 1)
X,Y = np.meshgrid(x,y)
fonctionInter = interpolate.interp2d(x,y,img, kind='cubic')
return fonctionInter</dd>
<dt>def construireImageInterpelee(function,l,L,nbPoint):</dt>
<dd>&quot;&quot;&quot;
Reconstruit une image grÃ¢ce Ã&nbsp; une RÂ² -&gt; R
:param function: Une fonction de RÂ² dans R
:param l: Longeur de l'image voulu
:param L: Largeur de l'image voulu
:param nbPoint: Nombre de point Ã&nbsp; interpoler
:return: Un tableau numpy bidimentionnel reprÃ©sentant une image
&quot;&quot;&quot;
x = np.arange(0, l/nbPoint,1/nbPoint)
y = np.arange(0, L/nbPoint,1/nbPoint)
img = function(x,y)
return img</dd>
<dt>def AjoutBruit(image):</dt>
<dd><p class="first">&quot;&quot;&quot;
Fonction principale appelant les mÃ©thodes permettant d'ajouter un bruit de peckel Ã&nbsp; image de type optique</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field"><th class="field-name">param image:</th><td class="field-body">Une image provenant de la bibliothÃ¨que &quot;PIL Image&quot;</td>
</tr>
<tr class="field"><th class="field-name">return:</th><td class="field-body">Un tableau bidimentionel numpy reprÃ©sentant une image</td>
</tr>
</tbody>
</table>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 126)</p>
Field list ends without a blank line; unexpected unindent.</div>
<p class="last">&quot;&quot;&quot;
# conversion de l'image en array numpy
nbPoint = 2
l,L = image.shape
img = echantillonageRect2(image,nbPoint)
img4 = AjoutSpeckel(img, 1,1 , 0.2,3)
img5 = interpolation(img4)
img5 = construireImageInterpelee(img5,l,L,nbPoint)
return img5</p>
</dd>
<dt>def AjoutBruitMultiThreah():</dt>
<dd>&quot;&quot;&quot;
Produit plusieurs threads permettant d'utiliser tous les coeurs pour l'ajout du bruit de speckel
:return: Void
&quot;&quot;&quot;
img = cv2.imread(&quot;images/vador.bmp&quot;)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
t1 = threading.Thread(target=multipleImage,args=(img,1))
t2 = threading.Thread(target=multipleImage,args=(img,2))
t3 = threading.Thread(target=multipleImage,args=(img,3))
t4 = threading.Thread(target=multipleImage,args=(img,4))
t5 = threading.Thread(target=multipleImage,args=(img,5))
t6 = threading.Thread(target=multipleImage,args=(img,6))
t7 = threading.Thread(target=multipleImage,args=(img,7))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
return 0;</dd>
<dt>def multipleImage(img,p):</dt>
<dd><p class="first">it = 0
while it &lt; 10:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 164)</p>
Unexpected indentation.</div>
<blockquote class="last">
<p>print(it)
img2 = AjoutBruit(img)
img3 = Image.fromarray(img2).</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 167)</p>
Unexpected indentation.</div>
<blockquote>
save(&quot;imgT1It%sP%s&quot;%(it,p),&quot;gif&quot;)</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 168)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>it += 1</p>
</blockquote>
</dd>
<dt>def trouveAlphaGama():</dt>
<dd><p class="first">img = cv2.imread(&quot;images/01_d_3.bmp&quot;)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
l,L = img.shape
y = -1
somme = 0
sommeC = 0
cpt = 0
a = [0]
while y &lt; L-1:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 180)</p>
Unexpected indentation.</div>
<blockquote>
<p>y +=1
x = -1
while x &lt; l-1:</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 183)</p>
Unexpected indentation.</div>
<blockquote>
<p>print(x,y)
x += 1
if ( img</p>
<div class="system-message">
<p class="system-message-title">System Message: ERROR/3 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 186)</p>
Unexpected indentation.</div>
<blockquote>
<blockquote>
[x][y] != 0):</blockquote>
<div class="system-message">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 187)</p>
Block quote ends without a blank line; unexpected unindent.</div>
<p>a.append(img[x][y])</p>
</blockquote>
</blockquote>
</blockquote>
<p class="last">print(a)
esp = np.mean(a,dtype=np.float64)
var = np.var(a,dtype=np.float64)
alpha = np.sqrt(np.square(math.pi)/(6*var))
gama = math.exp( alpha * (esp - math.log(2,10) - 0.577215664901532860606512090082402431042159335939923598805*((1/alpha)-1) ))
print(esp,var,alpha,gama)</p>
</dd>
</dl>
<p># MAIN
img = cv2.imread(&quot;images/fg1.bmp&quot;)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
AjoutBruit(img)</p>
<p># # GPU
# # creer un contexte
# myContext = cl.create_some_context()
# # creer une file de commandes
# myQueue = cl.CommandQueue(myContext)
# # allouer et initialiser la memoire du device
# inputData = np.random.rand(50000).astype(np.float32)
# outputData = np.empty_like(inputData)
# myFlags = cl.mem_flags
# inputBuffer = cl.Buffer(myContext,
# myFlags.READ_ONLY | myFlags.COPY_HOST_PTR, hostbuf=inputData)
# outputBuffer = cl.Buffer(myContext, myFlags.WRITE_ONLY, inputData.nbytes)
# # charger et compiler le kernel
# myProgram = cl.Program(myContext,
# &quot;&quot;&quot;__kernel void add42(__global const float <a href="#id1"><span class="problematic" id="id2">*</span></a>data, __global float <a href="#id3"><span class="problematic" id="id4">*</span></a>result){int gid = get_global_id(0);result[gid] = data[gid] + 42.f;}&quot;&quot;&quot;).build()
# # ajouter le kernel dans la file de commandes
# # recuperer les donnees dans la memoire du device
# myProgram.add42(myQueue, inputData.shape,None, inputBuffer, outputBuffer)
# cl.enqueue_copy(myQueue, outputData, outputBuffer)
# # verifier le resultat du calcul
# if abs(np.linalg.norm(outputData - (inputData + 42))) &lt; 1e-6 :
#     print(&quot;passed&quot;)
# else:
#     print(&quot;failed&quot;)
#</p>
<div class="system-message" id="id1">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 201); <em><a href="#id2">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
<div class="system-message" id="id3">
<p class="system-message-title">System Message: WARNING/2 (<tt class="docutils">C:\Users\polch_000\PycharmProjects\digiSimul\AjoutBruit.py</tt>, line 201); <em><a href="#id4">backlink</a></em></p>
Inline emphasis start-string without end-string.</div>
</div>
</body>
</html>
