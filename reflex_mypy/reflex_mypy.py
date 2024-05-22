import reflex as rx


class State(rx.State):
    """The app state."""

    counter: int = 0

    def increment_by(self, arg: int) -> None:
        """Increment the counter."""
        self.counter += arg

    @rx.var
    def counter_message(self) -> str:
        """Return the counter message."""
        return f"Click me: Counter: {self.counter}"


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.button(State.counter_message, on_click=lambda: State.increment_by(1)),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
