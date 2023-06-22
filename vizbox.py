#!/usr/bin/env python3
#coding:utf-8

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

import rospkg

img_pub_flag = "az"

def pub_operator_text(msg):
    pub_OT = rospy.Publisher("/operator_text", String, queue_size=10)
    pub_OT.publish(msg)

def pub_robot_text(msg):
    pub_RT = rospy.Publisher("/robot_text", String, queue_size=10)
    pub_RT.publish(msg)

    # rate = rospy.Rate(1) # 1hz
    # while not rospy.is_shutdown():
    #     pub_RT.publish(msg)
    #     rate.sleep()

def pub_challenge_step(msg):
    pub_CS = rospy.Publisher("/challenge_step", UInt32, queue_size=10)
    pub_CS.publish(msg)

def change_img_pub_flag(msg):
    global img_pub_flag
    img_pub_flag = msg

def pub_image():
    global img_pub_flag, az_img, yolo_img
    rospy.sleep(0.5)
    pub_Img = rospy.Publisher("/image", Image, queue_size=10)

    # img = cv2.imread("example.png", cv2.IMREAD_COLOR)
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # ex_img = CvBridge().cv2_to_imgmsg(img_rgb, "rgb8")
    # pub_Img.publish(ex_img)

    pub_Img.publish(az_img)

def az_callback(msg):
    global az_img
    cv2_az_img = CvBridge().imgmsg_to_cv2(msg, "bgr8")
    img_rgb = cv2.cvtColor(cv2_az_img, cv2.COLOR_BGR2RGB)
    az_img = CvBridge().cv2_to_imgmsg(img_rgb, "rgb8")
    # az_img = cv2_az_img

az_sub = rospy.Subscriber('/rgb/image_raw', Image, az_callback)

def yolo_callback(msg):
    global yolo_img
    yolo_img = CvBridge().imgmsg_to_cv2(msg, "bgr8")

yolo_sub = rospy.Subscriber('/yolov5/image_out', Image, yolo_callback)


if __name__ == "__main__":
    rospy.init_node('pub_to_vizbox')
    rate = rospy.Rate(1)
    try:
        while not rospy.is_shutdown():
            pub_image()
            rate.sleep()
            pub_robot_text("we are SOBITS")
            rate.sleep()
            pub_operator_text("Bring me apple")
            rate.sleep()

    except rospy.ROSInterruptException:
        pass