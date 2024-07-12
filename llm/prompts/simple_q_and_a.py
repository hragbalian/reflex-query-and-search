from llama_index.core.bridge.pydantic import BaseModel, Field


simple_question_prompt = """
You are a helpful assistant who answers questions.  
Respond always in markdown, using markdown notation where appropriate.
The question is: {question}
"""

class SimpleQuestionAnswer(BaseModel):
    """ Data model for the question answer"""
    answer: str = Field(..., description="The answer to the question")
    
