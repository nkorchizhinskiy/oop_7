from PyQt5.QtWidgets import QDialog,\
                            QLabel,\
                            QDoubleSpinBox,\
                            QSpinBox
                            


class Exercise_2(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        self._create_widgets()
        self._set_spinboxes_signals()
        
    def _create_window(self):
        self.resize(400, 250)
        self.setWindowTitle("Поиск расстояния и скорости")
        
    def _create_widgets(self):
        #// Create Labels
        self.label_data = QLabel("Исходные данные", self)
        self.label_result = QLabel("Результаты расчетов", self)
        self.label_start_speed = QLabel("Начальная\nскорость", self)
        self.label_acceleration = QLabel("Ускорение", self)
        self.label_time = QLabel("Время", self)
        self.label_result_data = QLabel("Конечная скорость:", self)
        self.label_distance = QLabel("Расстояние", self)

        #// Resize label, because content don't placed in.
        self.label_result_data.resize(200, 50)
        self.label_distance.resize(200, 50)

        #// Moving Labels
        self.label_data.move(30, 30)
        self.label_result.move(250, 30)
        self.label_start_speed.move(30, 100)
        self.label_acceleration.move(30, 150)
        self.label_time.move(30, 200)
        self.label_result_data.move(250, 100)
        self.label_distance.move(250, 200)

        #// Create spinboxes
        self.spinbox_start_speed = QDoubleSpinBox(self)
        self.spinbox_acceleration = QDoubleSpinBox(self)
        self.spinbox_time = QSpinBox(self)
        
        self.spinbox_start_speed.setButtonSymbols(2)
        self.spinbox_acceleration.setButtonSymbols(2)
        self.spinbox_time.setButtonSymbols(2)
        
        self.spinbox_start_speed.setMaximum(0)
        self.spinbox_start_speed.setMaximum(1000)
        self.spinbox_acceleration.setMaximum(0)
        self.spinbox_acceleration.setMaximum(1000)
        self.spinbox_time.setMinimum(0)
        self.spinbox_time.setMaximum(1000)
        
        #// Moving spinboxes
        self.spinbox_start_speed.move(100, 100)
        self.spinbox_acceleration.move(100, 150)
        self.spinbox_time.move(100, 200)
    
    def _set_spinboxes_signals(self):
        self.spinbox_start_speed.valueChanged.connect(self._calculate_value)
        self.spinbox_acceleration.valueChanged.connect(self._calculate_value)
        self.spinbox_time.valueChanged.connect(self._calculate_value)
            
    def _calculate_value(self):
        if self.spinbox_acceleration.value() != 0 and \
           self.spinbox_time.value() != 0:
               
            self.label_result_data.setText("Конечная скорость:\n{}".format(
                self.spinbox_start_speed.value() + self.spinbox_acceleration.value() * self.spinbox_time.value()
            ))

            self.label_distance.setText("Раастояние:\n{}".format(
                self.spinbox_start_speed.value() * self.spinbox_time.value() +
                (self.spinbox_acceleration.value() * self.spinbox_time.value() ** 2) / 2
            ))
        else:
            self.label_result_data.setText("Конечная скорость:")
            self.label_distance.setText("Расстояние:")