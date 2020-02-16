import unittest
import requests
import xml.etree.ElementTree as ET

class MVC():
    swUrl ="https://swapi.co/api/people/"

    def __init__(self,NumeroPersonaje):
        self.numPersonaje = str(NumeroPersonaje)
    
    def modelo(self):
        infoPersonaje = requests.get(self.swUrl+self.numPersonaje).json()
        return infoPersonaje["name"]


    

class MVC_Prueba(unittest.TestCase):
    def test_is_a_Class(self):
        self.assertIsInstance(type(MVC),type(MVC_Prueba))
    def test_model(self):
        luke  = MVC(1)
        C_3P0 = MVC(2)
        self.assertEqual(luke.modelo(),"Luke Skywalker")
        self.assertEqual(C_3P0.modelo(),"C-3PO")
    def test_controlador(self):
        luke  = MVC(1)
        C_3P0 = MVC(2)
        lukeXML   = luke.controlador().getroot()
        C_3P0_XML = C_3P0.controlador().getroot()
        self.assertEqual(lukeXML[0].text  ,"Luke Skywalker")
        self.assertEqual(C_3P0_XML[0].text,"C-3PO")
    def test_vista(self):
        pass

unittest.main()