
# SAE-Cryptographie

## Partie 1

### Questions :
1. En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout? En vous appuyant sur votre cours, justifiez votre réponse.

    En supposant que le RSA soit utilisé correctement, Eve ne pourra pas en venir à bout. Le chiffrement RSA est un algorithme de cryptographie asymétrique. Cette algorithmie utilise une clé publique pour chiffrer et une clé privée pour déchiffrer. La clé publique est connue de tous et la clé privée est connue uniquement de la personne qui veut déchiffrer le message. La clé publique est calculée à partir de la clé privée. Il est donc impossible de retrouver la clé privée à partir de la clé publique. Les seules façons de retrouver la clé privée sont de tester toutes les clés possibles ou de la demander à la personne qui la possède. Pour tester toutes les clés possibles, il faudrait énormément de temps car le nombre de clés possibles est très élévé.


2. En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai nécessaire à une méthode “force brute” pour retrouver la clé.

    L'algorithme symétrique SDES est très peu sécurisé, car il utilise une clé très courte de 10 bits. Celui-ci a essentiellement pour but éducatif et non pas pour être utilisé dans un contexte réel. Comme cette algorithme utilise une clé de 10 bits, ce qui signifie qu'il y a 2^10 clés possibles. Cela représente 1024 clés possibles. La méthode "force brute" consiste à tester toutes les clés possibles. Il faudrait donc 1024 essais pour retrouver la clé, ce qui est très peu pour un algorithme de chiffrement. La moyenne de temps pour trouver la clé est de 512 essais. De plus, le nombre de tours de l'algorithme est de 2, ce qui est peu pour un algorithme de chiffrement, par comparaison, l'algorithme DES (le non simplifié) utilise 16 tour.

3. Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal? Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé.

    Le double SDES est en théorie plus sécurisé que le SDES, car il utilise deux clés de 10 bits. Cela signifie qu'il y a 2^10 puis 2^10 clés possibles, ce qui représente 2^20 clés possibles. La méthode "force brute" consiste à tester toutes les clés possibles. Il faudrait donc 2^20 essais au maximum pour retrouver les deux clés, ce qui est certes plus que le SDES, mais cela reste très peu pour un algorithme de chiffrement. Une méthode astucieuse pour retrouver les deux clés est d'avoir le message déchiffré et le message chiffré avec le double SDES. Il suffit ensuite de tester toutes les clés possibles sur le message déchiffré et de tester toutes les clés possibles sur le message chiffré avec le double SDES. Si les deux résultats sont identiques, alors il s'agit des deux clés utilisées pour le double SDES.