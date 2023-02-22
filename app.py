from socket import timeout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty

from PIL import ImageGrab, Image
import models
import tools
import tensorflow as tf
import gc
import numpy
from pluginFactory import PluginFactory
import os
import time
 
Window.size = (350,550)

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Front/Poppins-Regular.ttf"
    font_size = 30


class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Front/Poppins-Regular.ttf"
    font_size = 30

class LinaApp(MDApp):

    def build(self):
        # Create the screen manager
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file('Front/Main.kv'))
        sm.add_widget(Builder.load_file('Front/Chats.kv'))
        return sm

    def response(self, value):
        global size, halign
        response = self.interface(value)
        if len(response) < 6:
            size = .22
        elif len(response) < 11:
            size = .32
        elif len(response) < 16:
            size = .45
        elif len(response) < 21:
            size = .58
        elif len(value) < 26:
            size = .71
        else:
            size = .77
        sm.get_screen('chats').chat_list.add_widget(Response(text=response, size_hint_x=size))

    def send(self):
        global size, halign, value
        if sm.get_screen('chats').text_input != "":
            value = sm.get_screen('chats').text_input.text
            print(value)
            if len(value) < 6:
                size = .22
                halign = "center"
            elif len(value) < 11:
                size = .32
                halign = "center"
            elif len(value) < 16:
                size = .45
                halign = "center"
            elif len(value) < 21:
                size = .58
                halign = "center"
            elif len(value) < 26:
                size = .71
                halign = "center"
            else:
                size = .77
                halign = "left"
            sm.get_screen('chats').chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            self.response(value)
            #if "youtube" in value:
            #    cmd = 'python3 Youtube_API.py'
            #    os.system(cmd)
            sm.get_screen('chats').text_input.text = ""
         
    
    def analyse(self,sentence):
         subjects, types, stopwords, dictionnary = tools.defaultValues()
         modelSubjects= models.getModelSubjects(dictionnary, subjects)
         modelSubjects.load("data/modelSubjects.tflearn")
         resultS= modelSubjects.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
         tf.keras.backend.clear_session()
         del modelSubjects
         gc.collect()
    
         modelTypes= models.getModelTypes(dictionnary, types)
         modelTypes.load("data/modelTypes.tflearn")
         resultT= modelTypes.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
         tf.keras.backend.clear_session()
         del modelTypes
         gc.collect()
    
         modelValues= models.getModelValues(dictionnary)
         modelValues.load("data/modelValues.tflearn")
         resultV= modelValues.predict([tools.bagOfWords(sentence, dictionnary, stopwords)])
         tf.keras.backend.clear_session()
         del modelValues
         gc.collect()
         return resultS[0], resultT[0], resultV[0][0]
         # rSubject, rType, rValue = self.build(self.user.text)
         # self.result = self.searchAnswer(self.user.text, subjects[numpy.argmax(rSubject)], types[numpy.argmax(rType)])
         # return self.result
     
         
     
    def searchAnswer(self, sentence, subject, typeS):
          plugin = PluginFactory.getPlugin(subject, typeS)
          return plugin.response(sentence)
      
    def interface(self, value):
        subjects, types, stopwords, dictionnary = tools.defaultValues()
        #while True:
            #print("Tape your sentence:")
            #test= input()
        print("je pass la 00")
        print("---->",value)
        rSubject, rType, rValue = self.analyse(value)
        self.result = self.searchAnswer(value, subjects[numpy.argmax(rSubject)], types[numpy.argmax(rType)])
        print("---->", self.result)
        #print(result)
        return self.result
      
    
    
if __name__ == '__main__':
    LinaApp().run()
     
    
              
        
             
        
   
                     
    
        
    
    

    
     
      
         

 