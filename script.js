// script.js

document.addEventListener("DOMContentLoaded", function () {
    const valorInput = document.getElementById("valor");
    const moedaOrigem = document.getElementById("moeda_origem");
    const moedaDestino = document.getElementById("moeda_destino");
    const convertidoInput = document.getElementById("convertido");
    const ultimaAtualizacao = document.getElementById("ultima-atualizacao");

    function converterMoeda() {
        const valor = valorInput.value;
        const origem = moedaOrigem.value;
        const destino = moedaDestino.value;

        if (!valor || isNaN(valor)) {
            convertidoInput.value = "Valor inválido";
            return;
        }

        fetch("/converter", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                moeda_origem: origem,
                moeda_destino: destino,
                valor: valor
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    convertidoInput.value = data.erro; // Exibe a mensagem detalhada
                } else {
                    convertidoInput.value = data.convertido;
                    ultimaAtualizacao.textContent = `Última atualização: ${data.ultima_atualizacao}`;
                }
            })
            .catch(() => {
                convertidoInput.value = "Erro na requisição";
            });
    }

    // Eventos para atualizar a conversão dinamicamente
    valorInput.addEventListener("input", converterMoeda);
    moedaOrigem.addEventListener("change", converterMoeda);
    moedaDestino.addEventListener("change", converterMoeda);
});
