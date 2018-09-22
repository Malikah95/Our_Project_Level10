import kivy
from kivy import Config
from kivy.lang import Builder

kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


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

            cur.execute(
                "SELECT username,pass FROM user WHERE username='" + username_text + "' AND pass ='" + password_text + "'")
            count = cur.fetchone()

            if count is None:

                # Label
                print("Enter a valid username and password")

            else:
                print("correct")
                # will allow to access next page

    class Loginapp(App):
        def build(self):
            self.load_kv('log.kv')
            return Login()

class Register(Screen):
    def register_pressed(self):
        username_text = self.username_input.text
        email_text = self.email_input.text
        password_text = self.password_input.text

        cur.execute("SELECT * FROM user WHERE username='" + username_text + "'")
        count = cur.fetchone()

        if count is not None:
            print("Username is exists,please change...")

        elif not username_text or not email_text or not password_text:

            # need LABEL
            print("must fill all blank.")



        else:
            cur.execute(
                "INSERT INTO user (username, email, pass) VALUES('" + username_text + "' , '" + email_text + "', '" + password_text + "')"
            )

            mydb.commit()
            cur.close()
            mydb.close()


class RegesApp(App):
    def build(self):
        self.load_kv('reges.kv')
        return Regesration()


RegesApp().run()


class Personal_Info(Screen):

        def personal_Info(self):
            age_input = self.age_input
            Gender_input = self.Gender_input
            BloodPresure_input = self.BloodPresure_input
            Length_input = self.Length_input
            weight_input = self.weight_input

            cur.execute("SELECT age_input,Gender_input,BloodPresure_input,weight_input,Length_input  FROM user")

            count = cur.fetchone()

            if count is None:
                cur.execute(
                    "INSERT INTO user (Age,Gender,BloodPresure,Weight,Length )VALUES('" + age_input + "', '" + Gender_input + "', '" + BloodPresure_input + "',"
                                                             " '" + weight_input + "', '" + Length_input + "')")
                mydb.commit()
                cur.close()
                mydb.close()


class personal_InfoApp(App):
    def build(self):
        self.load_kv('reges.kv')
        return personal_Inf


class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreensApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    ScreensApp().run()