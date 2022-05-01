**EYEASSSISTANT**

![image](https://drive.google.com/file/d/16_c2__HWSrrJs4_R3VSNxqSb7R_FWY-R/view?usp=sharing)
WHAT IT DOES?
The program collects the data from the mobile phone of the person that is taking a video in real life. From there it obtain frames and the API can detect in those frames some characteristics as the room type or the objects that are in there. Using the Alexa app, the person can ask to know in which room is it, which is the condition of the room or which objects are there and receive and answer.

HOW WAS BUILT?
At first, we learn about how to use the restb.ai API, and with that, we extracted some data about different pictures. With this data extracted from de Artificial vision API and also a pre-trained Deep Learning model called YOLOV4 Darknet, we got the data about which room is currently filming, how good is this room and also different objects around the room. The data extracted from this topics, were converted into a .json file that was sended to Alexa throw a public host. Using Alexa developer console, we created a Skill in which we invocate intents with utterances. This let us implement the answers that Alexa can give to the questions of the users. We got the data bridge from our Python script to Alexa throw ngrok libraries.



Project done for the sponsor Restb.ai by 
Cristina Ortega, Carlos Martín León and Arnau Ranchal.
