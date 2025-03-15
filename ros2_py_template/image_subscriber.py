import rclpy # Ros2 python API
from rclpy.node import Node
from sensor_msgs.msg import Image # Ros2 üzenet típus képekhez
from cv_bridge import CvBridge # Biztosítja a Ros2 és opencv közötti átmenetet
import cv2 # Képfeldolgozási könyvtár

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')

        self.subscription = self.create_subscription( # létrehozza a subscribert
            Image, # Image típusú üzeneteket várunk
            '/image',  # /image topicra iratkozunk fel
            self.listener_callback, # listener_callback függvény lesz meghívva új káp érkezésekor
            10)
        
        # Inicializálja CvBridge
        self.bridge = CvBridge()

    def listener_callback(self, msg): # Akkor kerül meghívásra mikor új kép érkezik
        self.get_logger().info('Received an image!') # Kiírja, hogy új képet kaptunk
        
        
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8') #A ros2 üzenetet opencv formátumú képpé konvertálja
        except Exception as e:
            # Hiba esetén az expect rész lép működésbe
            self.get_logger().error(f"Could not convert image: {e}")
            return
        
        img = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) # Fekete fehérbe váltja a képet
       
        img = cv2.GaussianBlur(img, (5, 5), 1.4) # A hibák korrigálására elhomájosítjuk

        edges = cv2.Canny(img, 100, 200) # Canny edge detectort alkalmazzuk

        cv2.imshow("Canny Edge Detection", edges) # Kijelzi a képet
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args) #Ros2 környezet inicializálása
    image_subscriber = ImageSubscriber() # ImageSubscriber objektum létrehozása
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
