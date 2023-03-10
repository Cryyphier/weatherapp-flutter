import flet
from flet import *
import requests
import datetime

api_key = "ea56d9e4767fb9783322932c31d5fd12"

_current = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=14.3488961&lon=121.0392436&exclude=minutely,hourly,alerts&units=metric&appid={api_key}"
)

days = [
    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun",
]


def main(page: Page) :
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update ()
        else:
            _c.content.controls[0].height = 660 * 0.4
            _c.content.controls[0].update ()    

        pass

    def _current_temp():

        _current_temp =int(_current.json() ["current"] ["temp"])

        return[_current_temp]

    pass

    def _top():


        _today =_current_temp()


        top = Container(
            width=310,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["blue", "green"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=450, 
            curve="decelerate"),
            on_hover=lambda e:_expand(e),
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Text(
                                'City of San Pedro, Laguna', 
                                size=16,
                                weight="w500",
                            )
                        ]
                    ),
                    Container(padding=padding.only
                    (bottom=5)),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                    ),
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align="center",
                                    ),
                                    Row(
                                        vertical_alignment='start',
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    _today[0],
                                                    size=52,
                                                ),
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                    
                ]
                
            )
         )

        return top

    
        

    _c = Container(
        width= 310,
        height=660,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(
            width=300, 
            height=550,
            controls=[
                _top(),
            ],
        ),
    )
        
    page.add(_c)

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
