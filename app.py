import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('sepsa07.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13):

	prediction = classifier.predict(
		[[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13]])
	print(prediction)
	return prediction
	

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Predicting Neonatal Sepsis")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Predicting Neonatal Sepsis </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	text1 = st.text_input("Gender", "(0=male; 1=female)")
	text2 = st.text_input("Type of Childbirth Delivery", "(0=vaginal)")
	text3 = st.text_input("5-Minute Apgar Score", "[1=(1-6); 0=(7-10)]")
	text4 = st.text_input("Gestational Age", "Type Here")
	text5 = st.text_input("Birth Weight", "Type Here")
	text6 = st.text_input("Age of Onset", "Type Here")
	text7 = st.text_input("Leukocyte Count", "(for decimal use dot)")
	text8 = st.text_input("Immature Neutrophile Percentage", "Type Here")
	text9 = st.text_input("Lymphocyte Percentage", "Type Here")
	text10 = st.text_input("Presence of Toxic Granulations", "(0-absent; 1-present)")
	text11 = st.text_input("Thrombocyte Count", "Type Here")
	text12 = st.text_input("Serum CRP Concentration", "(for decimal use dot)")
	text13 = st.text_input("Serum PCT Concentration", "(for decimal use dot)")
	result =""
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		result = prediction(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13)
	st.success('Probability of sepsis {}'.format(result))
	
if __name__=='__main__':
	main()
