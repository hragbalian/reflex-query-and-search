"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from search.interface import search_interface

app = rx.App()
app.add_page(search_interface, route="/search")
