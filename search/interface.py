

import reflex as rx

from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.llms.openai import OpenAI
from llama_index.core.bridge.pydantic import BaseModel, Field

openai_chat_model = "gpt-3.5-turbo-0125"
llm = OpenAI(model=openai_chat_model, temperature=.5)

prompt = """
You are a helpful assistant who answers questions.  

The question is: {question}
"""


class SimpleQuestionAnswer(BaseModel):
    """ Data model for the question answer"""
    answer: str = Field(..., description="The answer to the question")
    


class State(rx.State):
    """The app state."""
    
    search_processing: bool = False
    search_initial_placeholder: str = "Ask a question"
    search_followup_placeholder: str = "Ask a follow-up"
    search_count: int = 0
    search_query_value: str = ""

    search_response: str = ""
    
    @rx.var
    def search_placeholder(self) -> str:
        if not self.search_count:
            return self.search_initial_placeholder
        else:
            return self.search_followup_placeholder
    
    async def stop_search(self):
        self.search_processing = False
        yield
    
    async def reset_everything(self):
        self.reset()
    
    @rx.background
    async def ask_question(self, form_data: dict):
        
        program = OpenAIPydanticProgram.from_defaults(
            output_cls=SimpleQuestionAnswer,
            llm=llm,
            prompt_template_str=prompt, 
            verbose=True
        )
        
        
        async with self:
            
            self.search_count += 1
            
            self.search_processing = True
            yield
            
            
        for partial_object in program.stream_partial_objects(
            question=form_data["search_query"],
            ):
            
            if self.search_processing:
                async with self:
                    self.search_response = partial_object.answer
                    yield
            
        async with self:
            self.search_processing = False
            yield







def submit_search_button() -> rx.Component:
    return rx.icon_button(
                rx.icon(tag="arrow-right"),
                variant="soft",
                type="submit",
                radius="full",
                title="Submit search",
                # on_click=[]
            )

def stop_search_button() -> rx.Component:
    return rx.icon_button(
                rx.icon(tag="circle-stop"),
                variant="soft",
                color_scheme="red",
                type="submit",
                radius="full",
                title="Stop search",
                on_click=State.stop_search
            )
    
    


def search_form() -> rx.Component:
    
    return rx.vstack(
        
        rx.form(
            
                rx.hstack(
                                    
                    rx.input(
                        
                        rx.input.slot(
                            rx.icon(tag="search")
                        ),
                        
                        rx.input.slot(
                            
                            rx.cond(
                                State.search_count==0,
                                submit_search_button(),
                                rx.cond(
                                    State.search_processing,
                                    stop_search_button(),
                                    submit_search_button()
                                )
                            )
                            
                            
                        ),
                        
                        default_value=State.search_query_value,
                        placeholder=State.search_placeholder,
                        name="search_query",
                        required=True,
                        width="100%",
                        max_length=200,
                        height=75,
                        padding=10,
                        border_radius=20,
                    ),
                
                rx.spinner(
                    loading=State.search_processing, 
                    size="3"
                    ),
                    
                width="100%",
                align="center",
                z_index=100,
                ),
                
            on_submit=[
                State.set_search_query_value(""),
                State.ask_question,  
            ],
            
            reset_on_submit=True,
            align="center",
            ),
    
    rx.cond(
        State.search_count>0,
        rx.divider(width="100%")
    ),
    
    
    
    
    width="100%",
    )
    



def search_interface():
    return rx.vstack(
        
        rx.box(),
        
        # Form
        rx.hstack(
            
            rx.box(), # Placeholder
            
            search_form(),
            
            rx.box(), # Placeholder
        
        width="100%"
        ),
        
        # Response
        rx.hstack(
            
            rx.box(), # Placeholder
            
            rx.markdown(State.search_response),
            
            rx.box(), # Placeholder
        
        width="100%"
        ),
        
        
        
    width="100%",

    )

