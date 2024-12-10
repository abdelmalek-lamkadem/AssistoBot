

# **Navigation System**  


This project features a navigation system designed for the **Interactive Robotic Station**, aimed at enhancing the experience of students, teachers, administrators, and visitors in educational institutions. The system integrates an autonomous mobile robot and a touchscreen interface to provide intuitive guidance and personalized services.
 
---

### **Gazebo Simulation**:  
<p align="center">
    <img width="80%" src="https://github.com/reiniscimurs/DRL-robot-navigation/blob/main/env1.png">
</p>    

---

## **Key Features**  
- **Autonomous Navigation**: The robot guides users to desired destinations within the institution.  
- **Obstacle Avoidance**: Equipped with laser sensors and trained using **Deep Reinforcement Learning (DRL)**, the robot ensures safe navigation in dynamic environments.  
- **Touchscreen Interaction**: Users can input destinations, access timetables, and request administrative assistance.  
- **Customizable Deployment**: Adaptable to the layout and needs of different institutions.  

---

## **Technical Details**  
The navigation system is built using:  
- **Algorithm**: Twin Delayed Deep Deterministic Policy Gradient (TD3).  
- **Simulation**: ROS Gazebo simulator for development and testing.  
- **Platform**: ROS jazzy on Ubuntu 25.04 with Python 3.8.10 and PyTorch 1.10.  

---

### **Training Process**:  
<p align="center">
    <img width="100%" src="https://github.com/reiniscimurs/DRL-robot-navigation/blob/main/training.gif">
</p>  

---


### **Obstacle Detection with Rviz**:  
<p align="center">
    <img width="80%" src="https://github.com/reiniscimurs/DRL-robot-navigation/blob/main/velodyne.png">
</p>  
