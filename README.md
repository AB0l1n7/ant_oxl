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

![image](https://github.com/user-attachments/assets/26f7a686-c0b5-47f9-a6b8-dc1319803382)
![image](https://github.com/user-attachments/assets/91a7d7f2-622e-4501-8602-40d329810af8)
![image](https://github.com/user-attachments/assets/eca0a282-c346-45c0-9a4f-3a1186063290)


# Delete this part if you are using it as a template

ROS 2 pacage template, to get started, use template by clicking on the Green button labeled [`Use this template`](https://github.com/AB0l1n7/ant_oxl/generate) / [`Create new repository`](https://github.com/AB0l1n7/ant_oxl/generate). 

<p align="center"><img src="img/use_this_template01.png" width="60%" /></p>


Let's assume 
- your Github username is `mycoolusername`
- your ROS 2 repo shold be `cool_ros2_package`

Replace everything in the cloned repo:

- `ant_oxl` >> `cool_ros2_package` (the folder was already renamed after `Use this template`)
- `AB0l1n7` >> `mycoolusername`
- find all `todo` strings and fill the blanks

The easiest way is VS code:

<p align="center"><img src="img/replace01.png" width="90%" /></p>

> [!IMPORTANT]  
> Don't forget to rename the directory (folder) and the file too.

Now `colcon build` your ROS 2 package and you can start wokring.
