import json
import csv
import os
from tkinter import Tk, Label, Button, filedialog, StringVar
from tkinterdnd2 import DND_FILES, TkinterDnD

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("JSON ⇄ CSV Converter")
        self.geometry("400x250")

        self.arquivo = None

        self.label_text = StringVar()
        self.label_text.set("Arraste um arquivo JSON ou CSV aqui")

        self.label = Label(self, textvariable=self.label_text, wraplength=300)
        self.label.pack(pady=20)

        self.drop_area = Label(self, text="DROP HERE", bg="lightgray", width=40, height=5)
        self.drop_area.pack(pady=10)

        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.drop)

        self.btn_converter = Button(self, text="Converter", command=self.converter)
        self.btn_converter.pack(pady=10)

    def drop(self, event):
        caminho = event.data.strip("{}")  # remove chaves do windows
        self.arquivo = caminho
        self.label_text.set(f"Arquivo selecionado:\n{os.path.basename(caminho)}")

    def converter(self):
        if not self.arquivo:
            self.label_text.set("Nenhum arquivo selecionado")
            return

        if self.arquivo.endswith(".json"):
            self.json_para_csv()
        elif self.arquivo.endswith(".csv"):
            self.csv_para_json()
        else:
            self.label_text.set("Formato inválido!")

    def json_para_csv(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)

            caminho_saida = filedialog.asksaveasfilename(defaultextension=".csv")

            campos = dados[0].keys()

            with open(caminho_saida, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                writer.writerows(dados)

            self.label_text.set("Conversão JSON → CSV concluída!")
        except Exception as e:
            self.label_text.set(f"Erro: {str(e)}")

    def csv_para_json(self):
        try:
            dados = []

            with open(self.arquivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for linha in reader:
                    dados.append(linha)

            caminho_saida = filedialog.asksaveasfilename(defaultextension=".json")

            with open(caminho_saida, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)

            self.label_text.set("Conversão CSV → JSON concluída!")
        except Exception as e:
            self.label_text.set(f"Erro: {str(e)}")


if __name__ == "__main__":
    app = App()
    app.mainloop()