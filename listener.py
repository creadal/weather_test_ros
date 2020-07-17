import rospy
import json
from std_msgs.msg import String
from rospy_message_converter import json_message_converter
import ast
from datetime import datetime

def callback(data):
    message = json_message_converter.convert_ros_message_to_json(data)
    weather = json.loads(message).values()[0]
    weather = ast.literal_eval(weather)

    seconds = rospy.get_time()
    dt = datetime.fromtimestamp(seconds)

    print(str(dt) + ' Test weather subscriber - the weather in ' + str(weather['name']) + ' is ' + str(weather['weather'][0]['description']))


def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('test_weather_publisher', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
