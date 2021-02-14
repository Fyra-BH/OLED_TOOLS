***OLED取模工具***

![ba](https://github.com/Fyra-BH/OLED_TOOLS/blob/main/pic/ba.jpg)

试用前请确保你的电脑已经安装opencv

否则使用 pip install opencv-python安装

**简介：** 本程序可以读取视频，将其逐帧转为OLED点阵数据，并写入输出文件，适用的OLED屏幕分辨率为128*64



**使用说明：** 进入script目录，使用前先修改settings.json文件，设置输入输出文件路径，然后直接运行bitmap_gen.py即可



**注意**：最后生成的点阵文件的正确用法是：以二进制方式打开，每次读取1024个字节，并依次写入OLED帧缓冲，直到读取完毕。

