import reflex as rx
def index() -> rx.Component:
    return rx.box(
        
    )

app = rx.App(
    
)
app.add_page(
    index,
    title="VentaCar",
    description="Vendemos los mejores carros del mercado"
)

app.compile()