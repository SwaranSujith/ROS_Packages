#!/usr/bin/env python
   
from __future__ import print_function
   
import sys
import rospy
from dist_conv_server.srv import MotorStatus, MotorStatusResponse
   
def Motor_check_client():
    rospy.init_node('Motor_client')

    # rospy.wait_for_service('motor1_check')
    # rospy.wait_for_service('motor2_check')
    # rospy.wait_for_service('motor3_check')

    print("Motor check in progress ...")  

    try:  
        dist1 = rospy.ServiceProxy('motor1_check',MotorStatus)
        resp1 = dist1()
        rospy.loginfo(resp1.message) 
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e) 
        sys.exit(1)

    try:    
        dist2 = rospy.ServiceProxy('motor2_check',MotorStatus)
        resp2 = dist2()
        rospy.loginfo(resp2.message) 
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e) 
        sys.exit(1)

    try:       
        dist3 = rospy.ServiceProxy('motor3_check',MotorStatus)
        resp3 = dist3()
        rospy.loginfo(resp3.message)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s"%e) 
        sys.exit(1) 

    if ((resp1.result == 1)*(resp2.result == 1)*(resp3.result == 1)):
        rospy.loginfo("Joint Motor Check  : PASS")  

    else:
        rospy.loginfo("Joint Motor Check : FAIL")                                              
          
   

if __name__ == "__main__":
    print("Diagnostic code running")
    Motor_check_client()
