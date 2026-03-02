# 🌡️ Simulador IoT: Monitor de Ambiente com DHT11

![Status](https://img.shields.io/badge/Status-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte das atividades do curso de Bacharelado em Engenharia de Software. O objetivo é criar um **simulador web interativo** de um dispositivo IoT, mimetizando o comportamento de um microcontrolador (como o ESP32) equipado com um sensor de temperatura e umidade **DHT11**. 

Em vez de utilizar hardware físico imediatamente, a lógica de programação, o acionamento de atuadores (um ventilador via relé) e os indicadores visuais (LEDs) foram prototipados utilizando **apenas Python** através do framework **Streamlit**.

## ✨ Funcionalidades

* **Simulação de Sensores:** Controles deslizantes (sliders) na interface web permitem alterar dinamicamente a temperatura e a umidade do "ambiente".
* **Lógica Condicional (LEDs Virtuais):**
  * 🔵 **Azul:** Temperatura < 20°C (Ambiente Frio)
  * 🟢 **Verde:** Temperatura agradável (Entre 20°C e o limite definido)
  * 🔴 **Vermelho:** Temperatura alta (Acima do limite)
* **Atuador (Relé/Ventilador):** Acionamento automático de um "relé" (indicativo na tela) caso a temperatura ultrapasse o limite de segurança configurado pelo usuário.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a simulação na sua máquina local.

### Pré-requisitos
* Ter o [Python](https://www.python.org/downloads/) instalado na máquina.
* Opcional, mas recomendado: Criar um ambiente virtual (venv).

### Instalação

1. Clone este repositório:
git clone [https://github.com/kennyXP22/simulador-iot-dht11.git](https://github.com/SEU-USUARIO/simulador-iot-dht11.git)

2. Acesse a pasta do projeto:
cd simulador-iot-dht11

3. Instale as depedencias necessarias:
pip install streamlit

## Rodando a Aplicação
Para iniciar o servidor web do simulador, execute o seguinte comando no terminal:
streamlit run simulador_iot.py
