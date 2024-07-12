
import reflex as rx


from search.states.main import State

from search.components.buttons import (
    stop_search_button,
    submit_search_button
)

def search_form(
    processing: bool,
    submit_actions: list = []
    ) -> rx.Component:
    
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
                                    processing,
                                    stop_search_button(
                                        stop_action=State.stop_search
                                        ),
                                    submit_search_button()
                                )
                            )
                            
                            
                        ),
                        
                        default_value=State.search_query,
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
                    loading=processing, 
                    size="3"
                    ),
                    
                width="100%",
                align="center",
                z_index=100,
                ),
                
            on_submit=submit_actions,
            
            reset_on_submit=True,
            align="center",
            ),
    
    
    rx.heading(State.search_query, size="3"),
    
    
    
    width="100%",
    justify="center",
    align="center"
    )
    