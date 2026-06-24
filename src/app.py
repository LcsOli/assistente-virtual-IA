import streamlit as st
from gpt4all import GPT4All
from rag_pipeline import carregar_base_de_dados
from prompts import PROMPT_FINGUIA

st.set_page_config(page_title="FinGuia - Assistente Financeiro", page_icon="🏦", layout="centered")

st.title("🏦 FinGuia - Assistente Inteligente e Seguro")
st.markdown("Educação financeira com segurança total. Processamento 100% local.")

@st.cache_resource
def iniciar_recursos():
    db = carregar_base_de_dados()
    llm = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
    return db, llm

banco_vetorial, modelo_llm = iniciar_recursos()

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Ex: Como transfiro via Pix com segurança?")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("🔍 Analisando informações seguras...")
        
        docs = banco_vetorial.similarity_search(pergunta, k=2)
        contexto = "\n".join([d.page_content for d in docs])
        
        prompt_final = PROMPT_FINGUIA.format(context=contexto, question=pergunta)
        
        with st.spinner("Processando resposta..."):
            with modelo_llm.chat_session():
                resposta = modelo_llm.generate(prompt_final, max_tokens=600)
        
        placeholder.markdown(resposta)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})