# Conversor de Moedas

Este projeto é um conversor de moedas baseado em Flask, que consome uma API de taxas de câmbio e exibe uma interface web para conversão dinâmica entre diferentes moedas.

## 📌 Funcionalidades
- Conversão de moedas em tempo real utilizando dados da API `open.er-api.com`.
- Interface web simples e responsiva.
- Atualização automática das taxas de câmbio a cada 5 minutos.
- Validação e exibição de erros para entradas inválidas.

## 🛠 Tecnologias Utilizadas
- Python (Flask)
- HTML, CSS, JavaScript
- API externa para taxas de câmbio

## 📂 Estrutura do Projeto
```
📦 conversor_de_moedas
├── 📂 static
│   ├── styles.css  # Estilos do frontend
│   ├── script.js   # Lógica de conversão dinâmica
├── 📂 templates
│   ├── index.html  # Página principal da aplicação
├── app.py  # Servidor Flask
├── conversor_terminal.py  # Lógica de conversão de moedas via terminal
├── README.md  # Documentação do projeto
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado
- Flask instalado (`pip install flask`)

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/conversor_de_moedas.git
   cd conversor_de_moedas
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```bash
   python app.py
   ```
4. Acesse a aplicação no navegador:
   ```
   http://127.0.0.1:5000
   ```

## 📡 API de Câmbio
O projeto utiliza a API pública [Exchange Rate API](https://open.er-api.com/) para obter as taxas de câmbio atualizadas.

## 📝 Licença
Este projeto está licenciado sob a MIT License.

## 📞 Contato
Caso tenha dúvidas ou sugestões, entre em contato:
- 📧 Email: seuemail@email.com
- 🔗 GitHub: [seuusuario](https://github.com/seuusuario)