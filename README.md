本程序为基于树莓派与MG995舵机实现的对于宿舍机械锁的自动开关锁装置。用户只需要访问指定网站，方可实现对宿舍门锁的遥控解锁

服务端需要搭载的库（Debian）：[1]
①Flask
sudo apt - get update
sudo apt - get install python - pip
sudo pip3 install flask
②RPi.GPIO库：
sudo apt - get install python3 - rpi - gpio

随后运行start.sh脚本
./start.sh

参考文献：

[1] coderzach. 在Linux(Ubuntu/Debian)上快速开始你的第一个Flask应用_python flask linux-CSDN博客[EB/OL]. (2023-11-20)[2024-11-20]. https://blog.csdn.net/coderzach/article/details/134780004.
[2] 小雨coding. 树莓派人脸识别实际应用：人脸识别门禁_树莓派安装pybluez-CSDN博客[EB/OL]. (2020-02-27)[2024-11-20]. https://blog.csdn.net/qq_29855577/article/details/104538392.

