github图片不显示
######################################

**参考文章链接**

- `CSDN- github图片不显示的问题如何解决🤒 <https://blog.csdn.net/kaien1226/article/details/113885671>`_ 
- `知乎 Github图片显示不出来? 两步解决 <https://zhuanlan.zhihu.com/p/345258967>`_ 

windows 系统下打开文件 ``C:\Windows\System32\drivers\etc\hosts``

使用在线网页工具 IP地址查询,

我使用的 工具网页是 https://ip.900cha.com/github.com.html

.. figure:: github图片不显示/2023-10-05-09-40-31.png
    :align: center
    :figwidth: 550px

查询以下两个网页的 IP 地址:

- github.com
- raw.githubusercontent.com

文件末尾添加对应的 IP 地址:

.. code-block:: 

    20.205.243.166 github.com

    185.199.109.133 raw.githubusercontent.com

修改后效果如下:

.. figure:: github图片不显示/2023-10-05-09-43-19.png
    :align: center
    :figwidth: 550px

    