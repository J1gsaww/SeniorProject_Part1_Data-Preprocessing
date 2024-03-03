## Senior Project | Thai Hand Written Recognition using CNN (ResNet50)
This is just one part of my Senior Project, the preprocessing phase."

## ACKNOWLEDGEMENTS
The research team extends heartfelt thanks to everyone who supported us. 
<br> We are grateful to Assoc. Prof. Dr. Chomthip Pornpanomchai for invaluable guidance and advice, 
<br> as well as to all teachers, senior colleagues, and parents for their unwavering support

## Objectives
The goal of Thai handwritten recognition is to create technology that accurately converts handwritten Thai script into digital text. This involves using deep learning techniques like Convolutional Neural Networks (CNNs) to improve accuracy. By leveraging machine learning methods and large datasets of handwritten Thai characters, we aim to develop systems capable of recognizing diverse writing styles. Ultimately, our research aims to make Thai handwritten recognition a valuable tool for various industries and individuals in the digital age.

## System Structure Chart
<img src="System Structure Chart.png" alt="SystemArc">


## Preprocessing 
The Thai alphabet comprises 44 consonants, 21 vowels, 4 intonation marks, and 79 writing forms in total. The project needs convenient methods to retrieve the data by implementing an easier screen capture of the paper. One of the methods is creating a writing table template by implementing the Pillow library in Python.
<br><br>
The code provided among this repository are 
- Table Generator
- Paper Slicer
- Size Check

## Table Generator
**Required library:** PIL (Python Imaging Library) 
<br> **Command:** pip install pillow
<br> The script will generate an image file named `A4.png` containing a table drawn on an A4-sized canvas.
<br> The script defines a function `generate_table_on_a4()` that creates a table with red grid lines on an A4-sized canvas. The table cells have a default size of 44x44 pixels.
`Result`<br>
<img src="A4.png" alt="table" width="400">

