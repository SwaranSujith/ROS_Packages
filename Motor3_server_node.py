#!/usr/bin/env python

from __future__ import print_function
from dist_conv_server.srv import MotorStatus, MotorStatusResponse
import random
import rospy
   
def check_motor3_status(req):
   req.status = random.randint(0,1)
   if(req.status==1):
      return MotorStatusResponse(req.status,"Motor 3 OK")
   else:
      return MotorStatusResponse(req.status,"Motor 3  NOT OK")

   
def Motor_check_server():
   rospy.init_node('Motor3_server')
   s = rospy.Service('motor3_check', MotorStatus, check_motor3_status)
   print("Motor 3 checking service started ")
   rospy.spin()
   
if __name__ == "__main__":
   Motor_check_server()