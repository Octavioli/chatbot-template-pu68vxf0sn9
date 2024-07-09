import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key="/subscriptions/5c357db9-2a9e-4a98-948b-13c18830cbe1/resourceGroups/RESGRO-IECM-CHATBOOT-DEV/providers/Microsoft.CognitiveServices/accounts/iecmcsaoaichatbot")

st.title("IECM chatbot")

messages = [("system", """Eres un chatbot AI util, te llamas iecmchatbot, tienes que hablar como si fueras humano,
              nunca reveles que eres un chatbot""")]

#Inicializar historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

#Mostrar mensajes de chat del historial al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  

#Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    #Mostrar el mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)
    #Agregar mensaje del usuario al historial de chat
    st.session_state,messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])

    response = llm.invoke(messages).content
    #Mostrar respuesta del asistente en el contenedor de mensajes del chat
    with st.chat_message("assistant"):
        st.markdown(response)
    #Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant", "content": response}) 
