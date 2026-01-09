import flet as ft
import math
import os

# Mobile irratti iskiriiniin gurraacha'ee akka hin hafneef (Renderer sirreessuu)
os.environ["FLET_RENDERER"] = "skia"

def main(page: ft.Page):
    page.title = "Scientific Calculator Pro"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#000000"
    
    # Iskiriiniin mobile hunda irratti akka of sirreessu
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.padding = 15

    # Ibsituu (Display)
    result = ft.Text(value="0", color="white", size=50, weight="bold")

    def on_click(e):
        data = e.control.data
        
        if data == "AC":
            result.value = "0"
        elif data == "C":
            result.value = result.value[:-1] if len(result.value) > 1 else "0"
        elif data == "=":
            try:
                # Mallattoolee herregaa gara Python-itti jijjiiruu
                expr = result.value.replace("×", "*").replace("÷", "/").replace("^", "**").replace("%", "/100")
                res = eval(expr)
                result.value = str(round(res, 6)) if isinstance(res, (int, float)) else str(res)
            except:
                result.value = "Error"
        elif data in ["sin", "cos", "tan", "sqrt", "log"]:
            try:
                val = float(result.value)
                if data == "sin": res = math.sin(math.radians(val))
                elif data == "cos": res = math.cos(math.radians(val))
                elif data == "tan": res = math.tan(math.radians(val))
                elif data == "sqrt": res = math.sqrt(val)
                elif data == "log": res = math.log10(val) if val > 0 else 0
                result.value = str(round(res, 6))
            except:
                result.value = "Error"
        else:
            if result.value == "0":
                result.value = data
            else:
                result.value += data
        page.update()

    # Furtuulee (Buttons)
    def btn(text, color="#1C1C1E", t_color="white", data=None, expand=1):
        return ft.Container(
            content=ft.Text(text, size=22, weight="bold", color=t_color),
            alignment=ft.alignment.center,
            bgcolor=color,
            border_radius=15,
            height=75,
            expand=expand,
            on_click=on_click,
            data=data if data else text,
        )

    # UI Layout
    page.add(
        ft.Container(
            content=result,
            padding=30,
            alignment=ft.alignment.center_right,
            bgcolor="#1C1C1E",
            border_radius=20,
            margin=ft.margin.only(bottom=15)
        ),
        ft.Column([
            ft.Row([btn("sin", "#2C2C2E"), btn("cos", "#2C2C2E"), btn("tan", "#2C2C2E"), btn("log", "#2C2C2E")], spacing=10),
            ft.Row([btn("AC", "#FF3B30"), btn("C", "#48484A"), btn("^", "#FF9500"), btn("÷", "#FF9500")], spacing=10),
            ft.Row([btn("7"), btn("8"), btn("9"), btn("×", "#FF9500")], spacing=10),
            ft.Row([btn("4"), btn("5"), btn("6"), btn("-", "#FF9500")], spacing=10),
            ft.Row([btn("1"), btn("2"), btn("3"), btn("+", "#FF9500")], spacing=10),
            ft.Row([btn("0", expand=2), btn("."), btn("=", "#34C759")], spacing=10),
        ], spacing=10)
    )

# ft.app() bakka isaa ft.run() fayyadamneera
if __name__ == "__main__":
    ft.run(main) 
