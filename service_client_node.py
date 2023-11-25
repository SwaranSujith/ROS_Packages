#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from dist_conv_server.srv import cmmm_converter

def D_client(x):
    rospy.wait_for_service('dist_conv')
    try:
        conv_vari = rospy.ServiceProxy('dist_conv', cmmm_converter)
        resp1 = conv_vari(x)
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = int(sys.argv[1])
        
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s mm in cm"%(x))
    print("%s mm to cm = %s"%(x, D_client(x)))