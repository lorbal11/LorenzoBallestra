Ballestra Lorenzo
Delattre Mathys

# Alignment free - TP 2

On utilise une approche kmers pour comparer 5 génomes bactériens de manière rapide en échantillonnant 50000 kmers par génomes pour les comparaisons.

On commence par utiliser une table de hashage pour stocker les kmers retenus:

Concernant l'optimisation du code présent dans les fichiers annexes (mainTP2_hash.py), son exécution prends 23s et un espace mémoire maximal de 135896 kilobytes, réduisant ainsi le temps et l'espace par rapport à la comparaisons des sets de kmers complets.
![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/5faa7ed5-a20c-47af-9b17-679b801a2872)

Concernant les résultats, les disctances de jaccards obtenues permettent de dessiner la matrice suivante :
 ![matrixbact_hash](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/fa936f90-9939-4a47-b0ca-e73bde71af0a)

Celle-ci est similaire à celle trouvée lors de la comparaison des sets complets. Notamment, elle permet de retrouver les mêmes conclusions en termes de relation entre espèces bactériennes.

Ensuite nous répétons ce procédé d'échantillonage en utilisant des heapq :

Concernant l'optimisation du code présent dans les fichiers annexes (mainTP2_heap.py), son exécution prends 20s et un espace mémoire maximal de 135852 kilobytes, réduisant ainsi le temps et l'espace par rapport à la comparaisons des sets de kmers complets.
![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/16dd33e8-f80b-4918-b76c-47333ded6c7e)

Concernant les résultats, les disctances de jaccards obtenues permettent de dessiner la matrice suivante :
![matrixbact_heap](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/1fc39f88-9ade-487a-9088-cc91da72b0f9)

Celle-ci est similaire à celle trouvée lors de la comparaison des sets complets. Notamment, elle permet de retrouver les mêmes conclusions en termes de relation entre espèces bactériennes.

Finalement en comparant les deux approches on constate que du point de vue de l'optimisation elles ont des performances très similaires même si la méthode faisant recours à des heapq est légèrement plus rapide tandis que du point de vue des résultats elles donnent des bonnes approximations des distances entre génomes même si les résultats obtenus avec la méthode heapq se rapprochent légèrement plus des résultats obtenus en utilisant tous les kmers par rapport à la méthode utilisant des tables de hashage.
