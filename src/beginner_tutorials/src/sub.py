#!/usr/bin/env python

import rospy
from std_msgs.msg import String  # 예시로 String 메시지 타입을 사용

def callback(data):
    rospy.loginfo(f"Received data: {data.data}")

def listener():
    rospy.init_node('listener_node', anonymous=True)

    # 'chatter'라는 토픽을 구독
    rospy.Subscriber("chatter", String, callback)

    rospy.spin()  # 계속해서 데이터를 받을 수 있도록 유지

if __name__ == '__main__':
    try:
        listener()  # listener() 함수 실행
    except rospy.ROSInterruptException:
        pass  # ROS 종료시 예외 처리
