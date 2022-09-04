# certificate-generator
In life, automating the boring stuff is the main key to be a productive person. This simple python prototype generates certificates based on the given name list automatically.

The problem that, this simple python script tries to solve is re-entering the name of the certificate holders.

This script uses Python & OpenCV as its main component to perform this task. The logic is pretty simple to understand, It takes a template of a certificate and generates more certificates based on the given name list.

Technology and Framework
Python 3.8
OpenCV
Why OpenCV?
We use OpenCV to write text on the certificate templates, OpenCV is a popular framework for computer vision.

How to use it?

Step 01: Enter the name list of certificate holders in the "name.txt" file.

![2022-09-04](https://user-images.githubusercontent.com/93598241/188305353-5963a141-15b1-42eb-be3f-522b60e61581.png)

Step 02: Choose a certificate template

![2022-09-04 (1)](https://user-images.githubusercontent.com/93598241/188305362-615dcb8b-7ab4-4d85-a9d2-320adae2bdf0.png)

Step 03: Get the X1, Y1 coordinates, to get the X1, Y1 coordinates, use windows print application that is free and easy. To do that, open the print and load the template in it. An example is shown bellow.

![image](https://user-images.githubusercontent.com/93598241/188305436-60b37f1e-d341-4663-b6ba-bd8751c5336e.png)

Note In the bottom of the paint application, it will show the X1, Y1 coordinates.

Step 04: Enter the X1, Y1 coordinates in "run.py" script, to do that open the "run.py" in a text editor and, edit the X1, Y1 coordinates that is found on the code line number of 22.

![image](https://user-images.githubusercontent.com/93598241/188305322-5fe01c9d-2427-46a4-9cd6-50901a1e8b32.png)

Step 05: Finally, execute the "run.py" script to get the outputs. In the "generated-certificates" folder all the generated certificates will be stored.

![2022-09-04 (2)](https://user-images.githubusercontent.com/93598241/188305450-a4e39bac-424e-4ca9-bff2-3210f71598aa.png)

# thank you
