

from llama_index.program.openai import OpenAIPydanticProgram

from llm.config import llm

from llm.prompts.simple_q_and_a import (
    simple_question_prompt,
    SimpleQuestionAnswer
)


model_prompts = {
    "Simple Q&A": {
        "model": SimpleQuestionAnswer,
        "prompt": simple_question_prompt,
        "params": ["question"]
    }
}


class OpenAIPydanticProgramSwitch:
    
    def __init__(self, type: str):
        self.prompt = model_prompts[type]["prompt"]
        self.model = model_prompts[type]["model"]
    
    @classmethod
    def program_switch(self, prompt, pydantic_model):
        
        program = OpenAIPydanticProgram.from_defaults(
            output_cls=pydantic_model,
            llm=llm,
            prompt_template_str=prompt, 
            verbose=True
        )
        
        return program
    
    def get_program(self):
        return self.program_switch(self.prompt, self.model)
        

if __name__=="__main__":
    
    switch = OpenAIPydanticProgramSwitch("Simple Q&A")

    program = switch.get_program()

    program(question="who is joe biden")