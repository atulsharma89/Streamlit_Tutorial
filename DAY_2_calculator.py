import streamlit as st

st.title('Calculator')
# #st.write('Enter first number:')
# #first_value = st.number_input('Enter number:')
# #st.write('Enter second number:')
# #second_value = st.number_input('Enter second number:')
# #st.write('Addition of two numbers:')
# #st.write(first_value + second_value)
# #st.write('Subtraction of two numbers:')
# #st.write(first_value - second_value)
# #st.write('Multiplication of two numbers:')
# #st.write(first_value * second_value)
# #st.write('Division of two numbers:')
# #st.write(first_value / second_value)
# #st.write('Modulus of two numbers:')
# #st.write(first_value % second_value)
# #st.write('Exponent of two numbers:')
# #st.write(first_value ** second_value)
# #st.write('Floor division of two numbers:')
# #st.write(first_value // second_value)
#st.header('Revised code')


with st.form('my_form'):
  first_value = st.number_input('Enter number:')
  second_value = st.number_input('Enter second number:')

  addition = st.form_submit_button('Submit_add')
  if addition:
      add_value = first_value + second_value
      st.write(add_value)

  subtraction = st.form_submit_button('Submit_sub')
  if subtraction:
      sub_value = first_value - second_value
      st.write(sub_value)
  multiplication = st.form_submit_button('Submit_mul')
  if multiplication:
      mul_value = first_value * second_value
      st.write(mul_value)
  division = st.form_submit_button('Submit_div')
  if division:
      div_value = first_value / second_value
      st.write(div_value)
  modulus = st.form_submit_button('Submit_mod')
  if modulus:
      mod_value = first_value % second_value
      st.write(mod_value)
  exponent = st.form_submit_button('Submit_exp')
  if exponent:
      exp_value = first_value ** second_value
      st.write(exp_value)
  floor_division = st.form_submit_button('Submit_flr')
  if floor_division:
      flr_value = first_value // second_value
      st.write(flr_value)

#if submitted:
#  st.write(add_value)