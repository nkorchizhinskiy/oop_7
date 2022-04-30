from PyQt5.QtWidgets import QDialog,\
                            QLabel,\
                            QFrame,\
                            QDoubleSpinBox
                            



class Exercise_1(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        self._create_widgets()
        self._set_spinboxes_signals()
        
    def _create_window(self):
        self.resize(400, 250)
        self.setWindowTitle("Поиск гипотенузы")
        
    def _create_widgets(self):
        #// Create Labels
        self.label_data = QLabel("Исходные данные", self)
        self.label_result = QLabel("Результаты расчетов", self)
        self.label_first_leg = QLabel("1-й катет", self)
        self.label_second_leg = QLabel("2-й катет", self)
        self.label_result_data = QLabel('Результат:', self)

        self.label_result_data.resize(200, 50)

        #// Moving Labels
        self.label_data.move(30, 30)
        self.label_result.move(250, 30)
        self.label_first_leg.move(30, 100)
        self.label_second_leg.move(30, 200)
        self.label_result_data.move(250, 100)

        #// Create spinboxes
        self.spinbox_first_leg = QDoubleSpinBox(self)
        self.spinbox_second_leg = QDoubleSpinBox(self)
        
        self.spinbox_first_leg.setButtonSymbols(2)
        self.spinbox_second_leg.setButtonSymbols(2)
        
        self.spinbox_first_leg.setMaximum(0)
        self.spinbox_first_leg.setMaximum(1000)
        self.spinbox_second_leg.setMaximum(0)
        self.spinbox_second_leg.setMaximum(1000)
        
        #// Moving spinboxes
        self.spinbox_first_leg.move(100, 100)
        self.spinbox_second_leg.move(100, 200)
    
    def _set_spinboxes_signals(self):
        self.spinbox_first_leg.valueChanged.connect(self._calculate_value)
        self.spinbox_second_leg.valueChanged.connect(self._calculate_value)
            
    def _calculate_value(self):
        if self.spinbox_first_leg.value() != 0 and self.spinbox_second_leg.value() != 0:
            self.label_result_data.setText("Гипотенуза:\n{}".format(self.spinbox_first_leg.value()**2
                                                                    +
                                                                    self.spinbox_second_leg.value()**2))
        else:
            self.label_result_data.setText("Результат:")
        

    
        
        
        