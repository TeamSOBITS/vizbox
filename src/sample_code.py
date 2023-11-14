#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

import rospkg

def pub_operator_text(msg):
    pub_OT = rospy.Publisher("/operator_text", String, queue_size=10)
    pub_OT.publish(msg)

def pub_robot_text(msg):
    pub_RT = rospy.Publisher("/robot_text", String, queue_size=10)
    pub_RT.publish(msg)

def pub_challenge_step(msg):
    pub_CS = rospy.Publisher("/challenge_step", UInt32, queue_size=10)
    pub_CS.publish(msg)

def pub_image():
    global img
    rospy.sleep(0.5)
    pub_Img = rospy.Publisher("/image", Image, queue_size=10)

    pub_Img.publish(img)

def callback(msg):
    global img
    cv2_img = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    img = CvBridge().cv2_to_imgmsg(img_rgb, "rgb8")

sub = rospy.Subscriber('/rgb/image_raw', Image, callback)

if __name__ == "__main__":
    rospy.init_node('pub_to_vizbox')
    try:
        rospy.sleep(1)
        while not rospy.is_shutdown():
            pub_image()
            pub_robot_text("we are SOBITS")
            pub_operator_text("Bring me apple")

    except rospy.ROSInterruptException:
        pass