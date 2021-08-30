#!/usr/bin/env python

#This processes all of the scan values


import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int16, Float32
from state_definitions import *

#Process all the data from the LIDAR
def cb(msg):
    #Determine state
    pub_state.publish(FOLLOWING)
    #CALCULATE AND PUBLISH ANYTHING ELSE FOR THE PID

    prop_dist = msg.range_max
    for i in range(len(msg.ranges)):
        if msg.ranges[i] < prop_dist and msg.ranges[i] < msg.range_max and msg.ranges[i] > msg.range_min:
            prop_dist = msg.ranges[i]
    pub_dist.publish(prop_dist)





#Init node
rospy.init_node('scan_values_handler')

#Subscriber for LIDAR
sub = rospy.Subscriber('scan', LaserScan, cb)

#Publishers
pub_state = rospy.Publisher('state', Int16, queue_size = 1)
#THINK OF WHAT INFO TO PUBLISH TO THE PID
pub_dist = rospy.Publisher('dist', Float32, queue_size = 1)

#Rate object
rate = rospy.Rate(10)

#Keep the node running
while not rospy.is_shutdown():
    rate.sleep() 