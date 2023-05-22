import psycopg2
import sys
from PyQt5.QtWidgets import \
    (QApplication, QWidget, QTabWidget,
     QAbstractScrollArea, QVBoxLayout, QHBoxLayout,
     QTableWidget, QGroupBox, QTableWidgetItem,
     QPushButton, QMessageBox)

from functions import show_end_time
from consts import add_deleting_constraints_string, days_of_weeks_list, week_list, time_dict


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()

        self.setWindowTitle("Schedule")

        self.main_vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.main_vbox.addWidget(self.tabs)

        self._create_schedule_tab()
        self._create_teacher_tab()
        self._create_subject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(
            database="BVT2203_schedule",
            user="postgres",
            password="pantera377",
            host="localhost",
            port="3228"
        )
        self.cursor = self.conn.cursor()

    def _create_schedule_tab(self):
        self.schedule_tab = QWidget()
        self.tabs.addTab(self.schedule_tab, "Расписание")

        self.schedule_tab_vbox = QVBoxLayout(self)
        self.schedule_tab.setLayout(self.schedule_tab_vbox)

        self.weeks_tab = QTabWidget(self)  # weeks_tab
        self.schedule_tab_vbox.addWidget(self.weeks_tab)
        self._create_week_tab(0)
        self._create_week_tab(1)

    def _create_week_tab(self, is_week_even):
        exec("self.week_tab_{} = QWidget()".format(is_week_even))
        exec("self.weeks_tab.addTab(self.week_tab_{0}, week_list[{0}])"
             "".format(is_week_even))

        exec("self.week_tab_{}_vbox = QVBoxLayout(self)"
             "".format(is_week_even))
        exec("self.week_tab_{0}.setLayout(self.week_tab_{0}_vbox)"
             "".format(is_week_even))

        exec("self.week_tab_{}_hbox1 = QHBoxLayout()"
             "".format(is_week_even))
        exec("self.week_tab_{}_hbox2 = QHBoxLayout()"
             "".format(is_week_even))
        exec("self.week_tab_{}_hbox3 = QHBoxLayout()"
             "".format(is_week_even))
        exec("self.week_tab_{0}_vbox.addLayout(self.week_tab_{0}_hbox1)"
             "".format(is_week_even))
        exec("self.week_tab_{0}_vbox.addLayout(self.week_tab_{0}_hbox2)"
             "".format(is_week_even))
        exec("self.week_tab_{0}_vbox.addLayout(self.week_tab_{0}_hbox3)"
             "".format(is_week_even))

        for day in range(5):
            self._create_day_table(is_week_even, day)

        exec("self.update_week_{}_button = QPushButton('Обновить')"
             "".format(is_week_even))
        exec("self.week_tab_{0}_hbox3.addWidget(self.update_week_{0}_button)"
             "".format(is_week_even))
        exec("self.update_week_{}_button.clicked.connect(self._update_schedule_tab)"
             "".format(is_week_even))

    def _create_day_table(self, is_week_even, day):
        exec("self.day_{0}_{1}_gbox = QGroupBox(days_of_weeks_list[{1}])"
             "".format(is_week_even, day))
        if day <= 2:
            exec("self.week_tab_{0}_hbox1.addWidget(self.day_{0}_{1}_gbox)"
                 "".format(is_week_even, day))
        else:
            exec("self.week_tab_{0}_hbox2.addWidget(self.day_{0}_{1}_gbox)"
                 "".format(is_week_even, day))

        exec("self.day_{}_{}_table = QTableWidget()".format(is_week_even, day))
        exec("self.day_{}_{}_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)"
             "".format(is_week_even, day))

        exec("self.day_{}_{}_table.setColumnCount(7)"
             "".format(is_week_even, day))
        exec("self.day_{}_{}_table.setHorizontalHeaderLabels\
        (['ID', 'Время', 'Дисциплина', 'Преподаватель', 'Аудитория', '', ''])"
             "".format(is_week_even, day))

        self._update_day_table(is_week_even, day)

        exec("self.day_{}_{}_table_vbox = QVBoxLayout(self)".format(is_week_even, day))
        exec("self.day_{0}_{1}_table_vbox.addWidget(self.day_{0}_{1}_table)"
             "".format(is_week_even, day))
        exec("self.day_{0}_{1}_gbox.setLayout(self.day_{0}_{1}_table_vbox)"
             "".format(is_week_even, day))

    def _update_day_table(self, is_week_even, day):
        day_name = days_of_weeks_list[day]
        self.cursor.execute('''
                SELECT timetable.id, timetable.is_week_even, timetable.day, 
                subject.name, timetable.room, timetable.start_time, 
                teacher.full_name FROM timetable JOIN teacher on 
                timetable.subject_id = teacher.subject_id 
                JOIN subject on teacher.subject_id = subject.id 
                where is_week_even = {} and day ='{}' 
                order by timetable.start_time
                '''.format(is_week_even, day_name))
        records = list(self.cursor.fetchall())

        exec("self.day_{}_{}_table.setRowCount(len(records))".format(is_week_even, day))
        exec("self.day_{}_{}_table.setRowCount(len(records) + 1)".format(is_week_even, day))

        for i, r in enumerate(records):
            r = list(r)
            join_button = QPushButton("Изменить")
            delete_button = QPushButton("Удалить")  # создаем кнопку join

            exec("self.day_{}_{}_table.setItem(i, 0, QTableWidgetItem(str(r[0])))"
                 "".format(is_week_even, day))
            exec("self.day_{}_{}_table.setItem(i, 1, QTableWidgetItem"
                 "(str(r[5]) + ' — ' + show_end_time(str(r[5]), time_dict)))"
                 "".format(is_week_even, day))
            exec("self.day_{}_{}_table.setItem(i, 2, QTableWidgetItem(str(r[3])))"
                 "".format(is_week_even, day))
            exec("self.day_{}_{}_table.setItem(i, 3, QTableWidgetItem(str(r[6])))"
                 "".format(is_week_even, day))
            exec("self.day_{}_{}_table.setItem(i, 4, QTableWidgetItem(str(r[4])))"
                 "".format(is_week_even, day))
            exec("self.day_{}_{}_table.setItem(i, 0, QTableWidgetItem(str(r[0])))"
                 "".format(is_week_even, day))

            exec("self.day_{}_{}_table.setCellWidget(i, 5, join_button)"
                 "".format(is_week_even, day))
            join_button.clicked.connect\
                (lambda ch, num=i:
                 self._change_lesson_from_day_table(num, is_week_even, day))
            exec("self.day_{}_{}_table.setCellWidget(i, 6, delete_button)"
                 "".format(is_week_even, day))
            delete_button.clicked.connect\
                (lambda ch, num=i:
                 self._delete_lesson_from_day_table(num, is_week_even, day))

        insert_button = QPushButton("Добавить")
        exec("self.day_{}_{}_table.setCellWidget(len(records), 6, insert_button)"
             "".format(is_week_even, day))
        insert_button.clicked.connect\
            (lambda ch, num=len(records):
             self._insert_lesson_into_day_table(num, is_week_even, day))

        exec("self.day_{}_{}_table.resizeRowsToContents()".format(is_week_even, day))

    def _change_lesson_from_day_table(self, row_num, is_week_even, day):
        row = list()
        for i in range(7):
            try:
                exec("self.current_item = self.day_{}_{}_table.item(row_num, i).text()"
                     "".format(is_week_even, day))
                row.append(self.current_item)
            except:
                row.append(None)
        self.cursor.execute("select * from teacher where full_name='{}'".format(row[3]))
        try:
            list1 = list(self.cursor.fetchall())[0]
            teacher_full_name = list1[1]
            teacher_subject_id = list1[2]
        except:
            QMessageBox.about(self, "Error", "Enter existing teacher")

        self.cursor.execute("select * from subject where name='{}'".format(row[2]))
        try:
            timetable_subject_id = list(self.cursor.fetchall())[0][0]
        except:
            QMessageBox.about(self, "Error", "Enter existing subject")

        if timetable_subject_id:
            if timetable_subject_id == teacher_subject_id:
                # print(row[1][:5], timetable_subject_id, row[4], row[0])
                try:
                    self.cursor.execute(
                        "update timetable SET start_time='{0}', subject_id={1}, "
                        "room='{2}' where id={3};".format(
                            row[1][:5], timetable_subject_id, row[4], row[0]
                        ))
                    self.conn.commit()
                except:
                    QMessageBox.about(self, "Error", "Enter all fields")
            else:
                QMessageBox.about(self, "Error", "This teacher does not teach this subject!")

        self._update_day_table(is_week_even, day)

    def _delete_lesson_from_day_table(self, row_num, is_week_even, day):
        exec("self.lesson_id = str(self.day_{}_{}_table.item(row_num, 0).text())"
             "".format(is_week_even, day))

        try:
            self.cursor.execute('DELETE FROM timetable WHERE id={};'
                                ''.format(self.lesson_id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self._update_day_table(is_week_even, day)

    def _insert_lesson_into_day_table(self, row_num, is_week_even, day):
        row = list()
        for i in range(7):
            try:
                exec("self.current_item = self.day_{}_{}_table.item(row_num, i).text()"
                     "".format(is_week_even, day))
                row.append(self.current_item)
            except:
                row.append(None)

        self.cursor.execute("select * from subject where name='{}'"
                            "".format(row[2]))

        try:
            subject_id = list(self.cursor.fetchall())[0][0]
        except:
            QMessageBox.about(self, "Error", "Enter existing subject")

        try:
            self.cursor.execute(
                "INSERT INTO timetable(id, is_week_even, day, "
                "room, start_time, subject_id) "
                "VALUES ({}, {}, '{}', '{}', '{}', {})".format(
                    row[0], is_week_even, days_of_weeks_list[day],
                    row[4], row[1][:5], subject_id
                )
            )
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self._update_day_table(is_week_even, day)

    def _update_schedule_tab(self):
        for is_week_even in range(2):
            for day in range(5):
                self._update_day_table(is_week_even, day)

    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Преподаватели")

        self.teacher_tab_vbox = QVBoxLayout(self)
        self.teacher_tab_hbox1 = QHBoxLayout()
        self.teacher_tab_hbox2 = QHBoxLayout()

        self.teacher_tab_vbox.addLayout(self.teacher_tab_hbox1)
        self.teacher_tab_vbox.addLayout(self.teacher_tab_hbox2)

        self.teacher_gbox = QGroupBox("Преподаватели")
        self.teacher_tab_hbox1.addWidget(self.teacher_gbox)
        self._create_teacher_table()

        self.update_teacher_tab_button = QPushButton("Обновить")
        self.teacher_tab_hbox2.addWidget(self.update_teacher_tab_button)
        self.update_teacher_tab_button.clicked.connect(self._update_teacher_table)

        self.teacher_tab.setLayout(self.teacher_tab_vbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(
            ["ID", "Преподаватель", "Дисциплина", "", ""]
        )

        self._update_teacher_table()

        self.teacher_table_vbox = QVBoxLayout(self)
        self.teacher_table_vbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.teacher_table_vbox)

    def _update_teacher_table(self):
        self.cursor.execute('''
        SELECT teacher.id, teacher.full_name, subject.name from teacher 
        join subject on teacher.subject_id=subject.id
        ''')
        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records))
        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            join_button = QPushButton("Изменить")
            delete_button = QPushButton("Удалить")

            self.teacher_table.setItem\
                (i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem\
                (i, 1, QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem\
                (i, 2, QTableWidgetItem(str(r[2])))

            self.teacher_table.setCellWidget(i, 3, join_button)
            join_button.clicked.connect\
                (lambda ch, num=i:
                 self._change_teacher_from_table(num))
            self.teacher_table.setCellWidget(i, 4, delete_button)
            delete_button.clicked.connect\
                (lambda ch, num=i:
                 self._delete_teacher_from_table(num))

        insert_button = QPushButton("Добавить")
        self.teacher_table.setCellWidget(len(records), 4, insert_button)
        insert_button.clicked.connect\
            (lambda ch, num=len(records):
             self._insert_teacher_into_table(num))

        self.teacher_table.resizeRowsToContents()

    def _change_teacher_from_table(self, row_num):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(row_num, i).text())
            except:
                row.append(None)
        self.cursor.execute("select * from subject where name='{}'".format(row[2]))

        try:
            subject_id = list(self.cursor.fetchall())[0][0]
        except:
            QMessageBox.about(self, "Error", "Enter existing subject")

        try:
            self.cursor.execute("update teacher SET full_name='{0}', "
                                "subject_id={1} where id={2};"
                                "".format(row[1], subject_id, row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self._update_teacher_table()

    def _delete_teacher_from_table(self, row_num):
        teacher_id = str(self.teacher_table.item(row_num, 0).text())

        try:
            self.cursor.execute('DELETE FROM teacher WHERE id={};'
                                ''.format(teacher_id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self._update_teacher_table()

    def _insert_teacher_into_table(self, row_num):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(row_num, i).text())
            except:
                row.append(None)

        self.cursor.execute("select * from subject where name='{}'".format(row[2]))

        try:
            subject_id = list(self.cursor.fetchall())[0][0]
        except:
            QMessageBox.about(self, "Error", "Enter existing subject")

        try:
            self.cursor.execute("INSERT INTO teacher(id, full_name, subject_id) "
                                "VALUES ({}, '{}', {})".format(
                row[0], row[1], subject_id)
            )
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")

        self._update_teacher_table()

    def _create_subject_tab(self):
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Дисциплины")

        self.subject_tab_vbox = QVBoxLayout(self)
        self.subject_tab_hbox1 = QHBoxLayout()
        self.subject_tab_hbox2 = QHBoxLayout()

        self.subject_tab_vbox.addLayout(self.subject_tab_hbox1)
        self.subject_tab_vbox.addLayout(self.subject_tab_hbox2)

        self.subject_gbox = QGroupBox("Дисциплины")
        self.subject_tab_hbox1.addWidget(self.subject_gbox)
        self._create_subject_table()

        self.update_subject_tab_button = QPushButton("Обновить")
        self.subject_tab_hbox2.addWidget(self.update_subject_tab_button)
        self.update_subject_tab_button.clicked.connect(self._update_subject_table)

        self.subject_tab.setLayout(self.subject_tab_vbox)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(4)
        self.subject_table.setHorizontalHeaderLabels(["ID", "Дисциплина", "", ""])

        self._update_subject_table()

        self.subject_table_vbox = QVBoxLayout(self)
        self.subject_table_vbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.subject_table_vbox)

    def _update_subject_table(self):
        self.cursor.execute("SELECT * FROM subject ORDER BY name")
        records = list(self.cursor.fetchall())

        self.subject_table.setRowCount(len(records))
        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            join_button = QPushButton("Изменить")
            delete_button = QPushButton("Удалить")

            self.subject_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.subject_table.setItem(i, 1, QTableWidgetItem(str(r[1])))

            self.subject_table.setCellWidget(i, 2, join_button)
            join_button.clicked.connect\
                (lambda ch, num=i:
                 self._change_subject_from_table(num))
            self.subject_table.setCellWidget(i, 3, delete_button)
            delete_button.clicked.connect\
                (lambda ch, num=i:
                 self._delete_subject_from_table(num))

        insert_button = QPushButton("Добавить")
        self.subject_table.setCellWidget\
            (len(records), 3, insert_button)
        insert_button.clicked.connect\
            (lambda ch, num=len(records):
             self._insert_subject_into_table(num))

        self.subject_table.resizeRowsToContents()

    def _change_subject_from_table(self, row_num):
        subject_id = str(self.subject_table.item(row_num, 0).text())
        changed_subject_name = "'{}'".format(self.subject_table.item(row_num, 1).text())
        try:
            self.cursor.execute("update subject SET name={0} where id={1};"
                                "".format(changed_subject_name, subject_id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        self._update_subject_table()

    def _delete_subject_from_table(self, row_num):
        subject_id = str(self.subject_table.item(row_num, 0).text())
        delete_subject_string = add_deleting_constraints_string.format('''
                    DELETE FROM subject WHERE id={0}; 
                    DELETE FROM teacher WHERE subject_id={0}; 
                    DELETE FROM timetable WHERE subject_id={0};
                    ''')
        try:
            self.cursor.execute(delete_subject_string.format(subject_id))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        self._update_subject_table()

    def _insert_subject_into_table(self, row_num):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(row_num, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute\
                ("INSERT INTO subject(id, name) VALUES ({}, '{}')"
                 "".format(row[0], row[1]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields")
        self._update_subject_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
