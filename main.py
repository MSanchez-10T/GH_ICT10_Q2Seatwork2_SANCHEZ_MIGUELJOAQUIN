# Creating a general weighted average calculator using tuples
from pyscript import display, document #type:ignore

#  Calculating GWA
def student_information(e):
    document.getElementById('output1').innerHTML=""
    Last_Name= document.getElementById('Last_Name').value
    First_Name= document.getElementById('First_Name').value
    gr1= int(document.getElementById('English').value)
    gr2= int(document.getElementById('Science').value)
    gr3= int(document.getElementById('ICT').value)
    gr4= int(document.getElementById('Math').value)
    gr5= int(document.getElementById('Filipino').value)
    gr6= int(document.getElementById('PE').value)
    grades= (gr1, gr2, gr3, gr4, gr5, gr6)
    units = (5, 2, 3, 1)
    grade1 = {(grades [0] * units[0])}
    grade2 = {(grades [1] * units[0])}
    grade3 = {(grades [2] * units[1])}
    grade4 = {(grades [3] * units[0])}
    grade5 = {(grades [4] * units[2])}
    grade6 = {(grades [5] * units[3])}
    total_sum= grade1 + grade2 + grade3 + grade4 + grade5 +grade6
    total_value= (units [0] * 3) + (units [1] * 1) + (units [2] * 1) + (units [3] * 1)
    gwa = total_sum / total_value


#  Displaying Student Information
    display(f'{Last_Name} {First_Name}', target='output1')
    display(f'Your GWA is {gwa}', target='output1')
  



