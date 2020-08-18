from guizero import App, Text, Slider
from gpiozero import  RGBLED


led = RGBLED(2, 3, 17)
app = App(title="RGB Demo", height=150, width=400, layout="grid")


def create_ui():
    # RED
    text = Text(app, text="Red Value:", align="right", color="red", grid=[0,0])
    slider = Slider(app, grid=[1,0], width="250", align="bottom", command=on_red_slider_changed)

    # GREEN
    text = Text(app, text="Green Value:", align="right", color="green", grid=[0,1])
    slider = Slider(app, grid=[1,1], width="250", align="bottom", command=on_green_slider_changed)

    # BLUE
    text = Text(app, text="Blue Value:",  align="right",  color="blue", grid=[0,2])
    slider = Slider(app, grid=[1,2], width="250", align="bottom", command=on_blue_slider_changed)

    app.display()

def on_red_slider_changed(data):
    red, green, blue  = led.value
    new_red_value = int(data)/100
    led.color = (new_red_value, green, blue)


def on_green_slider_changed(data):
    red, green, blue = led.value
    new_green_value = int(data) / 100
    led.color = (red, new_green_value, blue)

def on_blue_slider_changed(data):
    red, green, blue = led.value
    new_blue_value = int(data) / 100
    led.color = (red, green, new_blue_value)


def main():
    create_ui()

if __name__ == '__main__':
    main()
