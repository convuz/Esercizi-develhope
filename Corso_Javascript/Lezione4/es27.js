// # Esercizio 27
 
// - Stampa in console tutti i numeri pari da 0 a 20.

// Suggerimento: utilizza l'operatore % (modulo) che restituisce il resto di una divisione intera
// Es: 10 % 2 --> restituisce 0    perchè 10 / 2 non ha resto
//     10 % 4 --> restituisce 2    perchè 10 / 4 ritorna 2 con un resto di 2

let i=0;

while (i<=20){
    if (i%2 == 0){
        console.log(i);
    }
    i++;
}