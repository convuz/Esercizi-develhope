// # Esercizio 35

// Sistemare la funzione in modo tale che non prendiamo errori in console. Inoltre spiegare brevemente come mai al momento la funzione è sbagliata.

// Indicazioni utili:

// - fate attenzione allo scope delle variabili



function canPlay() {
    let sport = " Football";
  
    if (true) {
        let personName = "Cosimo";
        console.log(personName + sport);
    }
}
  
canPlay();