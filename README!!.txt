Hello, Everyone this project is a Prototype, that detects an accident in the given source and sends an mail regards to the accident with image.

CHANGES THAT NEEDS TO BE DONE IN THE FILES, SO THIS PROJECT CAN BE USED BY YOU IN YOUR DEVICE.

!!!!CHANGES!!!!
1.Once you download the Yolov5 open Detect.py
1.1. In Detect.py chage the image address in line 225,226 for your device location.

2.In The Folder of Yolov5 open mail_send.py
2.1. In that mail_send.py file cahnge the sender and reciver email address to your clint and sender email's.
2.2. make sure you give the login for the gmail of the sender's address through Gooogle's 2 step varification login process that provides you with the ligin api code.  

3. In the GUI_W_Model_RADS file chnage the location of the trained model by giving the location of the model downloaded in your device in line 47(def accident()) by changing 
OneDrive/Documents/aiml/project/OG_data/new/yolov5/detect.py --weights OneDrive/Documents/aiml/project/OG_data/new/yolov5/runs/(etc) this into
(Give location of the model saved in your device)/yolov5/detect.py --weights (Give location of the model saved in your device)/yolov5/runs/(etc) .
 
4.Replace or change the CSV File in the GUI_W_Model_RADS File that acts as an Data base for login / Rigestration function.