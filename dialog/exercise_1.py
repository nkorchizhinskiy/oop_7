from PyQt5.QtWidgets import QDialog


class Exercise_1(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        
    def _create_window(self):
        self.resize(400, 250)
        self.setWindowTitle("Поиск гипотенузы")
        
    def _create_widgets(self):
        pass