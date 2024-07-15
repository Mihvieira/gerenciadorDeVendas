from gui.janelas import *


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x520")
        self.resizable(False, False)
        self._set_appearance_mode('dark')
        self.title("Gerenciamento de Vendas")
        self.janela = QuadroPrincipal(self)
        self.janela.pack(expand=True, fill='both')
        self.mainloop()


if __name__ == '__main__':
    app = App()
