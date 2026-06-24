# 🏦 FinGuia - Assistente Financeiro Inteligente

O **FinGuia** é um assistente financeiro educacional guiado por IA, focado em transparência, segurança digital e facilidade de uso. O projeto utiliza a arquitetura RAG (Retrieval-Augmented Generation) para fornecer respostas precisas e baseadas em documentos oficiais, garantindo que a IA não alucine com dados sensíveis.

## 🚀 Funcionalidades
- **Educação Financeira:** Explicação clara de produtos como CDB, LCI e Tesouro Direto.
- **Segurança Digital:** Diretrizes contra golpes (Phishing, Falso Funcionário) com base em manuais reais.
- **Arquitetura Privada:** Processamento 100% local. Seus dados e perguntas não saem da sua máquina.

## 🛠 Tecnologias
- **Python** e **Streamlit** (Interface e UX)
- **LangChain** (Orquestração da IA)
- **GPT4All** (Modelo Llama-3 rodando localmente)
- **FAISS** (Banco de dados vetorial para busca semântica)

## 📦 Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone <link-do-seu-repositorio>
   cd assistente-virtual-IA
2. **Instale as dependências**
    pip install -r requirements.txt
3. **Inicie o FinGuia**
    streamlit run src/app.py

## 🛡 Segurança e DevSecOps
Este projeto foi desenhado sob a premissa de Zero PII (Personally Identifiable Information) on Cloud. Todo o processamento ocorre via modelos de linguagem abertos, garantindo a soberania dos dados do usuário final.

Projeto desenvolvido como desafio de IA Aplicada e Cybersecurity.

### Por que esta organização é importante?
1. **Padronização:** O `requirements.txt` evita o "erro de biblioteca faltando" que enfrentamos durante a montagem do ambiente.
2. **Documentação:** O `README.md` bem escrito mostra que você tem preocupação com a **usabilidade** (quem vai baixar seu código precisa saber como rodar) e com o **valor de negócio** (o pitch que incluímos no topo).
