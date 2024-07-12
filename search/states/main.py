import reflex as rx

from llm.program_switch import OpenAIPydanticProgramSwitch


class State(rx.State):
    """The app state."""
    
    search_type: str = "Simple Q&A"
    search_program: str = "pydantic_program"
    
    search_processing: bool = False
    search_initial_placeholder: str = "Ask a question"
    search_followup_placeholder: str = "Ask a follow-up"
    search_count: int = 0
    search_query: str = ""
    search_response: str = ""
    
    
    extra_kwargs: dict = dict()
    
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
        
        async with self:
            
            self.search_query = form_data["search_query"]
            
        if self.search_program == "pydantic_program":

            async for _ in self.ask_question_with_program():
                yield


    async def ask_question_with_program(self):
        
        switch = OpenAIPydanticProgramSwitch(self.search_type)

        program = switch.get_program()
        
        async with self:
            self.search_count += 1
        
        async with self:
            self.search_processing = True
            yield
        
        
        for partial_object in program.stream_partial_objects(
            question=self.search_query,
            # **kwargs
            ):
            
            if self.search_processing:
                
                async with self:
                    self.search_response = partial_object.answer
                    yield
            
        async with self:
            self.search_processing = False
            yield


