from PyQt5.QtWidgets import QDialog,\
                            QLabel,\
                            QRadioButton,\
                            QDoubleSpinBox,\
                            QMessageBox
                            


class Exercise_3(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        self._create_widgets()
        self._set_spinboxes_signals()
        self._set_radio_button_signal()
        
    def _create_window(self):
        self.resize(400, 250)

    def _create_widgets(self):
        #// Create Labels.
        self.label_data = QLabel("Данные для расчета", self)
        self.label_result = QLabel("Результат расчета", self)
        self.label_first_data = QLabel("A =", self)
        self.label_second_data = QLabel("B =", self)
        self.label_result_data = QLabel("Y =", self)
        self.label_choice = QLabel("Выберите способ расчета", self)
        
        #// Moving Labels.
        self.label_data.move(20, 10)
        self.label_result.move(250, 10)
        self.label_first_data.move(20, 40)
        self.label_second_data.move(20, 70)
        self.label_choice.move(20, 100)
        self.label_result_data.move(250, 100)
        self.label_result_data.resize(150, 70)

        #// Create spinboxes.
        self.spinbox_first_data = QDoubleSpinBox(self)
        self.spinbox_second_data = QDoubleSpinBox(self)

        self.spinbox_first_data.setButtonSymbols(2)
        self.spinbox_second_data.setButtonSymbols(2)
        
        self.spinbox_first_data.setMinimum(-10000)
        self.spinbox_first_data.setMaximum(10000)
        self.spinbox_second_data.setMinimum(-10000)
        self.spinbox_second_data.setMaximum(10000)
        
        self.spinbox_first_data.setValue(0)
        self.spinbox_second_data.setValue(0)
        
        #// Moving spinboxes.
        self.spinbox_first_data.move(50, 40)
        self.spinbox_second_data.move(50, 70)

        #// Create RadioButtons.
        self.radio_button_first_choice = QRadioButton("Y = A + B", self)
        self.radio_button_second_choice = QRadioButton("Y = A / B", self)
        self.radio_button_third_choice  = QRadioButton("Y = A * B", self)

        # self.radio_button_first_choice.setChecked(True)
        
        #// Moving Radiobuttons.
        self.radio_button_first_choice.move(20, 150)
        self.radio_button_second_choice.move(20, 180)
        self.radio_button_third_choice.move(20, 210)
    
    def _set_spinboxes_signals(self):
        self.spinbox_first_data.valueChanged.connect(self._calculate_value)
        self.spinbox_second_data.valueChanged.connect(self._calculate_value)
            
    def _set_radio_button_signal(self):
        self.radio_button_first_choice.toggled.connect(self._calculate_value)
        self.radio_button_second_choice.toggled.connect(self._calculate_value)
        self.radio_button_third_choice.toggled.connect(self._calculate_value)
    
    def _calculate_value(self):
        try:
            if self.radio_button_first_choice.isChecked():
                self.label_result_data.setText("Y = {}".format(
                    self.spinbox_first_data.value() + self.spinbox_second_data.value()
                ))
            elif self.radio_button_second_choice.isChecked():
                self.label_result_data.setText("Y = {}".format(
                    self.spinbox_first_data.value() / self.spinbox_second_data.value()
                ))
            elif self.radio_button_third_choice.isChecked():
                self.label_result_data.setText("Y = {}".format(
                    self.spinbox_first_data.value() * self.spinbox_second_data.value()
                ))
        except ZeroDivisionError:
            QMessageBox.warning(self, "Ошибка!", "Ошибка при делении на ноль!\n"\
                                "Этого делать нельзя!")
            self.spinbox_second_data.setValue(1)