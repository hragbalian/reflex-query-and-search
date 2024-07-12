
import reflex as rx


from search.components.buttons import (
    stop_search_button,
    submit_search_button,
)

def search_form(
    processing: bool,
    search_sequence: int,
    placeholder: str,
    default_value: str,
    submit_actions: list = [],
    stop_action: list = [],
    search_query: str = ""
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
                                search_sequence==0,
                                submit_search_button(),
                                rx.cond(
                                    processing,
                                    stop_search_button(stop_action=stop_action),
                                    submit_search_button()
                                )
                            )
                            
                            
                        ),
                        
                        default_value=default_value,
                        placeholder=placeholder,
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
                justify="center",
                align="center",
                z_index=100,
                ),
                
            on_submit=submit_actions,
            
            reset_on_submit=True,
            justify="center",
            align="center",
            ),
    
    
    rx.heading(search_query, size="3"),
    
    
    
    width="100%",
    justify="center",
    align="center"
    )
    