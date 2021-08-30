#!/usr/bin/env python

#This is a PID controller to determine twist values

import rospy
from state_definitions import *
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16, Float32

#Linear speed of the robot
LINEAR_SPEED = 0.3
#Angular speed of the robot
ANGULAR_SPEED = 3.1415926/6

#Multipliers used to tune the PID controller
#Proportional constant
P_CONSTANT = .5
#Integral constant
I_CONSTANT = 0
#Derivative constant
D_CONSTANT = .1


target_line = 1 #meters

#CALLBACKS FOR ANYTHING YOUR PID NEEDS TO SUBSCRIBE TO FROM scan_values_handler

def scan_values_handler_cb (msg):
    global dist
    dist = msg.data


#Init node
rospy.init_node('pid')

#Create publisher for suggested twist objects
pub = rospy.Publisher('pid_twist', Twist, queue_size = 1)

#SUBSCRIBERS FOR THINGS FROM scan_values_handler YOU MIGHT WANT
sub = rospy.Subscriber('/dist', Float32, scan_values_handler_cb)

#Twist and rate object
t = Twist()
rate = rospy.Rate(10)

dist = target_line
previous = 0
p_component = 0

while not rospy.is_shutdown():
    previous = p_component
    #calculate p component
    p_component = dist - target_line
    #calculate d component
    d_component = p_component - previous
    #calculate i component
    i_component = 0
    #Add them all together, multiplied by their respective tuning values, and multiply everything
    #by the angular velocity
    t.angular.z = ANGULAR_SPEED * (P_CONSTANT * p_component + D_CONSTANT * d_component + I_CONSTANT * i_component)
    t.linear.x = LINEAR_SPEED
    #Publish the twist to the driver
    pub.publish(t)
    rate.sleep() 