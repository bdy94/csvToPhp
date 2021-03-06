# csvToPhp
Function CSV => ARRAY

Entrez un fichier local ou une url, retourne un array.

ex:

test.csv = 

"Boisson","Viande","Divers"
"Lait","Poulet","Brosse à dent"
"Eau","Bœuf","Dentifrice"

csvToArray('test.csv');

Array
(
    [0] => Array
        (
            [Boisson] => Lait
            [Viande] => Poulet
            [Divers] => Brosse à dent 
        )

    [1] => Array
        (
            [Boisson] => Eau
            [Viande] => Bœuf
            [Divers] => Dentifrice
        )

)
