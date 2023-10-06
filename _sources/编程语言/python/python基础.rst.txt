python基础
######################################

main函数声明
*********************************************

.. code-block:: python

   if __name__ == "__main__":

python hex字符串转int
*********************************************

.. code-block:: python

   int(hex_str, 16)

打印十六进制例子
*********************************************

.. code-block:: python

   print('%#.8x'%num)

意思是打印宽度为 8 个宽度的十六进制字符串。


requirements.txt
*********************************************

库的导出
=============================================

.. code-block:: bash

   pip freeze > requirements.txt

库的导入
=============================================
.. code-block:: bash

   pip install -r requirements.txt

镜像网站
*********************************************

pip install 后加上 ``-i https://mirror.baidu.com/pypi/simple`` 可以通过国内网站下载 python 库，加快下载速度。

