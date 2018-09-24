# Fill image frame

This scripts achieves the _contrary_ of the "Scale to Frame Size" for image frames: it makes an image fill the frame on the _smaller_ side.

This is the same as doing manually:

- charge l'image dans le cadre
- mise à l'échelle, sans garder les proportions
- échelle libre
- copier la plus grande des valeurs (x-scale / y-scale)
- verrouiller le cadenas sur la droite (pour garder les proportions entre les valeurs)
- coller la plus grande des valeurs (si nécessaire)

ensuite (si nécessaire):

- double clique sur l'image pour positionner "correctement" le portrait
- corriger le x-pos ou y-pos pour qu'il soit zéro (pas de bandes blanches sur le côté qui ne déborde pas)
