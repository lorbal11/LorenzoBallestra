Ballestra Lorenzo
Delattre Mathys

# Alignment free - TP 1

On utilise une approche kmers pour comparer 5 génomes bactériens de manière rapide.
Concernant l'optimisation du code présent dans les fichiers annexes, son exécution prends 93s et un espace mémoire maximal de 482280 kilobytes.
![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/d4702199-4f36-4c4e-ac52-6c00902e36f9)

Concernant les résultats, on obtient les disctances suivante entre les 5 génomes :

GCF_000006945.2_ASM694v2_genomic.fna GCF_008244785.1_ASM824478v1_genomic.fna 0.9377564127983907
GCF_000006945.2_ASM694v2_genomic.fna GCF_014892695.1_ASM1489269v1_genomic.fna 0.0017591971757668513
GCF_000006945.2_ASM694v2_genomic.fna GCF_020526745.1_ASM2052674v1_genomic.fna 0.019091889920944443
GCF_000006945.2_ASM694v2_genomic.fna GCF_020535205.1_ASM2053520v1_genomic.fna 0.01791173059511927
GCF_008244785.1_ASM824478v1_genomic.fna GCF_014892695.1_ASM1489269v1_genomic.fna 0.00176801912767907
GCF_008244785.1_ASM824478v1_genomic.fna GCF_020526745.1_ASM2052674v1_genomic.fna 0.019325578624672622
GCF_008244785.1_ASM824478v1_genomic.fna GCF_020535205.1_ASM2053520v1_genomic.fna 0.01801460961272788
GCF_014892695.1_ASM1489269v1_genomic.fna GCF_020526745.1_ASM2052674v1_genomic.fna 0.0019466253653915354
GCF_014892695.1_ASM1489269v1_genomic.fna GCF_020535205.1_ASM2053520v1_genomic.fna 0.0039007084501784146
GCF_020526745.1_ASM2052674v1_genomic.fna GCF_020535205.1_ASM2053520v1_genomic.fna 0.6139027671100382

qu'on résume dans la matrice de distaces suivante :
 ![image](https://github.com/lorbal11/LorenzoBallestra/assets/150147653/4173e5ea-0604-4acd-90f7-e9aac2525f98)

En observant les distances obtenues, on peut dire que les génomes des bactéries GCF_008244785.1_ASM824478v1 et GCF_000006945.2_ASM694v2 sont très proches, ces 2 bactéries ont probablement un ancêtre commun proche. D'autre par les bactéries GCF_020526745.1_ASM2052674v1 et GCF_020535205.1_ASM2053520v1 sont aussi relativement proches et devrait avoir un ancêtre commun plus récent qu'avec les 3 autres bactéries. Enfin la bactérie GCF_014892695.1_ASM1489269v1 semble être très distante des 4 autres bactéries.



