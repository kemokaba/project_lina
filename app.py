from kivymd.app import App
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
import re 

from PIL import ImageGrab, Image
import models
import tools
import tensorflow as tf
import gc
import numpy
from pluginFactory import PluginFactory
 
Window.size = (350,550)

class ChatBot(App):
    
    def build(self):
            self.window = GridLayout()
            self.window.cols = 1
            self.window.size_hint = (0.6, 0.7)
            self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
            # add widgets to window
            
            # image widget
            #self.window.add_widget(Image(source)="logo.png")
            
            # label widget
            self.greeting = Label(
                            text=str("Tape your sentence"),
                            font_size = 18,
                            color="#00FFCE"
                            )
            self.window.add_widget(self.greeting)
            
            # text input widget
            
            self.user =  TextInput(
                         multiline=False,
                         padding_y = (20,20),
                         size_hint = (1, 0.5)
                         )
            self.window.add_widget(self.user)
            
            # button widget 
            self.button =  Button(
                           text="SEND",
                           size_hint = (1, 0.5),
                           bold = True,
                           background_color = "#00FFCE",
                           background_normal = ""
                           )
            
            self.button.bind(on_press=self.callback)
            #self.button.bind(on_press=self.analyse)
            
            self.window.add_widget(self.button)
            return self.window
            
            # fonction callback
    def  callback(self, instance):
        #self.greeting.text = "Hello " + self.user.text + " !"
        #rSubject, rType, rValue = self.analyse(re)
        self.greeting.text = self.interface()
        #print(self.result)
        
         
    
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
      
    def interface(self):
        subjects, types, stopwords, dictionnary = tools.defaultValues()
        #while True:
            #print("Tape your sentence:")
            #test= input()
        print("je pass la 00")
        print("---->",self.user.text)
        rSubject, rType, rValue = self.analyse(self.user.text)
        self.result = self.searchAnswer(self.user.text, subjects[numpy.argmax(rSubject)], types[numpy.argmax(rType)])
        print("---->", self.result)
        #print(result)
        return self.result
      
    
    
if __name__ == '__main__':
    ChatBot().run()
     
    
              
        
             
        
   
                     
    
        
    
    

    
     
      
         

 