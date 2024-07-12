import reflex as rx


from search.states.main import State

from search.components.search_form import search_form

from search.components.buttons import (
    reset_button
)

from search.components.navbar import navbar






def search_interface():
    return rx.vstack(
        
        rx.box(),
        
        navbar(
            left_corner_text = State.search_type
            ),
        
        # Buttons
        rx.hstack(
            
            rx.box(), # Placeholder
            
            reset_button(
                reset_action=State.reset_everything
            ),
            
            rx.box(), # Placeholder
        
        width="100%"
        ),
        
        
        # Form
        rx.hstack(
            
            rx.box(), # Placeholder
            
            search_form(
                processing = State.search_processing,
                search_sequence =  State.search_count,   
                default_value = State.search_default,
                placeholder = State.search_placeholder,
                submit_actions = [
                        State.set_search_query(""),
                        State.ask_question,
                    ],
                stop_action = [
                        State.stop_search
                    ],
                search_query = State.search_query
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

