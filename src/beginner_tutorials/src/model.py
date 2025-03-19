#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16MultiArray, MultiArrayLayout, MultiArrayDimension


def callback(data):
    rospy.loginfo(f"Received data: {data.data}")


def main():
    # 노드 초기화
    rospy.init_node('listener_and_publisher', anonymous=True)

    # Subscriber 설정
    rospy.Subscriber("pca9685", Int16MultiArray, callback)

    # Publisher 설정
    pub = rospy.Publisher('servo/command', Int16MultiArray, queue_size=10)

    # 루프 주기 설정 (1Hz)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # 발행할 메시지 생성
        number = Int16MultiArray()

        # data 필드 설정
        number.data = [1, 2, 3, 4, 5, 6, 7, 8]

        # 메시지 발행
        rospy.loginfo(f"Publishing: {number.data}")
        pub.publish(number)

        # 루프 대기
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
