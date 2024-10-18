function Enviar(){
    var valor = document.getElementById('valor-lance').value

    if (valor.trim() === "") {
        alert("Por favor, lance um valor."); 
        return; 
    }
    valor = parseFloat(valor);

    var alerta = document.getElementById('alerta');

    if (valor < 450) {
        alerta.textContent = "O lance mínimo é R$450,00";
        alerta.style.color = "red"; 

        setTimeout(function() {
            alerta.textContent = ""; 
        }, 2000);
    
    } else {
        alerta.textContent = `Lance de R$${valor.toFixed(2)} enviado com sucesso!`;
        alerta.style.color = "green"; 

        setTimeout(function() {
            alerta.textContent = ""; 
        }, 2000);
    }
}

