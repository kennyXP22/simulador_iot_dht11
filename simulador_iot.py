import streamlit as st

# Configuração da página Web
st.set_page_config(page_title="Simulador IoT", page_icon="🌡️")
st.title("Monitor de Ambiente DHT11 🌡️")

st.sidebar.header("🕹️ Painel de Simulação (Sensor DHT11)")
st.sidebar.markdown("Use os controles abaixo para simular as leituras do ambiente:")

# Simuladores do sensor
temperatura = st.sidebar.slider("Temperatura (°C)", min_value=-10.0, max_value=50.0, value=25.0, step=0.5)
umidade = st.sidebar.slider("Umidade (%)", min_value=0, max_value=100, value=50)

# Configuração de limite
limite_temp_vent = st.sidebar.number_input("Limite para ligar Ventilador (°C)", value=30.0)

# LÓGICA DO MICROCONTROLADOR 
ventilador_ligado = temperatura >= limite_temp_vent

if temperatura < 20:
    cor_led = "🔵 Azul (Ambiente Frio)"
elif 20 <= temperatura < limite_temp_vent:
    cor_led = "🟢 Verde (Ambiente Agradável)"
else:
    cor_led = "🔴 Vermelho (Ambiente Quente)"

# FRONT-END 

st.subheader("📡 Leituras do Sensor")
col1, col2 = st.columns(2)
col1.metric(label="Temperatura Atual", value=f"{temperatura} °C")
col2.metric(label="Umidade Atual", value=f"{umidade} %")

st.divider()

st.subheader("⚙️ Atuadores e Indicadores (Saídas)")

st.info(f"**Status do LED:** Acendeu a cor {cor_led}")

# Relé/Ventilador
if ventilador_ligado:
    st.error("🌪️ **Relé ACIONADO:** A temperatura ultrapassou o limite! O Ventilador está LIGADO.")
else:
    st.success("💤 **Relé DESLIGADO:** A temperatura está sob controle. O Ventilador está parado.")