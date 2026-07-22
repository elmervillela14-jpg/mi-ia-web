import streamlit as st
st.title("🤖 Mi Primera Web de IA")
st.write("¡Hola! Escribe un mensaje para conversar.")

pregunta = st.text_input("Tu mensaje:", placeholder="Escribe 'hola' o 'como estas'")

if st.button("Enviar"):
    texto = pregunta.lower()
    
    if "hola" in texto or "buenas" in texto:
        st.success("Bot: ¡Hola! Qué gusto verte por aquí. 👋")
    elif "como estas" in texto or "cómo estás" in texto:
        st.info("Bot: ¡Súper bien! Corriendo en vivo en tu página web. 🚀")
    elif "nombre" in texto:
        st.warning("Bot: Me llamo PythonWeb AI. 🤖")
    elif texto == "":
        st.error("Por favor escribe un mensaje primero.")
    else:
        st.write("Bot: Interesante... Aún estoy aprendiendo sobre ese tema. 🤔")