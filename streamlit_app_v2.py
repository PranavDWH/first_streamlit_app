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
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response)  -- It will only show response(200). We will need to convert it to JSON
# streamlit.text(fruityvice_response.json())  # writes data in json format on screen

# below code will pick json version and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output will come on screen in table format
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

#######
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
# my_data_row = my_cur.fetchone() # fetchone function fetches only one value. Instead we will need to use fetchall()
my_data_rows = my_cur.fetchall() # fetchone function fetches only one value. Instead we will need to use fetchall()
streamlit.header("The Fruit Load list contains")
# streamlit.text(my_data_row) # It returns only one row - banana as text though there are 10 rows in table
# streamlit.dataframe(my_data_row) # dataframe shows result in table format instead of text, however, it will still show only one row
streamlit.dataframe(my_data_rows) # passing my_data_rows as variable to show multiple rows

# Take suggestion of what fruit customers want to add
streamlit.header("What fruit would you like to add?")
add_my_fruit = streamlit.text_input('jackfruit')
# streamlit.text(add_my_fruit)
my_data_rows = my_data_rows + add_my_fruit
streamlit.dataframe(my_data_rows)
