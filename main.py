

from pathlib import Path



import pdfkit

import mysql.connector

from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.uix.picker import MDDatePicker
from kivymd.uix.datatables import MDDataTable
from kivymd.theming import ThemeManager

from kivymd.app import MDApp

from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.metrics import dp
import pandas as pd
from kivy.uix.anchorlayout import AnchorLayout

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

import os

from multiprocessing import Process



from logging import Logger

'''class FlaskThread(Thread):
    def run(self):
        Logger.manager.loggerDict['werkzeug'] = Logger.manager.loggerDict['kivy']
        app.run(
            host='127.0.0.1', port=8200, debug=True, use_debugger=True,
            use_reloader=False)'''


###########################################################
class SplashScreen(Screen):
    pass


class LoginIn(Screen):
    def login(self):
        '''login = self.ids.login.text
        passw = self.ids.password.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("""SELECT login, password FROM auth WHERE login=%s AND password=%s""")

        mycursor.execute(query, (login, passw))

        myresult = mycursor.fetchone()
        for x in myresult:
            if login == x[0] and passw == x[1]:
                self.manager.current == 'navigationDrawer'
                # root.manager.current == 'navigationDrawer'
            else:
                self.manager.current == 'navigationDrawer'

        mydb.commit()
        mydb.close()'''
        pass

    '''layout = AnchorLayout()
        columns = [('ID_Examen', dp(40)), ('Examen_Name', dp(40)), ('Score', dp(40))]
        for i in range(3):
            rows = [x[i] for x in myresult]

        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            check=True,
            # row_data=[{'text': str(x)} for x in myresult],
            column_data=columns,
            row_data=rows,
        )
        self.add_widget(self.data_tables)
        return layout

    def on_press(self, *args):
        self.load_table()'''


class Content(BoxLayout):
    def fetch_button(self):
        '''name = self.ids.NameExamen.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT ExamName,score FROM exam WHERE ExamName=%s"""
        mycursor.execute(query, (name,))
        data = mycursor.fetchall()

        for x in data:
            self.ids.Nexamen.text = x[0]
            self.ids.score.text = str(x[1])
        mydb.commit()'''
        pass


class NavigationDrawer(Screen):
    # def __init__(self, **kwargs):
    # super(NavigationDrawer, self).__init__(**kwargs)
    # Window.bind(on_request_close=self.endFunction)
    # self.add_widget(self.content)
    # clock.schedule_interval(self.game.update, 1.0 / 60.0)
    '''@app.route('/')
    def HtmlEnrolleeData(self):
        file= filedialog.askopenfile()
        os.open("C:\\Users\\dell\\PycharmProjects\\CourseWork\\SMS Data Report-1.pdf", os.O_RDONLY)'''

    def load_table(self):
        '''name = self.ids.NameText.text
        phone = self.ids.phone.text
        picture = self.ids.picture.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("INSERT INTO enrollee "
                 "(FullName, phone, id_photo_fk) "
                 "VALUES (%s, %s, %s)")
        val = (name, phone, picture)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def on_press(self, *args):
        self.load_table()
        pass

    def fetch_data(self):
        '''if self.ids.NameText.text == '':
            print('Fill the full name or the number of enrollee')
        name = self.ids.NameText.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT phone,id_photo_fk FROM enrollee WHERE FullName=%s"""
        mycursor.execute(query, (name,))
        data = mycursor.fetchall()

        for x in data:
            self.ids.phone.text = x[0]
            self.ids.picture.text = str(x[1])
        mydb.commit()'''
        pass

    def update_data(self):
        '''name = self.ids.NameText.text
        phone = self.ids.phone.text
        picture = self.ids.picture.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """UPDATE enrollee SET FullName=%s,phone=%s,id_photo_fk=%s WHERE FullName=%s"""
        mycursor.execute(query, (name, phone, picture, name))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")'''
        pass

    def delete_data(self):
        '''name = self.ids.NameText.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """delete from enrollee WHERE FullName=%s"""
        mycursor.execute(query, (name,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")'''
        pass


    ################################### 2nd Screen #############################
    def fetch_Examen(self):
        '''IDE = str(self.ids.idExam.text)
        IDEN = self.ids.ExamName.text
        IDS = self.ids.ScoreExamen.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT * FROM exam WHERE id_exam=%s"""
        mycursor.execute(query, (IDE,))
        myresult = mycursor.fetchall()
        for x in myresult:
            self.ids.idExam.text = str(x[0])
            self.ids.ExamName.text = x[1]
            self.ids.ScoreExamen.text = str(x[2])'''

    def insert_Examen(self):
        '''IDE = str(self.ids.idExam.text)
        IDEN = self.ids.ExamName.text
        IDS = self.ids.ScoreExamen.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("INSERT INTO exam"
                 "(id_exam, ExamName, score) "
                 "VALUES (%s, %s, %s)")
        val = (IDE, IDEN, IDS)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def update_Examen(self):
        '''IDE = str(self.ids.idExam.text)
        IDEN = self.ids.ExamName.text
        IDS = self.ids.ScoreExamen.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """UPDATE exam SET id_exam=%s,ExamName=%s,score=%s WHERE id_exam=%s"""
        mycursor.execute(query, (IDE, IDEN, IDS, IDE))
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")'''
        pass

    def delete_Examen(self):
        '''IDE = self.ids.idExam.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """delete from exam WHERE id_exam=%s"""
        mycursor.execute(query, (IDE,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")'''
        pass

    def showExamenPdf(self):
        '''import pandas as pd
        CSV = pd.read_csv('examen.csv')

        CSV.to_html('examen.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('examen.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''

        pass

    def show_datepicker(self):
        '''picker = MDDatePicker()
        picker.open()'''
        pass

    def display_examen(self):
        '''mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM exam")
        myresult = mycursor.fetchall()
        mydb.commit()
        mydb.close()
        layout = AnchorLayout()
        columns = [('ID_Examen', dp(40)), ('Examen_Name', dp(40)), ('Score', dp(40))]
        rows = [(x[0], x[1], x[2]) for x in myresult]
        self.data_tables = MDDataTable(

            pos_hint={'center_y': 0.5, 'center_x': 0.2},
            size_hint=(0.9, 0.2),
            use_pagination=True,
            check=True,
            column_data=columns,
            row_data=rows, )
        # background_color_header = get_color_from_hex("#65275d"))

        # background_color_header= get_color_from_hex("#65275d"),

        self.add_widget(self.data_tables)
        # self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        print(len(columns))
        return layout'''
        pass

    def on_check_press(self, instance_table, current_row):
        '''print(instance_table, current_row)
        self.ids.idExam.text = current_row[0]
        self.ids.ExamName.text = current_row[1]
        self.ids.ScoreExamen.text = current_row[2]

        # self.data_tables.disabled = True
        # self.data_tables.theme_cls = 'Green'''

    def sort_on_signal(self, data):
        '''return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))'''

    def sort_on_schedule(self, data):
        '''return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )'''
        pass

    def sort_on_team(self, data):
        '''return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))'''
        pass

    def update_examen(self):
        '''if not self.dialog:
            self.dialog = MDDialog(
                title="Fetch and Update:",
                type="custom",
                content_cls=Content(),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                buttons=[
                    MDRectangleFlatButton(
                        text="Fetch Data",
                        theme_text_color="Custom", on_bind=self.fetch_button()
                    ),
                    MDRectangleFlatButton(
                        text="Update",
                        theme_text_color="Custom", ),
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",

                    ),
                ],
            )
        self.dialog.open()  #'''
        pass

    def fetch_button(self):
        '''name = self.ids.NameExamen.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT ExamName,score FROM exam WHERE ExamName=%s"""
        mycursor.execute(query, (name,))
        data = mycursor.fetchall()

        for x in data:
            self.ids.Nexamen.text = x[0]
            self.ids.score.text = str(x[1])
        mydb.commit()'''
        pass



    # @app.route('')
    def endFunction(self):
        pass
        # App.get_running_app().stop()

    # @app.route()
    '''def print_data(self):
        app.run('127.0.0.1', port=8200, debug=True, use_reloader=False, threaded=True)
        pass'''

    ##################################################### screen 3############################
    def show_faculty(self):
        '''mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        # SELECT `name`, `term` from `speciality`, `theplan` where `id_plan`= `id_group_fk`;
        mycursor.execute("SELECT name, term from speciality, theplan where id_plan= id_group_fk")
        myresult = mycursor.fetchall()
        mydb.commit()
        mydb.close()
        layout = AnchorLayout()
        columns = [('term', dp(70)), ('speciality', dp(70))]
        rows = [(x[0], x[1]) for x in myresult]
        print(myresult)
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            check=True,
            column_data=columns,
            row_data=rows,

        )
        self.add_widget(self.data_tables)
        print(len(columns))
        return layout
        # background_color_header= get_color_from_hex("#65275d"),'''
        pass

    def DisplayFaculty(self):
        '''absolutePath = Path('C:\\Users\\dell\\PycharmProjects\\CourseWork\\faculties.xlsx').resolve()
        os.system(f'start excel.exe "{absolutePath}"')
        cur_path = os.path.dirname(__file__)

        new_path = os.path.relpath('C:\\Users\\dell\\PycharmProjects\\CourseWork\\Faculties.xlsx', cur_path)
        with open(new_path, 'r') as f:
            f.read()'''
        pass

    def FetchFaculty(self):
        '''mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT id_speciality,name, term from speciality, theplan, faculty where 
          id_plan=id_group_fk """
        mycursor.execute(query)
        data = mycursor.fetchall()

        mydb.commit()'''
        pass

    def UpdateFaculty(self):
        '''if self.ids.IdSpeciality.text == '':
            print('Fill the Speciality')
        idSpeciality = str(self.ids.IdSpeciality.text)
        nameS = str(self.ids.nameS.text)
        termS = str(self.ids.termS.text)
        nameF = str(self.ids.nameF.text)
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        # FROM
        ##speciality, theplan, faculty
        mycursor = mydb.cursor()
        query = ("UPDATE speciality "
                 "(SET id_speciality=%s,speciality.name=%s) "
                 "where id_speciality=%s")
        query2 = ("UPDATE theplan "
                  "(term) "
                  "VALUES (%s)")
        query3 = ("INSERT INTO faculty "
                  "(faculty.name) "
                  "VALUES (%s)")
        val = (idSpeciality, nameS)
        val2 = (termS)
        val3 = (nameF)
        mycursor.execute(query, val)
        mycursor.execute(query2, val2)
        mycursor.execute(query3, val3)
        data = mycursor.fetchall()
        for x in data:
            self.ids.IdSpeciality.text = str(x[0])
            self.ids.nameS.text = x[1]
            self.ids.termS.text = x[2]
            self.ids.nameF.text = x[3]
        mydb.commit()
        print(x)'''
        pass

    def Insert_Faculty(self):
        '''idSpeciality = str(self.ids.IdSpeciality.text)
        nameS = str(self.ids.nameS.text)
        termS = str(self.ids.termS.text)
        nameF = str(self.ids.nameF.text)
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("INSERT INTO speciality "
                 "(id_speciality,speciality.name) "
                 "VALUES (%s, %s)")
        query2 = ("INSERT INTO theplan "
                  "(term) "
                  "VALUES (%s)")
        query3 = ("INSERT INTO faculty "
                  "(faculty.name) "
                  "VALUES (%s)")
        val = (idSpeciality, nameS)
        val2 = (termS)
        val3 = (nameF)
        mycursor.execute(query, val)
        mycursor.execute(query2, val2)
        mycursor.execute(query3, val3)
        mydb.commit()'''
        pass

    ########################## SCreen 4 Questionnaire #############################
    def FetchQuestionnaire(self):
        # self.ids.idquest.text
        # self.ids.IdEnrollee.text
        # self.ids.IdFacultytext
        # self.ids.IdSched.text
        # self.ids.IdEmp.text

        '''idq = self.ids.idquest.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT * FROM questionnaire WHERE id_questionnaire=%s"""
        mycursor.execute(query, (idq,))
        data = mycursor.fetchall()

        for x in data:
            self.ids.idquest.text = str(x[0])
            self.ids.IdEnrollee.text = str(x[1])
            self.ids.IdFaculty.text = str(x[2])
            self.ids.IdSched.text = str(x[3])
            self.ids.IdEmp.text = str(x[4])
        mydb.commit()'''
        pass

    def InsertQuestionnaire(self):
        '''IDQ = self.ids.idquest.text
        IDE = self.ids.IdEnrollee.text
        IDF = self.ids.IdFaculty.text
        IDS = self.ids.IdSched.text
        IDEM = self.ids.IdEmp.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("INSERT INTO questionnaire "
                 # "(id_questionnaire,id_enrollee_fk, id_faculty_fk,phone, id_photo_fk) "
                 "VALUES (%s, %s, %s,%s,%s)")
        val = (IDQ, IDE, IDF, IDS, IDEM)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def UpdateQuestionnaire(self):
        '''IDQ = self.ids.idquest.text
        IDE = self.ids.IdEnrollee.text
        IDF = self.ids.IdFaculty.text
        IDS = self.ids.IdSched.text
        IDEM = self.ids.IdEmp.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("UPDATE questionnaire "
                 "SET id_questionnaire=%s,id_enrollee_fk=%s, id_faculty_fk=%s,id_schedule_fk=%s,id_employee_fk=%s "
                 "Where id_questionnaire=%s")
        val = (IDQ, IDE, IDF, IDS, IDEM, IDQ)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def DeleteQuestionnaire(self):
        '''IDQ = self.ids.idquest.text
        IDE = self.ids.IdEnrollee.text
        IDF = self.ids.IdFaculty.text
        IDS = self.ids.IdSched.text
        IDEM = self.ids.IdEmp.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """delete from questionnaire WHERE id_questionnaire=%s"""
        mycursor.execute(query, (IDQ,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")'''
        pass

    def ShowAllQuestionnaire(self):
        pass

    ########################## SCreen 4 Examen Result #############################
    def FetchExamenResult(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT * FROM examresult WHERE id_result=%s"""
        mycursor.execute(query, (IDR,))
        data = mycursor.fetchall()

        for x in data:
            self.ids.IdResult.text = str(x[0])
            self.ids.IdSchedule.text = str(x[1])
            self.ids.Marks.text = str(x[2])

        mydb.commit()'''

        pass

    def InsertExamenResult(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """"INSERT INTO examresult VALUES (%s, %s, %s)"""
        mycursor.execute(query, (IDR, IDS, IDM))
        mydb.commit()'''
        pass

    def UpdateExamenResult(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("UPDATE examresult SET id_result=%s,id_schedule=%s, grade=%s Where id_result=%s")
        val = (IDR, IDS, IDM, IDR)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass


    def DeleteExamenResult(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """delete from examresult WHERE id_result=%s"""
        mycursor.execute(query, (IDR,))
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")'''
        pass

    def ShowAllExamenResult(self):
        pass

    ####################### Screen 4 Examen Schedule####################
    def FetchExamenSchedule(self):
        '''IDES = self.ids.idExamSched.text
        IDS = self.ids.StreamN.text
        IDI = self.ids.IdExamen1.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """SELECT * FROM examschedule WHERE id_examschedule=%s"""
        mycursor.execute(query, (IDES,))
        data = mycursor.fetchall()
        for x in data:
            self.ids.idExamSched.text = str(x[0])
            self.ids.StreamN.text = str(x[1])
            self.ids.IdExamen1.text = str(x[2])'''

        pass

    def InsertExamenSchedule(self):
        '''IDES = self.ids.idExamSched.text
        IDS = self.ids.StreamN.text
        IDI = self.ids.IdExamen1.text
        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = """INSERT INTO examschedule VALUES (%s, %s, %s)"""
        mycursor.execute(query, (IDES, IDS, IDI))
        mydb.commit()'''
        pass

    def UpdateExamenSchedule(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        query = ("UPDATE examschedule SET id_examschedule=%s,StreamNumber=%s, id_exam_fk=%s Where id_examschedule=%s")
        val = (IDR, IDS, IDM, IDR)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def DeleteExamenSchedule(self):
        '''IDR = self.ids.IdResult.text
        IDS = self.ids.IdSchedule.text
        IDM = self.ids.Marks.text

        mydb = mysql.connector.connect(
            host="localhost",
            user="majda",
            passwd="98Majdajan98",
            database="majda", )
        mycursor = mydb.cursor()
        # delete from examresult WHERE id_result=%s"
        query = ("delete from examschedule Where id_examschedule=%s")
        val = (IDR)
        mycursor.execute(query, val)
        mydb.commit()'''
        pass

    def ShowAllExamenSchedule(self):
        '''import pandas as pd
        CSV = pd.read_csv('examen.csv')

        CSV.to_html('examen.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('examen.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass

    ####################### join 1 Screen 4 ###############################
    def Join1(self):
        '''import pandas as pd

        CSV = pd.read_csv('Questionnaire.csv')

        CSV.to_html('Questionnaire.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('Questionnaire.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass

    def Join2(self):

        '''
        CSV = pd.read_csv('ExamenResult.csv')

        CSV.to_html('ExamenResult.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('ExamenResult.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass

    def Join3(self):
        '''
        CSV = pd.read_csv('ExamenSchedule.csv')

        CSV.to_html('ExamenSchedule.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('ExamenSchedule.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass

    def PrintAll(self):



        pass



    ############################################################Last window ######################
    def employee_Information(self):
        '''import pandas as pd
        CSV = pd.read_csv('EmployeePdf.csv')

        CSV.to_html('EmployeePdf.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('EmployeePdf.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass
    def enrolle_Information(self):
        '''import pandas as pd
        CSV = pd.read_csv('enrolle.csv')

        CSV.to_html('enrolle.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('enrolle.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass
    def Global_examen_Results(self):
        '''import pandas as pd
        CSV = pd.read_csv('GlobalRes.csv')

        CSV.to_html('GlobalRes.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('GlobalRes.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass
    def enrollement_details(self):
        '''import pandas as pd
        CSV = pd.read_csv('EnrollementDetails.csv')

        CSV.to_html('EnrollementDetails.html')
        config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
        for file in glob.glob('EnrollementDetails.html'):
            pdfkit.from_file(file, file[:-4] + '.pdf', configuration=config)'''
        pass





class NavigationLayout(Screen):
    pass


class WindowManager(ScreenManager):
    sm = ScreenManager()
    sm.add_widget(LoginIn(name='Login'))
    sm.add_widget(NavigationDrawer(name='navigationDrawer'))


class MyMainApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    class Content(BoxLayout):
        pass

    def build(self):
        dialog = None
        global root
        root = self.root
        theme_cls = ThemeManager()
        # MyMainApp.on_start(self)
        # self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
         '''
WindowManager:
    SplashScreen:
    LoginIn:
    NavigationDrawer:
    #ClientsTable:


<SplashScreen>:
    Button:
        background_normal:'./assets/signInLogo.png'
        background_down:'./assets/signInLogo.png'
        size_hint:.26,.26
        pos_hint:{'center_x':.5, 'center_y':.55}
        on_press:
            #root.on_press()
            root.manager.current='Login'
<LoginIn>:
    name:'Login'
    GridLayout:
        cols:1
        size_hint:0.6, 0.7
        pos_hint:{'center_x':0.5,'center_y':0.5 }
        Image:
            source:'./assets/signInLogo.png'
            size_hint:1.5,1.5
            pos_hint:{'center_x':0.5 }
            padding_y:20
        Label:
            id:'login'
            text: 'What is Your Login ?'
            font_size:20
            color:'#00FFCE'
        TextInput:
            id:login
            multiline:False
            padding_y:10,1
            size_hint:1,0.5
            pos_hint:{'center_x':0.5, 'center_y':0.9}
            cursor_color:0,0,0,1
            cursor_width:"2sp"
        Label:
            id:'password'
            text: 'What is Your Password ?'
            font_size:20
            color:'#00FFCE'
        TextInput:
            id:password
            multiline:False
            padding_y:20,1
            size_hint:0.5,0.5
            pos_hint:{'center_x':0.5, 'center_y':0.9}
            icon:'zmdi-account'
            password:True
        Label:
            id:'passw'
            font_size:20
            color:'#00FFCE'
        Button:
            text:'Sign in'
            bold:True
            font_size:20
            background_color:'#00FFCE'
            pos_hint:{'center_x':0.5, 'center_y':0.9}
            size_hint:0.5,0.7
            on_release:
                #root.login()
                root.manager.current='navigationDrawer'

<NavigationDrawer>:
    name:'navigationDrawer'
    NavigationLayout:
        ScreenManager:
            id:screen_manager
            Screen:
                canvas.before:
                    Color:
                    #rgba:(0, 255, 255, .5)pistash
                    #rgba:(0, 0, 255, 0.3)blue
                    #rgba:(0, 0, 255, 0.1) dark blue
                    #rgba:(30,255,50,0.5)grey
                        rgba:((0, 0, 255, 0.1))
                    Rectangle:
                        pos:self.pos
                        size:self.size
                name: "s1"
                GridLayout:
                    cols: 1
                    BoxLayout:
                        #pos_hint:{'center_x':0.5,'center_y':0.5 }
                        #size_hint:0.5, 1
                        orientation:'vertical'
                        spacing:"8dp"
                        padding:"8dp"
                        Label:
                            #pos_hint:{'center_x':0.5,'center_y':7 }
                            text: 'Registration Form'
                            font_size:30
                            background_color:'#D81CD5'
                            bold:True

                        Label:
                            text:'FullName:'
                            font_size:20
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                        TextInput:
                            size_hint:0.7, 1
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                            font_size:15
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            id:NameText
                            multiline:False
                            cursor_color:0,0,0,1
                            cursor_width:"2sp"
                            multiline:False
                            hint_text:'Enter The Full Name'
                        Label:
                            font_size:20
                            text:'Phone Number:'
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                        TextInput:
                            id:phone
                            size_hint:0.7, 1
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                            hint_text:'Enter The phone number'
                            font_size:15
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                        Label:
                            font_size:20
                            text:'Picture Id:'
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                        TextInput:
                            id:picture
                            size_hint:0.7, 1
                            #pos_hint:{'center_x':0.5,'center_y':0.3 }
                            pos_hint:{'center_x':0.5,'center_y':5 }
                            font_size:15
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            hint_text:'Enter The photo Id'

                        Label:
                            text:''
                        Button:
                            id:'Register'
                            text:'Register'
                            size_hint:0.7, 1
                            pos_hint:{'center_x':0.5,'center_y':5 }
                            font_size:20
                            #D81CD5
                            background_color:'#BF22BC'
                            bold:True
                            on_release:root.on_press()
                        Button:
                            id:'Fetch'
                            text:'Fetch'
                            size_hint:0.7, 1
                            pos_hint:{'center_x':0.5,'center_y':5 }
                            font_size:20
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            on_release:root.fetch_data()
                        Button:

                            id:'Update'
                            size_hint:0.7, 1
                            text:'Update'
                            pos_hint:{'center_x':0.5,'center_y':5 }
                            font_size:20
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            on_release:root.update_data()
                        Button:

                            id:'delete'
                            size_hint:0.7, 1
                            text:'Delete'
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                            font_size:20
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            on_release:root.delete_data()
                        Button:
                            id:'fetch photo'
                            size_hint:0.7, 1
                            text:'Fetch photo'
                            pos_hint:{'center_x':0.5,'center_y':0.5 }
                            font_size:20
                            #D81CD5
                            background_color:'#E985E7'
                            bold:True
                            on_release:root.fetch_photo()
                        Label:
                            text:''


            Screen:
                canvas.before:
                    Color:
                    #rgba:(0, 255, 255, .5)pistash
                    #rgba:(0, 0, 255, 0.3)blue
                    #rgba:(0, 0, 255, 0.1) dark blue
                    #rgba:(30,255,50,0.5)grey
                        rgba:(80,80,80,80)
                    Rectangle:
                        pos:self.pos
                        size:self.size
                name: "s2"
                GridLayout:
                    cols:1
                    pos_hint:{'center_x':0.5, 'center_y':0.5}
                    padding: '8dp'
                    spacing: '8dp'
                    BoxLayout:
                        orientation:'vertical'
                        pos_hint:{'center_x':0.5, 'center_y':0.5}
                        padding: '8dp'
                        spacing: '8dp'
                        Label:
                            text: 'Enrollee Examen Data'
                            font_size: 30
                            color:'#9400d3'
                            #pos_hint:{'center_x':1, 'center_y':1}
                        Label:
                            id:'idExam'
                            text: 'Id Exam'
                            font_size:20
                            color:'#483d8b'
                            #pos_hint:{'center_x':1, 'center_y':1}
                        TextInput:
                            id:idExam
                            background_color:'#C0C0C0'
                            multiline:False
                            #padding_y:10,2
                            size_hint:.5,0.5
                            #height: self.minimum_height
                            pos_hint:{'center_x':0.5, 'center_y':0.5}
                            background_color:'#C0C0C0'
                            #size_hint:0.5,0.5
                        #pos_hint:{'center_x':0.5, 'center_y':0.9}
                            cursor_color:0,0,0,1
                            cursor_width:"2sp"
                            multiline:False
                        Label:
                            #id:'ExamName'
                            text: 'ExamName'
                            font_size:20
                            color:'#483d8b'
                            #pos_hint:{'center_x':1, 'center_y':1}
                        TextInput:
                            id:ExamName
                            size_hint:.5,0.5
                            multiline:False
                            #padding_y:10,2
                            #size_hint:.1,0.9
                            #height: self.minimum_height
                            #pos_hint:{'center_x':0.5, 'center_y':0.2}
                            #size_hint:0.5,0.5
                            #pos_hint:{'center_x':0.5, 'center_y':0.9}
                            cursor_color:0,0,0,1
                            cursor_width:"2sp"
                            multiline:False
                            pos_hint:{'center_x':0.5, 'center_y':0.5}
                            background_color:'#C0C0C0'
                        Label:
                            text: 'Exam Score'
                            font_size:20
                            color:'#483d8b'
                            #pos_hint:{'center_x':1, 'center_y':1}
                        TextInput:
                            id:ScoreExamen
                            size_hint:.5,0.5
                            multiline:False
                            #padding_y:10,2
                            #size_hint:.1,0.9
                            #height: self.minimum_height
                            #pos_hint:{'center_x':0.5, 'center_y':0.2}
                            #size_hint:0.5,0.5
                            #pos_hint:{'center_x':0.5, 'center_y':0.9}
                            cursor_color:0,0,0,1
                            cursor_width:"2sp"
                            multiline:False
                            pos_hint:{'center_x':0.5, 'center_y':0.5}
                            background_color:'#C0C0C0'
                        BoxLayout:
                            padding:'8dp'
                            spacing:'8dp'
                            Button:
                                text:'Fetch'
                                background_color:'#556b2'
                                on_release:root.fetch_Examen()
                            Button:
                                text:'Insert'
                                background_color:
                                on_release:root.insert_Examen()
                            Button:
                                text:'Update'
                                background_color:'#2f4f4f'
                                on_release:root.update_Examen()
                            Button:
                                text:'Delete'
                                background_color:'#e9967a'
                                on_release:root.delete_Examen()
                            Button:
                                text:'Show all'
                                background_color:'#8fbc8f'
                                on_release:root.showExamenPdf()

            Screen:
                name: "s3"
                GridLayout:
                    cols:1
                    #size_hint:0.6, 0.7
                    #pos_hint:{'center_x':0.5,'center_y':0.5 }
                    Label:
                        text: 'Faculties and Specialities'
                        pos_hint:{'center_x':0.5,'center_y':1 }
                        font_size:30
                        background_color:'#ff1493'
                        bold:True
                    BoxLayout:
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        orientation: 'vertical'
                        padding: "8dp"
                        spacing: "8dp"
                        TextInput:
                            id:IdSpeciality
                            hint_text:'Id Speciality'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            #size_hint:1, 0.5
                            size_hint:0.5,0.3
                        TextInput:
                            id:nameS
                            hint_text:'Name Speciality'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.5, 0.3
                        TextInput:
                            id:termS
                            hint_text:'Term Speciality'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.5, 0.3
                        TextInput:
                            id:nameF
                            hint_text:'Name Faculty'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.5, 0.3
                        TextInput:
                            id:nameF
                            hint_text:'Name Faculty'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.5, 0.3
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Button:
                            text:'Show All Data'
                            size_hint:0.5, 0.5
                            background_color: 1, .3, .4, .85
                            on_release: root.DisplayFaculty()
                        Button:
                            text:'Show in Table'
                            size_hint:0.5, 0.5
                            #background_color:170, 141, 96
                            on_release:root.show_faculty()
                        Button:
                            text:'Update Data'
                            size_hint:0.5, 0.5
                            #background_color:236, 221, 46
                            on_release:root.UpdateFaculty()
                        Button:
                            text:'Delete Data'
                            size_hint:0.5, 0.5
                            #background_color: 142, 65, 134
                            on_release:root.FetchFaculty()
                        Button:
                            text:'Insert Data'
                            size_hint:0.5, 0.5
                            #background_color:133, 96, 170
                            on_release:root.Insert_Faculty()




            Screen:
                name: "s4"
                GridLayout:
                    #size_hint:0.6, 0.7
                    #pos_hint:{'center_x':0.5,'center_y':0.5 }
                    cols:1
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        orientation:'horizontal'
                        background_color:.8, .8, 0, 1
                        Label:
                            text: 'Questionnaire'
                        TextInput:
                            id:idquest
                            hint_text:'IdQuestio'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.7, 0.5

                        TextInput:
                            id:IdEnrollee
                            hint_text:'Id_Enrollee'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.7, 0.5
                        TextInput:
                            id:IdFaculty
                            hint_text:'Id Faculty'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.7, 0.5

                        TextInput:
                            id:IdSched
                            hint_text:'Id Schedule'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.7, 0.5
                        TextInput:
                            id:IdEmp
                            hint_text:'Id Employee'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.7, 0.5
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Button:
                            size_hint:0.7, 0.5
                            text:'Fetch One'
                            on_release:on_release: root.FetchQuestionnaire()
                        Button:
                            text:'Insert'
                            size_hint:0.7, 0.5
                            background_color:'#E9967A'
                            on_release: root.InsertQuestionnaire()
                        Button:
                            text:'Update'
                            size_hint:0.7, 0.5
                            on_release: root.UpdateQuestionnaire()
                            background_color:'#9932CC'
                        Button:
                            text:'Delete'
                            size_hint:0.7, 0.5
                            on_release: root.DeleteQuestionnaire()
                            background_color:'#8B008B'
                        Button:
                            text:'Show All'
                            size_hint:0.7, 0.5
                            on_release: root.ShowAllQuestionnaire()
                            background_color:'#BDB76B'
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Label :
                            text:'Examen Result'
                        TextInput:
                            id:IdResult
                            hint_text:'Id Result'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.9, 0.5
                        TextInput:
                            id:IdSchedule
                            hint_text:'Id Schedule'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.9, 0.5

                        TextInput:
                            id:Marks
                            hint_text:'Marks'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:0.9, 0.5
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Button:
                            text:'Fetch One'
                            size_hint:0.7, 0.5
                            on_release:root.FetchExamenResult()
                            background_color:'#008B8B'
                        Button:
                            text:'Insert'
                            size_hint:0.7, 0.5
                            on_release:root.InsertExamenResult()
                            background_color:'#B8860B'
                        Button:
                            text:'Update'
                            size_hint:0.7, 0.5
                            on_release:root.UpdateExamenResult()
                            background_color:'#DC143C'
                        Button:
                            text:'Delete'
                            size_hint:0.7, 0.5
                            on_release:root.DeleteExamenResult()
                            background_color:'#00FFFF'
                        Button:
                            text:'Show All'
                            size_hint:0.7, 0.5
                            on_release:root.ShowAllExamenResult()
                            background_color:'#6495ED'
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Label :
                            text:'Examens Schedule'
                        TextInput:
                            id:idExamSched
                            hint_text:'Id_ExamSched'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:1, 0.5
                        TextInput:
                            id:StreamN
                            hint_text:'Stream Number'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:1, 0.5
                        TextInput:
                            id:IdExamen1
                            hint_text:'Id Examen'
                            pos_hint:{'center_x':0.5,'center_y':0.5}
                            size_hint:1, 0.5
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Button:
                            size_hint:0.7, 0.5
                            text:'Fetch One'
                            on_release:root.FetchExamenSchedule()
                            background_color:'#FF7F50'
                        Button:
                            size_hint:0.7, 0.5
                            text:'Insert'
                            on_release:root.InsertExamenSchedule()
                            background_color:'#D2691E'
                        Button:
                            size_hint:0.7, 0.5
                            text:'Update'
                            on_release:root.UpdateExamenSchedule()
                            background_color:'#A52A2A'
                        Button:
                            size_hint:0.7, 0.5
                            text:'Delete'
                            on_release:root.DeleteExamenSchedule()
                            background_color:'#8A2BE2'
                        Button:
                            size_hint:0.7, 0.5
                            text:'Show All'
                            on_release:root.ShowAllExamenSchedule()
                            background_color:'#F5F5DC'
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"
                        Button:
                            size_hint:1.2, 0.5
                            text:'Join 1'
                            background_color:'#F5F5DC'
                            on_release: root.Join1()
                        Button:
                            size_hint:1.2, 0.5
                            text:'Join 2'
                            background_color:'#00FFFF'
                            on_release: root.Join2()
                        Button:
                            size_hint:1.2, 0.5
                            text:'Join 3'
                            background_color:'#FAEBD7'
                            on_release: root.Join3()
                    BoxLayout:
                        padding: "8dp"
                        spacing: "8dp"

                        Button:
                            size_hint:1.6, 0.5
                            text:'Print All '
                            background_color:'#7FFFD4'

            Screen:
                name: "s5"
                GridLayout:
                    padding: "8dp"
                    spacing: "8dp"
                    rows:7
                    size_hint:0.6, 0.7
                    pos_hint:{'center_x':0.5,'center_y':0.5 }
                    Button:
                        text: 'Enrolle Information'
                        pos_hint:{'center_x':0.5,'center_y':1 }
                        font_size:30
                        background_color:'#ff1493'
                        bold:True
                        on_release:root.enrolle_Information()
                    Button:
                        text: 'Selection Committee Employees'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        orientation: 'vertical'
                        on_release:root.employee_Information()
                    Button:
                        text: 'Examen Results'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        orientation: 'vertical'
                        on_release:root.Global_examen_Results()

                    Button:
                        text: 'Enrollement'
                        pos_hint:{'center_x':0.5,'center_y':0.5}
                        orientation: 'vertical'
                        on_release:root.employee_Information()



            Screen:
                name: "s6"
                BoxLayout
                    orientation: "vertical"
                    size_hint_y: None
                    spacing: "12dp"
                    height: "120dp"
                    TextInput:
                    Button :
                    Image:
                        id:image




















    MDNavigationDrawer:
        id:nav2
        anim_type: 'slide_above_simple'
        ContentNavigationDrawer:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"
            Image:
                id: avatar
                size_hint: (0.75,0.75)
                source: "./assets/signInLogo.png"
            MDLabel:
                text: "Selection Commitee "
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]
            MDLabel:
                text: "majda1bounif@gmail.com"
                size_hint_y: None
                font_style: "Caption"
                height: self.texture_size[1]
            ScrollView:
                DrawerList:
                    id:md_list
                    MDList:
                        OneLineIconListItem:
                            text:'Student'
                            on_release:
                                screen_manager.current='s1'
                                nav2.set_state()
                            IconLeftWidget:
                                icon:'face'
                        OneLineIconListItem:
                            on_release:
                                screen_manager.current='s2'
                                nav2.set_state()
                            text: "Schedule Examen"
                            IconLeftWidget:
                                icon: "calendar"
                        OneLineIconListItem:
                            text: "Faculties and Specialists "
                            on_release: screen_manager.current='s3'
                            IconLeftWidget:
                                icon: "school"
                        OneLineIconListItem:
                            text: "Studying plan"
                            on_release: screen_manager.current='s4'
                            IconLeftWidget:
                                icon: "folder"
                        OneLineIconListItem:
                            text: "All About"
                            on_release: screen_manager.current='s5'
                            IconLeftWidget:
                                icon: "file"
                        OneLineIconListItem:
                            text: "Where are we?"
                            IconLeftWidget:
                                icon: "map"
                                on_release: screen_manager.current='s6'
                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"

<Content@BoxLayout>
    name:'dialog'
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id: NameExamen
        hint_text: "Examen Name"
    MDTextField:
        id:score
        hint_text: "Score"

<Manager>:
    id: manager










































         '''




        )


from multiprocessing import Queue

MyMainApp().run()


