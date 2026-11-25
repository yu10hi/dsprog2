import flet as ft


def main(page: ft.Page):

    hello_world=ft.Text("HelloWorld", size=50)

    counter = ft.Text("0", size=50, data=0)

    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.value = str(counter.data)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, key="increment", on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
    #content=counter,
    content=ft.Row(
        controls=[
            ft.Column(controls=[hello_world, counter]),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        ),
    ),
        ),
        ft.FloatingActionButton(icon=ft.Icons.REMOVE, key="decrement", on_click=decrement_click),
                                
    )


if __name__ == "__main__":
    ft.run(main)
