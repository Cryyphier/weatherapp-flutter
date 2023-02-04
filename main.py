import flet
from flet import *


class DropDownSearchBar(UserControl):
    def __init__(self):
        super().__init__()

    def drop_down_search(self):
        _object_ = Container(
            width=450,
            height=50,
            bgcolor="white10",
            border_radius=6,
            padding=padding.only(top=15, left=21, right=21, bottom=15),
            clip_behavior=ClipBehavior.HARD_EDGE,
            animate=animation.Animation(400, 'decelerate'),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                alignment=MainAxisAlignment.START,
                controls=[

                    Row(
                        spacing=10,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Icon(
                                name=icons.SEARCH_ROUNDED,
                                size=15, 
                                opacity=0.90,
                            ),
                            TextField(
                                border_color="transparent",
                                height=20,
                                text_size=12,
                                content_padding=2,
                                cursor_color='black',
                            ),
                        ]
                    )
                ]
            )
        )

        return _object_

    def build(self):
        return self.drop_down_search()

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = padding.only(top=50)
    page.add(DropDownSearchBar())
    page.update()
    pass


if __name__ == "__main__":
    flet.app(target=main)

