import sys
from PyQt5.QtWidgets import QDialog,\
                            QLabel,\
                            QCheckBox,\
                            QDoubleSpinBox,\
                            QMessageBox, \
                            QPushButton
                            


class Exercise_4(QDialog):
    
    def __init__(self):
        super().__init__()
        self._create_window()
        self._create_widgets()
        self._set_spinboxes_signals()
        self._set_checkbox_signal()
        
    def _create_window(self):
        self.resize(400, 250)
        self.setWindowTitle("X and Y and Z")

    def _create_widgets(self):
        #// Create Labels.
        self.label_data = QLabel("Данные для расчета", self)
        self.label_result = QLabel("Результат расчета", self)
        self.label_first_data = QLabel("A =", self)
        self.label_second_data = QLabel("B =", self)
        self.label_result_data = QLabel("Результат:", self)
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
        self.checkbox_first_choice = QCheckBox("X = A + B", self)
        self.checkbox_second_choice = QCheckBox("Y = A / B", self)
        self.checkbox_third_choice  = QCheckBox("Z = A * B", self)

        #// Moving Radiobuttons.
        self.checkbox_first_choice.move(20, 150)
        self.checkbox_second_choice.move(20, 180)
        self.checkbox_third_choice.move(20, 210)
        
        #// Exit button
        self.button_exit = QPushButton("Выход", self)
        self.button_exit.move(300, 200)
        self.button_exit.clicked.connect(lambda: self.close())
    
    def _set_spinboxes_signals(self):
        self.spinbox_first_data.valueChanged.connect(self._calculate_value)
        self.spinbox_second_data.valueChanged.connect(self._calculate_value)
            
    def _set_checkbox_signal(self):
        self.checkbox_first_choice.toggled.connect(self._calculate_value)
        self.checkbox_second_choice.toggled.connect(self._calculate_value)
        self.checkbox_third_choice.toggled.connect(self._calculate_value)
    
    def _calculate_value(self):
            result = ""
            if self.checkbox_first_choice.isChecked():
                    result += "X = " + str(self.spinbox_first_data.value() + self.spinbox_second_data.value()) + "\n"
            if self.checkbox_second_choice.isChecked():
                try:
                            result += "Y = " + str(self.spinbox_first_data.value() / self.spinbox_second_data.value()) + "\n"
                except ZeroDivisionError:
                    QMessageBox.warning(self, "Ошибка!", "Ошибка при делении на ноль!\n"\
                                        "Этого делать нельзя!")
                    self.checkbox_second_choice.setChecked(False)
            if self.checkbox_third_choice.isChecked():
                    result += "Z = " + str(self.spinbox_first_data.value() * self.spinbox_second_data.value())
            
            if result != "":
                self.label_result_data.setText(result)
            else:
                self.label_result_data.setText("Результат")