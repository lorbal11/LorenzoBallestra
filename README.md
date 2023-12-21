Ballestra Lorenzo
Delattre Mathys

# Alignment free - TP 2

On utilise une approche kmers pour comparer 5 génomes bactériens de manière rapide en échantillonnant 50000 kmers par génomes pour les comparaisons.
Concernant l'optimisation du code présent dans les fichiers annexes, son exécution prends 21s et un espace mémoire maximal de 135836 kilobytes, réduisant ainsi le temps et l'espace par rapport à la comparaisons des sets de kmers complets.
![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/ba2392fb-1f51-4cbc-881b-c9efb81f7519)


Concernant les résultats, les disctances de jaccards obtenues permettent de dessiner la matrice suivante :

 ![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/4173e5ea-0604-4acd-90f7-e9aac2525f98)

En observant les distances obtenues, on peut dire que les génomes des bactéries GCF_008244785.1_ASM824478v1 et GCF_000006945.2_ASM694v2 sont très proches, ces 2 bactéries ont probablement un ancêtre commun proche. D'autre par les bactéries GCF_020526745.1_ASM2052674v1 et GCF_020535205.1_ASM2053520v1 sont aussi relativement proches et devrait avoir un ancêtre commun plus récent qu'avec les 3 autres bactéries. Enfin la bactérie GCF_014892695.1_ASM1489269v1 semble être très distante des 4 autres bactéries.



