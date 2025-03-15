import rclpy # Ros2 python API
from rclpy.node import Node
from sensor_msgs.msg import Image # Ros2 üzenet típus képekhez
from cv_bridge import CvBridge # Biztosítja a Ros2 és opencv közötti átmenetet
import cv2 # Képfeldolgozási könyvtár

class VideoPublisher(Node):
    def __init__(self, video_source="/home/ajr/ros2_ws/src/ant_oxl/road_video.mp4"):  # video_source a videó elérési útja
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, '/image', 10) # Létrehozza a publishert Image típusú üzenethez, a topic neve /image
        self.bridge = CvBridge() # Inicializálja a CvBridge objektumot

        # Videóforrás inicializálása
        self.cap = cv2.VideoCapture(video_source)

        if not self.cap.isOpened():
            # Ellenőrzi sikerült-e megnyitni a videófájlt
            # Ha nem, akkor naplózza a hibát és leállítja a Ros2 rendszert
            self.get_logger().error(f"Failed to open video source: {video_source}")
            rclpy.shutdown()
            return
        
        self.timer = self.create_timer(1/30, self.timer_callback)  # Másodpercenként 30-szor meghívja a timer_callback függvényt

        self.get_logger().info("Video Publisher Node has started!") # Informáló üzenetet ír ki sikeres indítás esetén

    def timer_callback(self):
        ret, frame = self.cap.read() # Képkockát olvas a videóból
        # ret egy bool ami az olvasás sikerességét jelzi, frame a képkocka
        if not ret:
            # Ha a ret - bool false-ot ad, akkor hibát jelez és a videót az elejére állítja
            self.get_logger().warning("Video stream ended or error reading frame.")
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Újrakezdés az elejéről
            return

        # OpenCV kép konvertálása Ros Image üzenetté
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")

        # Publikálás a Ros2 topicba topicba
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing video frame")

    def destroy_node(self):
        # Ez a függvény van meghívva a Node leállításakor 
        self.cap.release()  # Felszabadítja a videófájlt
        super().destroy_node() # Leállítja a Node-ot

def main(args=None):
    rclpy.init(args=args) # Inicializálja a Ros2 környezetet

    video_publisher = VideoPublisher("/home/ajr/ros2_ws/src/ant_oxl/road_video.mp4")  # Módosítani kell a fájl nevét szükség szerint

    rclpy.spin(video_publisher)

    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
