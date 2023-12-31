#Test funtions of interface
import sys
sys.path.append('../')  # Agrega la ruta del directorio principal
from readFiles import *
import selectColumns as s
import streamlit as st
from modelOperations import *
import showError as e
import prediction as p
import pickle
import plotModel as pm

from streamlit.testing.v1 import AppTest
at = AppTest.from_file("interface.py")
at.run()