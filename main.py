from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ElifApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)

        message = Label(
            text="Elif ❤️\nFatih seni çok seviyor!",
            font_size="28sp",
            halign="center"
        )

        button = Button(
            text="❤️ Mesaja Dokun ❤️",
            font_size="22sp"
        )

        button.bind(
            on_press=lambda x: setattr(
                message,
                "text",
                "Elif ❤️\nFatih seni çok seviyor!"
            )
        )

        layout.add_widget(message)
        layout.add_widget(button)

        return layout

ElifApp().run()
