import reflex as rx


from search.states.main import State

from search.components.search_form import search_form







def search_interface():
    return rx.vstack(
        
        rx.box(),
        
        # Form
        rx.hstack(
            
            rx.box(), # Placeholder
            
            search_form(
                processing = State.search_processing,
                submit_actions = [
                        State.set_search_query(""),
                        State.ask_question,
                        
                    ]
                ),
            
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

