from PyQt5.QtWidgets import QMainWindow,\
                            QAction,\
                            QMenuBar,\
                            QMenu

#// Custom imports 
from dialog.exercise_1 import Exercise_1
from dialog.exercise_2 import Exercise_2
from dialog.exercise_3 import Exercise_3
from dialog.exercise_4 import Exercise_4
from dialog.exercise_5 import Exercise_5
from dialog.exercise_6 import Exercise_6



class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.setWindowTitle("Лабораторная №7")
        
        self._create_actions()
        self._create_menu_bar()
        self._connect_actions()
    
    def _create_menu_bar(self):
        menu_bar = QMenuBar(self)
        
        #// Line Algorithm.
        line_algorithm = QMenu("Линейный алгоритм", self)
        line_algorithm.addAction(self.open_exercise_1_action)
        line_algorithm.addAction(self.open_exercise_2_action)
        line_algorithm.addAction(self.open_exercise_3_action)
        line_algorithm.addAction(self.open_exercise_4_action)

        #// Branching.
        branching = QMenu("Ветвления", self)
        branching.addAction(self.open_exercise_5_action)
        branching.addAction(self.open_exercise_6_action)

        #// Add to menu.
        menu_bar.addMenu(line_algorithm)
        menu_bar.addMenu(branching)

        self.setMenuBar(menu_bar)
    
    def _create_actions(self):
        """Create actions to menubar's elements."""
        
        #// Line algorithm
        self.open_exercise_1_action = QAction("Задание 1", self)
        self.open_exercise_2_action = QAction("Задание 2", self)
        self.open_exercise_3_action = QAction("Задание 3", self)
        self.open_exercise_4_action = QAction("Задание 4", self)
        
        #// Branching
        self.open_exercise_5_action = QAction("Задание 5", self)
        self.open_exercise_6_action = QAction("задание 6", self)

    def _connect_actions(self):
        """Add signals to actions in menubar."""

        #// Connect Line Algorithm.
        self.open_exercise_1_action.triggered.connect(self.open_exercise_1)
        self.open_exercise_2_action.triggered.connect(self.open_exercise_2)
        self.open_exercise_3_action.triggered.connect(self.open_exercise_3)
        self.open_exercise_4_action.triggered.connect(self.open_exercise_4)

        #// Connect Branhing.
        self.open_exercise_5_action.triggered.connect(self.open_exercise_5)
        self.open_exercise_6_action.triggered.connect(self.open_exercise_6)

    #// Connecting functions.
    def open_exercise_1(self):
        self.window = Exercise_1()
        self.window.show()

    def open_exercise_2(self):
        self.window = Exercise_2()
        self.window.show()

    def open_exercise_3(self):
        self.window = Exercise_3()
        self.window.show()

    def open_exercise_4(self):
        self.window = Exercise_4()
        self.window.show()
    
    def open_exercise_5(self):
        self.window = Exercise_5()
        self.window.show()

    def open_exercise_6(self):
        self.window = Exercise_6()
        self.window.show()











