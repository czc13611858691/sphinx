beyond
######################################

比较文件夹命令行调用
====================

BCompare.exe "C:\\左侧文件夹" "C:\\右侧文件夹"

bat example

.. code:: bat

   @REM example use:
   @REM .\BeyondCompare.bat bsw
   @REM .\BeyondCompare.bat rte
   @REM .\BeyondCompare.bat os

   if "%1" == "bsw" (
       "D:\Program Files (x86)\Beyond Compare 3\BCompare.exe" "BasicSoftware\src\bsw" "BasicSoftware\src\bsw1"
   )
   if "%1" == "rte" (
       "D:\Program Files (x86)\Beyond Compare 3\BCompare.exe" "BasicSoftware\src\rte" "BasicSoftware\src\rte1"
   )
   if "%1" == "os" (
       "D:\Program Files (x86)\Beyond Compare 3\BCompare.exe" "BasicSoftware\src\os" "BasicSoftware\src\os1"
   )

也可以使用 ``BComp.exe`` ，BCompare.exe不关闭比较窗口 bat
程序一直会在那运行。

.. _header-n7:

复制不同的文件到另一个文件
==========================

选择需要操作的文件，然后选择同步-->镜像到左侧/右侧

.. _header-n9:

比较时界面显示有差异，打开无差异的现象
======================================

https://blog.csdn.net/qq_43592064/article/details/119565913

BeyondCompare比较时界面显示有差异，打开无差异的现象，这个博客里有解决方法

会话设置 --> 比较 --> 比较内容 and 基于规则的比较 and 更新默认会话值

