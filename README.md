# Eng4_Sky_Pi

### This project takes the meaning of Pi(e) in the Sky a little too literal. For our DE Engineering 4 project, we decided to create a drone attachment to the Phantom 4, that can drop pies from the sky. The goal of this project was to drop a pie/whipped cream on our engineering teacher's head. The final outcome should look like this.

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Pie.png?raw=true" width="500">

# Pi in the Sky

## CAD
With Dylan Hensley

### Goal/Problem

- I had two big problems that I needed to face. I needed to design an attachment to a drone that wasn't designed to have anything attached to it. the whole drone is curved, with no edges to easily attach things to, the bottom of the drone is covered with sensors that can't be obstructed, and each component of the Phantom 4 has to stay attached. I had the idea of unscrewing the camera to make space to the attachment, however, I'd have to cut a few wires off a $1,000 dollar drone. NOT worth it.
- The second issue was weight. For a long while, I was more focussed on the complexity of the design than the function. The first dropper design contained way too many parts and would've been too heavy for the Phantom to carry.

### Solutions

- To solve the attachment problem, I had to do a lot of trial and error. In the Beginning, The first attachment I designed was made to go on the bottom of the drone, however, there are multiple sensors on the the bottom of the Phantom 4, and they can't be obstructed in any way. To solve this, I designed the new attachment that went on the sides of the drone. This way, the sensors can actually do their job.
- The reason weight was an issue at first. was becuase the first design of the dropper was an iris door. the iris door caused problems with weight and was to complex for the main goal of the project. We scrapped the idea and went with a lighter and less complex design, using a trap door instead.

### Pictures

<details><summary>The Pics</summary>

* first draft of attachment ↓

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(69).png?raw=true" width="200">

* first design of dropper ↓

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(66).png?raw=true" width="200">

* final atleration of dropper ↓

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(67).png?raw=true" width="200">

* final design of dropper ↓

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(71).png?raw=true" width="200">

* final design of cylinder ↓

<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(73).png?raw=true" width="200">


  </details>

### Links
 [- Iris Door](https://cvilleschools.onshape.com/documents/40cc3a7f2ae78f6941bb7a26/w/cac2b2e6847575ec62d46551/e/32d9a1864e7203af29d0071b)
 
 [- Final Design](https://cvilleschools.onshape.com/documents/f7c19773c7e7398ac151e850/w/93b63ee8ed95d510d0a8f784/e/a8d8ad2519b2f786b5c9a8e2)
 
 ### Final Assembly


## Code
With Conard Heins

<details><summary>The tale</summary>
 
the code for this project was criminally simple. basically, when the pi reaches a certain altitude, a servo fires, opening a hatch and dropping whipped cream onto whatever unfortunate teacher got stuck with the dubious duo. so simple any ape could code it, right? WRONG, NOT THIS APE! I feel I should preface my struggles with the fact that computers hate me. "But Conrad, computers don't have emotion or preference over individuals, they only do as they're told." I hear you smuggly reassuring yourself that computers couldn't possibly rise up and kill us all behind your computer screen. well i'm something of a special case, see, when I was born, the horrible witch aichtee'em'ell actually cursed me with a terrible curse. now whenever i use a pi, github, or any coding software, something will go horribly wrong, an entirely unique issue that apparently no one has ever experienced before. every. single. time. for example: in the early stages of the coding process, whenever I attempted to upload my progress to github, it would never push properly. after WEEKS of troubleshooting we found out my pi, despite telling us it was pinging google, and had full connection to the internet, did not in fact have connection to the internet. the little piece of s*** would lie to me every time I was pinging the internet, how is it even able to do that!?!? like it would be able to give me a fake packet from the internet that did not exist. but whatever, simple fix right? just get a new pi. WRONG!!!! ladies and gentlemen, I tried 5 different raspberry pi's, and 3 seperate sim cards, different breadboards, a different T cobbler, 3 different peoples chromebooks, someone else's github altogether, I even got my chromebook upgraded to the new ones only the seniors get. they all had the exact same issue. it didn't matter if we already knew they worked, we would use setups from my neighbors that have been working all year. my PI would lie to my face every damn time. all that mattered was that I was the one using it, and I simply wouldn't be able to access github. my only option was to manually upload all my code and pray that it was 1: saved properly and 2: wouldn't get fried in the process. This severely stunted my progress, as I would have to spend upwards of 20 minutes at the beginning and end of the class.
 

 </details>
 
### Goal/Problem
 
we decided to make the code as simple as possible by making the whipped cream drop once it reached a certain height.  if we added more advanced features we would also be adding weight. whether that be a camera, motion sensor, infared, no matter what these thing would make the code to complicated for my little chimp brain, but also compromise our payload.

### Solution

the solution is easy, copy harriet novaK.  or rather repurpose her code, her code used an altimeter that would measure when their PI reached the peak of its arc, and once it reached said peak it would fire a servo.  I took her code and removed all the weird math jazz and simplified the functionality.  once the altimeter reaches 15 meters from its launch point, it will fire a servo, dropping whatevers in the tube.

```python
 #taken from Harriet Novaks repository.
import time
import board
import adafruit_mpl3115a2 # barometer library
import pwmio
from adafruit_motor import servo
import busio
from gpiozero import Servo
import RPi.GPIO as GPIO
import pigpio


#servo = Servo(GPIO, min_pulse_width = minPW, max_pulse_width = maxPW)
my_servo=Servo(18)

i2c = board.I2C()
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)

sensor.sealevel_pressure = 102574
time.sleep(0.5)

my_servo.min()
alt = [] # array for altitude values
lv = sensor.altitude # initial value; zeroes it; 'launch value'

while True:
	altitude = sensor.altitude - lv
        # altitude is the diff between initial alt and current alt
	alt.append(altitude)
        # add latest data to alt array

	print(alt) # print array
	print(alt[0]) # print first altitude

	if altitude < 15: # if length of array is greater than 1
		print("servo fire")
		my_servo.max()
		time.sleep(5)
	else:
		my_servo.min()
		time.sleep(5)
 ```

## Reflection

<details><summary>Old Proposal</summary>
 
 
 # Proposal

For this years PI in the sky project me and dylan decided to make a thomas the tie fighter drone.  we think it would be a poetic end to our in class independent projects, as our first project together was thomas the dank tank.  we were inspired by this offhand photo we found. 

![alt text](https://github.com/cheins48/Eng4_Sky_Pi/blob/main/IThomas_the_TIE_fighter_drone_by_Null_Hypothesis_-_Thingiverse.jpg?raw=true)

## Problem
I do not have a thomas the tie fighter drone. This is a huge issue. Plus, Our first project (thomas the dank tank), was cut off at the last minute so we would like to let the Dank tank go out in a bang.

## Solution
make a thomas the tie fighter drone that shoots lasers and scares children.

## Some forseeable bumps in the road include:
1. the shape of tie fighters are really strange.  the walls and the shape of the cockpit will introduce a interesting challenge of space (get it, like space wars) managment.
2. weight,  goes hand in hand w/ the previous issue of shape.  but the walls will introduce a lot more weght to the build, the choice of material will be very important.  it will probably be styrofoam.
3. drone parts (see shopping list at bottom of page).  apparently we have a lot of these in the lab from an old Eng4 project but me and dylan havent seen any of them.
4. learning to program the drone parts.  the most annoying part of this is that there are countless drone coding tutorials ive found, but most are useless until I know what kind of harware I'm working with.
5. figuring out what out PI is gonna do.  the current plan is to make it turn laser pointers on and make a "pew" sound.

## Media/Design concepts
<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(29).png?raw=true" width="700">
<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/WIN_20220210_10_05_11_Pro.jpg?raw=true" width="700">

### Sudo Code For Laser
 ``` python
import pygame

# When turned on speaker plays downloaded audio

pygame.mixer.init()
pygame.mixer.music.load("myFile.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
    
# When button on controller is pressed, laser go pew pew.
# When button is pressed, signal reaches laser's power sourse and turns on

```


## Links
most of the information about drones that we are learning comes from this really exellent two part youtube series on drone theory by riley morgan (linked here: https://www.youtube.com/watch?v=K05UwsiqZ_E&list=PLwQuIH2CxvuNwSc9hrZjqlJOshi5iXb3l)
video on making budget racing drone, also where we got our parts list.  https://www.youtube.com/watch?v=GFNGUDT_9_c
website for making a laser pointer. https://makersportal.com/blog/2019/5/27/diy-cat-laser-pointer-toy

Supplies need for project
[Shopping list](https://docs.google.com/document/d/1tPvGNWoNBOXyaVN1nHXxPhS11FHQBHK2nczqA5JGK0U/edit?usp=sharing)

[Flight concept](https://www.youtube.com/watch?v=Lkd2jHDpMM0)

## Schedule

We will only plan two to three weeks at a time to maintain flexablity.

our first three weeks will be dedicated to getting the PI stuff outta the way. 
feb 21st to 26th getting the lazer code opperational
feb 28th to march 2nd getting the speaker working
march 4th to 9th *Might* be dedicated to getting a signal from a remote and controling it remotly with a controller depending on whether we have a micro reciever, and if we are able to get the other weeks done.

https://cvilleschools.onshape.com/documents/d02f9702869bb797ed84e06b/w/fb1974f453891c9a477c8c79/e/1e578d433cdf4da34e018e66

_________________________________________________________________________________________________________________________________________________________________________________

# Project Pivot

## Problems

- Due to some unpredicted issues, we have changed our project backed to the whipped cream launching drone. We already have the rough drafts and the cost of our project will be reduced. The drone would have an attachment that could drop whipped cream on people. (Mr.Miller)

## Rough draft


<img src="https://github.com/cheins48/Eng4_Sky_Pi/blob/main/Screenshot%20(34).png?raw=true" width="700">

[Rough draft](https://cvilleschools.onshape.com/documents/7b0aa35e39150dcdb07f0aa1/w/73e9bc6d49cae74f99640450/e/dae8bcf0fcdd82229f5a84aa)

## New Shopping list

[Shopping list](https://docs.google.com/document/d/1tPvGNWoNBOXyaVN1nHXxPhS11FHQBHK2nczqA5JGK0U/edit?usp=sharing)

## Risks

- We altered our project a little late in the game but we still think that this is the best decision.
- We might have some complications with weight while making the whipped cream launcher.
- whipped cream = mess

 
</details>
