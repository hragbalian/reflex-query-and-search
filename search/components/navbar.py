import reflex as rx


def menu_item_link(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": rx.color("accent", 3),
            "background_color": rx.color("accent", 3),
        },
    )
    
    
def navbar_menu() -> rx.Component:
    
    return rx.menu.root(
        
        rx.menu.trigger(
            rx.icon_button(
                rx.icon(tag="menu"),
                variant="ghost"
            ),
        ),
        
        rx.menu.content(

            rx.menu.item(
                "Unlink token", 
                on_click=[]),

            rx.menu.separator(),

            menu_item_link("About", "https://github.com/reflex-dev"),
            menu_item_link("Contact", "mailto:founders@=reflex.dev"),
        ),
    ),


def navbar(
    left_corner_text: str
    ) -> rx.Component:

    return rx.hstack(
          
        # Left side
        rx.hstack(
            rx.box(),
            
            rx.heading(left_corner_text, size="3"),
        ), 
        
        # Right side
        rx.hstack(
            
            rx.icon_button(
                rx.icon(tag="github"),
                variant="ghost",
                on_click=rx.redirect(
                    path="https://github.com/hragbalian/reflex-query-and-search",
                    external=True
                    )
            ),
            
            navbar_menu(),
            
            rx.box()
            
        ),
    
    
    width="100%",
    align="center",
    justify="between"
    ),