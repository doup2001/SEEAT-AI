"""
RetrievalQA 체인 생성 및 질의응답 수행 모듈
"""
from langchain_openai import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class QAService:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore

    def create_qa_chain(self):
        """
        LangChain RetrievalQA 체인을 생성합니다.
        """
        retriever = self.vectorstore.as_retriever()

        prompt = PromptTemplate.from_template(
            """
            아래는 상영관에 대해 유저들이 작성한 후기 모음입니다.
            리뷰에 존재하는 각각의 상영관 후기를 바탕으로 이용 패턴, 선호하는 영화의 장르/좌석/영화관,
            후기의 전반적 감성(긍정/부정/중립), 자주 사용하는 해시태그, 특징적인 의견을 요약해 주세요:
            
            {context}
            """
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
        )

    def query(self, question: str) -> dict:
        """
        질문에 대해 요약 답변을 생성합니다.

        Args:
            question (str): 사용자 질문

        Returns:
            dict: 질의와 요약 결과 포함
        """
        if not hasattr(self, 'qa_chain'):
            self.create_qa_chain()

        result = self.qa_chain.invoke(question)
        return {"query": question, "result": result}
