MksSimpleFOC
######################################

`CSDN - Simple FOC Makerbase教程 <https://blog.csdn.net/gjy_skyblue/category_10936827.html>`_ 

`Github simplefoc-MKS <https://github.com/makerbase-mks/simplefoc-MKS>`_ 

.. figure:: MksSimpleFOC/2023-10-05-09-54-55.png
    :align: center
    :figwidth: 550px

github 仓库中有如下内容

- 原理图 ArduinoFOC_V2.0.3.pdf
- 磁编码器 AS5600 原理图 MKS AS5600 V1.0_002.pdf
- 若干数据手册

.. figure:: MksSimpleFOC/2023-10-05-10-02-23.png
    :align: center
    :figwidth: 550px

    驱动板实物图

.. figure:: MksSimpleFOC/2023-10-05-10-02-45.png
    :align: center
    :figwidth: 550px

    磁编码器实物图

.. figure:: MksSimpleFOC/2023-10-05-10-12-26.png
    :align: center
    :figwidth: 550px

    AS5600编码器原理图

**问**: AS5600编码器是用来做什么的？

**答**: AS5600是一种易于编程的具有12位高分辨率模拟或PWM输出的磁性旋转位置传感器。这个非接触式模块可以检测出磁铁径向  ``磁轴转动的绝对角度`` 。

**问**: 上述原理图中每个引脚的作用?

**答**: 可以参考下图:

.. figure:: MksSimpleFOC/2023-10-05-10-19-28.png
    :align: center
    :figwidth: 550px

    SOIC-8 Pin Description

AS5600 支持 5V 电压供电或者 3.3V 电压供电， 原理图中使用的是 5V 供电的方式。

**问**: DIR 可以选择 CW/CCW 方式，这两种方式有什么区别?

CW：clockwise 顺时针

CCW：counterclockwise 逆时针

数据手册中的解释如下: 

.. figure:: MksSimpleFOC/2023-10-05-10-28-05.png
    :align: center
    :figwidth: 550px

.. note:: 这里的顺时针和逆时针指的是？

    我目前的理解是，顺时针配置，顺时针旋转后角度+，逆时针配置后，逆时针旋转角度+

