import re
import tkinter as tk

palabras_reservadas = ["do", "for", "while", "if", "else"]

def analizar(entrada):
    identificador = []
    for token in palabras_reservadas:
        matches = re.findall(r"\b{}\b".format(token), entrada)
        for match in matches:
            identificador.append(f"<Reservada     {token}>   Simbolo     {token}")
            entrada = entrada.replace(match, " ", 1)
    matches = re.findall(r"(?<!\()(\()(?!\()", entrada)

    for match in matches:
        identificador.append(f"<Parentesis_apertura {match}>")
        entrada = entrada.replace(match, " ", 1)
    matches = re.findall(r"(?<!\))(\))(?!\))", entrada)

    for match in matches:
        identificador.append(f"<Parentesis en cierre {match}>")
        entrada = entrada.replace(match, " ", 1)
    entrada = entrada.strip()
    if len(entrada) > 0:
        identificador.append("<No definido> {}".format(entrada))
    return identificador


def analizar_de_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    entrada = codigo.split("\n")
    tokens_totales = []
    for i, entrada in enumerate(entrada):
        tokens_linea = analizar(entrada)
        for token in tokens_linea:
            tokens_totales.append((i+1, token))

    resultado_texto.delete("1.0", tk.END)
    for numero_linea, token in tokens_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n {token}\n")

    numero_reservadas = len([token for numero_linea, token in tokens_totales if token.startswith("<Reservada")])

    numero_Parente_apertura = len([token for numero_linea, token in tokens_totales if token.startswith("<Parentesis_apertura")])

    numero_Parente_cierre = len([token for numero_linea, token in tokens_totales if token.startswith("<Parentesis en cierre")])


    resultado_texto.insert(tk.END, f"\nPalabras reservadas: {numero_reservadas}\n")

    resultado_texto.insert(tk.END, f"Parentesis de apertura: {numero_Parente_apertura}\n")

    resultado_texto.insert(tk.END, f"Parentesis de cierre: {numero_Parente_cierre}\n")
    

ventana = tk.Tk()
ventana.geometry("500x580")
ventana.title("Analizador de código léxico")
ventana.config(bg="#12657f")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=60, y=20)
entrada_texto.configure(insertbackground="black")

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
resultado_texto.place(x=60, y=220)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_de_codigo)
boton_analizar.place(x=150, y=430)

boton_borrar = tk.Button(ventana, text="Borrar",font=("Arial", 12), bg="#121b29", fg="white", command=lambda: entrada_texto.delete("1.0", tk.END))
boton_borrar.place(x=280, y=430)

ventana.mainloop()
