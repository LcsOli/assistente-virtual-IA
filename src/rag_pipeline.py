from langchain_community.document_loaders import PyPDFLoader, UnstructuredExcelLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def carregar_base_de_dados():
    print("Iniciando a leitura dos documentos...")
    
    loader_pdf = PyPDFLoader("data/manual_seguranca_faq.pdf")
    docs_pdf = loader_pdf.load()
    
    loader_excel = UnstructuredExcelLoader("data/catalogo_produtos_financeiros.xlsx", mode="elements")
    docs_excel = loader_excel.load()
    
    documentos = docs_pdf + docs_excel
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documentos)
    
    print("Gerando Embeddings...")
    embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    vector_store = FAISS.from_documents(chunks, embeddings_model)
    
    print("Base RAG gerada com sucesso!")
    return vector_store

if __name__ == "__main__":
    banco_vetorial = carregar_base_de_dados()