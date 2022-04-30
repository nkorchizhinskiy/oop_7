from PyQt5.QtWidgets import QDialog


class Exercise_6(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        
    def _create_window(self):
        self.resize(400, 250)
