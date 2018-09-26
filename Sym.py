import kivy
from kivy import Config
from kivy.lang import Builder
from kivy.uix.popup import Popup
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import mysql.connector
import mysql
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from mysql.connector import MySQLConnection
from kivy.uix.screenmanager import Screen

mydb =mysql.connector.Connect(

    host="localhost",
    user="root",
    password="root1234567",
    database="user_inf"
 )
cur = mydb.cursor()

Config.set('graphics', 'width',  350)
Config.set('graphics', 'height', 600)

Builder.load_file("symkivy.kv")

class Manager(ScreenManager):
    pass

class LoginWindow(Screen):


        def Login_pressed(self):
            username_text = self.username_input.text
            password_text = self.password_input.text
            popup1 = Popup(content=Label(text='Enter a valid username and password'),
                           auto_dismiss=True, size_hint=(None, None), size=(400, 400))


            cur.execute(
                "SELECT username,pass FROM user WHERE username='" + username_text + "' AND pass ='" + password_text + "'")
            count = cur.fetchone()

            if count is None:
                popup1.open()


            else:
                #diagnosis interface, delete print
                print("correct")



class Loginapp(App):
        def build(self):
            self.load_kv('symkivy.kv')
            return Loginapp()

class Register(Screen):
    def register_pressed(self):
        username_text = self.username_input.text
        email_text = self.email_input.text
        password_text = self.password_input.text
        popup1 = Popup(content=Label(text='Username is exists,please change'),
                       auto_dismiss=True, size_hint=(None, None), size=(400, 400))

        popup2 = Popup(content=Label(text='Fill all blank'),
                       auto_dismiss=True, size_hint=(None, None), size=(400, 400))

        cur.execute("SELECT * FROM user WHERE username='" + username_text + "'")
        count = cur.fetchone()

        if count is not None:
            popup1.open()


        elif not username_text or not email_text or not password_text:
            popup2.open()





        else:
            cur.execute(
                "INSERT INTO user (username, email, pass) VALUES('" + username_text + "' , '" + email_text + "', '" + password_text + "')"
            )

            mydb.commit()
            cur.close()
            mydb.close()


class RegesApp(App):
    def build(self):
        self.load_kv('symkivy.kv')
        return RegesApp()


#RegesApp().run()


class Personal_Info(Screen):

        def personal_Info(self):
            age_input = self.age_input
            gender_input = self.gender_input
            bloodpresure_input = self.bloodpresure_input
            length_input = self.length_input
            weight_input = self.weight_input

            cur.execute("SELECT age_input,Gender_input,BloodPresure_input,weight_input,Length_input  FROM user")

            count = cur.fetchone()

            if count is None:
                cur.execute(
                    "INSERT INTO user (Age,Gender,BloodPresure,Weight,Length )VALUES('" + age_input + "', '" + gender_input + "', '" + bloodpresure_input + "',"
                                                             " '" + weight_input + "', '" + length_input + "')")
                mydb.commit()
                cur.close()
                mydb.close()


class personal_InfoApp(App):
    def build(self):
        self.load_kv('symkivy.kv')
        return personal_InfoApp


class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreensApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    ScreensApp().run()
