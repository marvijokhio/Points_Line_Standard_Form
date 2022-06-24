# Points_Line_Standard_Form_Exercise
Program to find the equation of a line in the standard form Ax +By = C. 
This program takes user input in form of two co-ordinate pairs. The code is 
PEP-8 compliant and written using pylint linting tool.

This program takes two points (co-ordinate pairs) as input and outputs the linear euation of a line 
crossing these two co-rdinates in the standard form i,e. Ax + By = C. 
For example, co-ordinates (1,3) and (2,4) have line equation −1x+1y=2. 
You can use this [This is an external link to genome.gov](https://www.mathwarehouse.com/calculators/equation-line-from-2-points.php) webpage to check your answers. This web page takes two points and show line equation in all the forms but just check the standard form. Note: there could be difference in some answers as our code doesn't 
reduces or simplifies the equation by taking commons facotrs. 

Limitations: 
1. The program does not reduce or simplify the final euation by taking highest common factors. 
2. There is no proper handline for minimum or maximum values fo x and y- axis of co-ordinate pairs in this initial version. It's highly 
recommended to use values under 10 for x and y.



## How to run the program
You can run the program in two ways. 
1. Run it to just test using given test file named 'test_findline_equation.py' or 
2. You can directly run the main file named 'findline_equation.py'


### Method 1
Download the repository and run the python file named 'test_findline_equation.py'  

### Method 2
1. Download the repository  <br>
2. Open the file names 'test_findline_equation.py' <br>
3. add the following line at the very end of the file and hit enter and save. 
```
find_line_from_two_coordinates(input_coordinates())
```
Now run this python file named 'test_findline_equation.py'

