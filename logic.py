from PyQt5.QtWidgets import QMainWindow,\
                            QPushButton,\
                            QSpinBox,\
                            QRadioButton,\
                            QCheckBox,\
                            QAction,\
                            QFrame,\
                            QMenuBar,\
                            QMenu



class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("Лабораторная №7")
        
        self._create_actions()
        self._create_menu_bar()
    
    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        
        #// Line Algorithm
        line_algorithm = QMenu("Линейный алгоритм", self)
        line_algorithm.addAction(self.exercise_1)
        line_algorithm.addAction(self.exercise_2)
        line_algorithm.addAction(self.exercise_3)
        line_algorithm.addAction(self.exercise_4)

        #// Branching
        branching = QMenu("Ветвления", self)
        branching.addAction(self.exercise_5)
        branching.addAction(self.exercise_6)

        #// Add to menu
        menu_bar.addMenu(line_algorithm)
        menu_bar.addMenu(branching)

        self.setMenuBar(menu_bar)
    
    def _create_actions(self):
        self.exercise_1 = QAction("Задание 1", self)
        self.exercise_2 = QAction("Задание 2", self)
        self.exercise_3 = QAction("Задание 3", self)
        self.exercise_4 = QAction("Задание 4", self)
        
        self.exercise_5 = QAction("Задание 5", self)
        self.exercise_6 = QAction("задание 6", self)