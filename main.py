from kivy.app import App
from kivy.lang import Builder

from Buscador import buscar_por_codigo, buscar_por_texto

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 15
    spacing: 10

    Label:
        text: "BUSCADOR DE UNIDADES"
        font_size: 24
        bold: True
        size_hint_y: None
        height: 45

    TextInput:
        id: busqueda
        hint_text: "Ingrese código o descripción..."
        multiline: False
        font_size: 20
        size_hint_y: None
        height: 50

    BoxLayout:
        size_hint_y: None
        height: 50
        spacing: 10

        Button:
            text: "BUSCAR"
            on_release: app.buscar()

        Button:
            text: "LIMPIAR"
            on_release: app.limpiar()

    ScrollView:

        Label:
            id: resultado
            text: ""
            text_size: self.width-20, None
            size_hint_y: None
            height: max(self.texture_size[1], self.parent.height)
            halign: "left"
            valign: "top"
            padding: 10,10
'''

class BuscadorApp(App):

    def build(self):
        return Builder.load_string(KV)

    def buscar(self):

        texto = self.root.ids.busqueda.text.strip()

        if texto == "":
            self.root.ids.resultado.text = "Ingrese un código o una descripción."
            return

        # Si parece un código
        if texto.upper().startswith("U"):
            resultado = buscar_por_codigo(texto)

            if resultado == "No encontrado":
                self.root.ids.resultado.text = resultado
            else:
                self.root.ids.resultado.text = (
                    f"[b]{texto.upper()}[/b]\n\n{resultado}"
                )

        else:
            resultados = buscar_por_texto(texto)

            if isinstance(resultados, dict):

                if len(resultados) == 0:
                    self.root.ids.resultado.text = "No se encontraron coincidencias."
                    return

                salida = ""

                for codigo, descripcion in resultados.items():

                    salida += (
                        f"[b]{codigo}[/b]\n"
                        f"{descripcion}\n\n"
                    )

                self.root.ids.resultado.markup = True
                self.root.ids.resultado.text = salida

            else:
                self.root.ids.resultado.text = resultados

    def limpiar(self):
        self.root.ids.busqueda.text = ""
        self.root.ids.resultado.text = ""


if __name__ == "__main__":
    BuscadorApp().run()
