import rospy
from std_msgs.msg import String
import requests
from rospy_message_converter import json_message_converter
import sys

LAT = sys.argv[1]
LON = sys.argv[2]

APP_ID = '0cbcb61b71a97450075db693d7de6930'

def get_weather(lat = LAT, lon = LON, appid = APP_ID):
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'lat': lat, 'lon': lon, 'appid': appid}

    r = requests.get(url = URL, params = PARAMS)
    return r.json()

def talker():
    pub = rospy.Publisher('test_weather_publisher', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        msg = str(get_weather())
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
