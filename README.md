# `ant_oxl` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/AB0l1n7/ant_oxl
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select ant_oxl --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 run ant_oxl image_publisher
ros2 run ant_oxl image_subscriber
```
# The video with lane detection can be seen with "rqt" visualization software, but it's just the most comfortable for me, not the only option.

![image](https://github.com/user-attachments/assets/26f7a686-c0b5-47f9-a6b8-dc1319803382)
![image](https://github.com/user-attachments/assets/91a7d7f2-622e-4501-8602-40d329810af8)
![image](https://github.com/user-attachments/assets/c8a797f3-afd1-4eab-985d-399c044504b7)


