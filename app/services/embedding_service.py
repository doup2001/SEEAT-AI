# app/services/embedding_service.py


from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from app.core.config import OPENAI_API_KEY
class EmbeddingService:
    """
    문서 리스트에 대해 임베딩 생성 및 FAISS 인덱스 빌드/저장/로드를 제공합니다.
    """

    def __init__(self, index_path: str = "theater_reviews_index"):
        self.embedding_model = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.index_path = index_path
        self.vectorstore = None

    def create_index(self, documents: list[Document]) -> None:
        """
        문서 리스트로부터 임베딩을 생성하고 FAISS 인덱스를 구축합니다.
        """
        self.vectorstore = FAISS.from_documents(documents, embedding=self.embedding_model)

    def save_index(self) -> None:
        """
        현재 구축된 FAISS 인덱스를 로컬에 저장합니다.
        """
        if self.vectorstore:
            self.vectorstore.save_local(self.index_path)
        else:
            raise ValueError("vectorstore가 비어 있어 저장할 수 없습니다. 먼저 create_index를 호출하세요.")

    def load_index(self) -> FAISS:
        """
        저장된 FAISS 인덱스를 로드합니다.
        """
        self.vectorstore = FAISS.load_local(
            folder_path=self.index_path,
            embeddings=self.embedding_model,
            allow_dangerous_deserialization=True)
        return self.vectorstore

