# app/services/qa_service.py


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
            아래는 특정 상영관에 대해 유저들이 작성한 후기 모음입니다. 이 리뷰들을 참고하여, 상영관의 이용 패턴, 예를 들어 방문 시간대나 방문 빈도, 그리고 좌석 선택의 특징 등을 포함해 상세하게 요약해 주세요. 
            또한, 좌석 위치를 보고 상/하/좌/우/ 중에서 어디를 선호하는지 와 그 이유도 함께 설명해 주시기 바랍니다.
            더불어 해당 영화관의 전반적인 분위기와 특징, 예를 들어 청결도, 음향, 시설 상태 등에 대해서도 객관적으로 평가해 주세요. 
            후기에 드러난 감성 분석 결과, 즉 긍정적, 부정적, 중립적인 의견들의 비율과 그 주요 원인도 포함해 주시면 좋겠습니다.
            리뷰 속에서 자주 등장하는 해시태그의 의미도 설명해 주시고, 마지막으로 특징적이고 인상적인 의견이나 개선 요청사항이 있다면 그것도 함께 정리해 주세요.
            아래 리뷰 데이터를 바탕으로, 상영관의 상세한 정보를 명확하고 체계적으로 전달해 주시기 바랍니다:
            
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

        # result가 dict면, 답변 텍스트만 꺼내서 반환
        if isinstance(result, dict):
            answer_text = result.get("result") or str(result)
        else:
            answer_text = str(result)

        return answer_text
