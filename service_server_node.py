#!/usr/bin/env python
from __future__ import print_function
from dist_conv_server.srv import cmmm_converter, cmmm_converterResponse
import rospy

def handle_dist_req(req):
      print("Returning [%s mm = %s cm]"%(req.a ,(req.a *10)))
      return cmmm_converterResponse(req.a *10)

def serv_function():
       rospy.init_node('distance_converter')
       s = rospy.Service('dist_conv', cmmm_converter, handle_dist_req)
       print("Ready to convert")
       rospy.spin()
if __name__ == "__main__":
       serv_function()