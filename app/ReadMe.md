# Synth - Mus3325 - Mode d'emploie

Projet dans le cadre du cours MUS3325, il s'agit d'un petit logiciel qui simplifie l'accès à un clavier midi via pyo, permettant d'appliquer différents instruments, différents effets et en activant les controles de leurs paramètres sur les controleurs midi du clavier.

### Ressource utiliser
python 2
debian 9 - Stretch
les librairie python :
*	pyo
*	WxPython

### Installation

Assurez-vous d'ajuster les PATH dans les fichiers main.py et Synth/synth.py.
main.py devrait importer les fichiers Synth/synth.py et GUI/gui2.py.
Synth/synth.py devrait importer les fichiers Synth/Instrument/instrument.py et Synth/Effect/effect.py

Si vous demarrez via E-Pyo sur un ordinateur sous linux, le chemin ne devrait que légèrement différer.

Ajustez les controleurs recquis si vous les connaissez déjà dans Synth/synth.py. par defaut , l'ensemble est vide.


## Demarrage

Pour démarrer, simplement exécuter le fichier main.py et appuyer sur le bouton 

```
Start/Stop
```

### Ce que ca fait

Le bouton 

```
Pause/Resume
```

permet de mettre en pause l'exécution de la sortie. 

Le menu défilant qui se trouve juste en dessous permet de sélectionner à tout moment la source primaire.

Juste en dessous, on trouve les controles generaux : le volume d'entrée, le volume de sortie, et 3 filtres: un passe haut un passe bas et un passe bande.

En dessous,encore une fois, un controleur stereo.

Chaque controle fonctionne de la facon suivante : un slider pour selectionner la valeur désirée, un menue défilant pour choisir un controleur à assigner et un checkbox pour indiquer si oui ou non il est assigné.

Le bouton
```
Refresh inputs
```
qui se trouve en dessous permet de recuperer les inputs ajouter apres l'ouverture de l'application. Si vous ne connaissez pas vos controleurs MIDIs, une fois demarré, vous devrez les deplacer pour qu'il senregistre, puis vous pourrez les reccuperer en appyant sur ce bouton.

Au centre ce trouvent les controles d'ajout d'effet.
Vous devez d'abord selectionner un effet dans le menu défilant. Par la suite, si vous voulez donner un nom personnalisé a l'effet, vous pouvez l'indiquer dans la section name. Ensuite, si cet effet n'est pas le premier que vous ajoutez, vous avez le choix entre : 

* L'ajouter comme premier effet, soit juste apres la source
* L'ajouter comme dernier effet, soit juste avant la sortie
* L'ajouter entre deux autres effets en position i en selectionnant sa position avec 0 étant le plus près de la source 

Finalement, pour chacun des effets que vous aurez ajoutés, il vous sera possible de modifier leur paramtre ou de leur assigner un controleur MIDI via l'onglet MyEffect. En selectionnant l'un des effets dans le menue défilant, le paramèètre disponnible s'affiche. En tout temps, il vous sera possible de retirer un effet non desirez en appuyant sur le bouton

```
Remove
```

L'effet selectionner sera l'effet supprimé.


### Fichier necessaire

Les fichiers : 
* main.py
* GUI/gui2.py
* Synth/synth.py
* Synth/Instrument/instrument.py
* Synth/Effect/effect.py


### info

Vous pouvez me contacter via mon couriel 
vincent.g.beauregard@umontreal.ca
ou
vincentgb48@hotmail.ca

Vincent G. Beauregard
Matricule : 20034236
