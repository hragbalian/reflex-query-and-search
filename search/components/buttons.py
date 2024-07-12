
import reflex as rx


def submit_search_button() -> rx.Component:
    return rx.icon_button(
                rx.icon(tag="arrow-right"),
                variant="soft",
                type="submit",
                radius="full",
                title="Submit search",
                # on_click=[]
            )

def stop_search_button(
    stop_action: list = []
    ) -> rx.Component:
    return rx.icon_button(
                rx.icon(tag="circle-stop"),
                variant="soft",
                color_scheme="red",
                type="submit",
                radius="full",
                title="Stop search",
                on_click=stop_action
            )
    