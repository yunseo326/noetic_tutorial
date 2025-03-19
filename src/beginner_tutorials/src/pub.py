#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def publisher():
    rospy.init_node('simple_publisher', anonymous=True)  # 노드 초기화
    pub = rospy.Publisher('number_topic', Int32, queue_size=10)  # Publisher 생성
    rate = rospy.Rate(1)  # 1Hz로 publish

    while not rospy.is_shutdown():
        number = 3  # publish할 숫자
        rospy.loginfo(f"Publishing: {number}")  # 출력 로그
        pub.publish(number)  # 메시지 publish
        rate.sleep()  # 1초 대기

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
