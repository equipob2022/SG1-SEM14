import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pandas_datareader import data as pdr
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import plotly.express as px
import datetime

def app():
    st.title('Model 1 - SVR')
