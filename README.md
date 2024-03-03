## Senior Project | Thai Hand Written Recognition using CNN (ResNet50)
This is just one part of my Senior Project, the preprocessing phase."

## ACKNOWLEDGEMENTS
The research team extends heartfelt thanks to everyone who supported us. 
<br> We are grateful to Assoc. Prof. Dr. Chomthip Pornpanomchai for invaluable guidance and advice, 
<br> as well as to all teachers, senior colleagues, and parents for their unwavering support

## Objectives
The goal of Thai handwritten recognition is to create technology that accurately converts handwritten Thai script into digital text. This involves using deep learning techniques like Convolutional Neural Networks (CNNs) to improve accuracy. By leveraging machine learning methods and large datasets of handwritten Thai characters, we aim to develop systems capable of recognizing diverse writing styles. Ultimately, our research aims to make Thai handwritten recognition a valuable tool for various industries and individuals in the digital age.

## Members
Mr. Thanawath 		Huayhongthong		6388016 
<br> Resposible on GUI Displaying
<br><br>
Mr. Dhammawat		Siribunchawan		6388055
<br> Resposible on Trainning and Devleoping member process
<br><br>
Mr. Naphat			Sookjitsumrarn		6388059
<br> Resposible on Evaluating

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
<br>`Result`<br>
<img src="A4.png" alt="table" width="300">

## Paper Slicer
This Python script performs image processing operations such as replacing red pixels with white, enhancing brightness, and slicing an A4-sized image into smaller squares.
**Required library:** PIL (Python Imaging Library) 
<br> **Command:** pip install pillow

As you see that the template contain red lines, after we collect the calography image and put to the progeam.
<br> The script will eplaces red pixels in the input image with white pixels based on a distance threshold. It returns the modified image.
<br> Then slices an A4-sized image into smaller squares and applies image processing operations to each square. It saves the processed squares in the specified output folder.
**Don't forget to change the output after pulling this repository**
<br>`if __name__ == "__main__":`
   <br> `slice_a4_image("1.jpg", "C:\\Users\\Jigsaw\\Desktop\\Paperslicer\\เ-ะ", 88)`

## Size Check
Just check the size of the paper because shen you retrieve a scanning paper (with caligraphy), the resolutions and size may have changed

## Data Chosen 
When croping, the program will skip the last row and column because the image containing black space will not be selected. 
<br> The image that contain the black space is because the changed resolution of the caligraphy paper but the script originally size of the small image.
<br> Actually we can replace mentioned black space with better solution.
<br>
`Data chosen`<br>
<img src="/Snapshot/Data Chosen.png" alt="data chosen" width="300">
<br>
`Data with black space`<br>
<img src="/Snapshot/ExampleDataWithBlackSpace.png" alt="black">

