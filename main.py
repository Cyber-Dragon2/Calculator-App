from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from math import sqrt


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.equation = ""
        self.brac = 0 # 0 for '(' and 1 for ')'
        self.layout = BoxLayout()
        self.layout.orientation = "vertical"

        self.textarea = TextInput(font_size = "45sp",disabled = True,size_hint = (1,0.5),background_color = (255,255,255,1))
        #self.textarea.foreground_color = (0,0,0,1)
        # self.textarea.hint_text = "Enter number"
        self.GridInside = GridLayout()
        # self.GridInside.spacing = 20
        self.GridInside.rows = 5
        self.GridInside.cols = 4
        
        self.btn_ac = Button(text = "AC",on_press = lambda x :self.clear("ac"))
        self.btn_del = Button(text = "del",on_press = lambda x :self.clear("del"))
        self.btn_root = Button(text = "√",on_press = self.solve_root)
        self.btn_divide = Button(text = "/",on_press = lambda x:self.action("/"))
        self.btn1 = Button(text = "1",on_press = lambda x:self.action("1"))
        self.btn2 = Button(text = "2",on_press = lambda x:self.action("2"))
        self.btn3 = Button(text = "3",on_press = lambda x:self.action("3"))
        self.btn_mul = Button(text = "x",on_press = lambda x:self.action("*"))
        self.btn4 = Button(text = "4",on_press = lambda x:self.action("4"))
        self.btn5 = Button(text = "5",on_press = lambda x:self.action("5"))
        self.btn6 = Button(text = "6",on_press = lambda x:self.action("6"))
        self.btn_min = Button(text = "-",on_press = lambda x:self.action("-"))
        self.btn7 = Button(text = "7",on_press = lambda x:self.action("7"))
        self.btn8 = Button(text = "8",on_press = lambda x:self.action("8"))
        self.btn9 = Button(text = "9",on_press = lambda x:self.action("9"))
        self.btn_plus = Button(text = "+",on_press = lambda x:self.action("+"))
        self.btn_percent = Button(text = "()",on_press = self.addbrac)
        self.btn0 = Button(text = "0",on_press = lambda x:self.action("0"))
        self.btn_dot = Button(text = ".",on_press = lambda x:self.action("."))
        self.btn_calc = Button(text = "=",on_press = self.calculate)
        
        self.btn_list=[self.btn_ac,self.btn_del,self.btn_root,self.btn_divide,self.btn1,self.btn2,self.btn3,self.btn_mul,self.btn4,self.btn5,self.btn6,self.btn_min,self.btn7,self.btn8,self.btn9,self.btn_plus,self.btn_percent,self.btn0,self.btn_dot,self.btn_calc]
        for i, self.btn in enumerate(self.btn_list):
            if i <= 1:
                self.btn.font_size = "40sp"    
                # self.btn.background_color = (255,255,255,1)
                # self.btn.color = "black"
               
            else:
                # self.btn.background_color = "black"
                self.btn.font_size = "50sp"
            self.GridInside.add_widget(self.btn)

        self.layout.add_widget(self.textarea)
        self.layout.add_widget(self.GridInside)



    def action(self,num):
        self.equation += num 
        self.textarea.text = self.equation

    def clear(self,command):
        if command == "ac":
            self.textarea.text = ""
            self.equation = ""
        if command == "del":
            self.equation = self.equation[:-1]
            self.textarea.text = self.equation


    def calculate(self,instance):
        try:
            print(self.equation)
            self.equation = str(eval(self.equation))
            print(self.equation)
            self.textarea.text = self.equation
        except Exception as e:
            self.textarea.text = "Error"
            print(e)
            self.equation = ""
    
    def solve_root(self,instance):
        try:
            self.equation = str(sqrt(int(float(self.equation))))
            self.textarea.text = self.equation
        except:
            self.textarea.text = "Error"

    def addbrac(self,instance):
        if self.brac == 0:
            if len(self.equation)!=0:
                if self.equation[-1] == "*": 
                    self.equation+="("
                else:
                    self.equation+="*("
            else:
                self.equation+="("
            self.textarea.text = self.equation
            self.brac = 1
        else:
            self.equation+=")"
            self.textarea.text = self.equation
            self.brac = 0
    def build(self):
        return self.layout


app = CalculatorApp()
app.run()

