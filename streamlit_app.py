import streamlit

streamlit.title('My Parents New Heathly Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥣 Idli Sambhar')
  
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df = streamlit.dataframe(my_fruit_list)
streamlit.dataframe(my_fruit_list.Fruit)


my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Capture list of selected fruits in a variable
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]  
# loc - Access a group of rows and columns by label(s) or a boolean array.


# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New Section to display fruit API response
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response)  -- It will only show response(200). We will need to convert it to JSON
streamlit.text(fruityvice_response.json())  
