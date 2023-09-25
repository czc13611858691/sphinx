Bat命令行
=========

1. robocopy备份
---------------

`robocopy命令行程序-百度百科 <https://baike.baidu.com/item/robocopy/4883980?fr=aladdin>`__

.. code:: shell

   @echo off
   set "SrcDir=xx"
   Set "DstDir=bb"

   robocopy "%SrcDir%" "%DstDir%" /s /PURGE /MT:128 /ETA

   pause


2. 压缩文件
-----------

`windows脚本bat做文件备份 <https://www.shuzhiduo.com/A/obzbEMOBdE/>`__

.. code:: shell

   set "YYYYmmdd=%yyyy%%mm%%day%"
   set YYYYmmdd=%date:~0,4%%date:~5,2%%date:~8,2%
   set "YYYYmmdd=%YYYYmmdd: =0%"
   set hhmiss=%time:~0,2%%time:~3,2%%time:~6,2%
   set "hhmiss=%hhmiss: =0%"
   set filename=BakAllProgram%YYYYmmdd%_%hhmiss%.rar
    
   cd ..
    
   echo 进入备份目录
   echo %cd%
    
   ::源路径
   set sourcesDir=%cd%\备份\bakdir
   ::目标路径
   set zipfile=%cd%\备份/%filename%
   echo WINRAR压缩文件...
   "C:\Program Files\WinRAR\Rar.exe" a -as -r -ep1 "%zipfile%" "%sourcesDir%"
   echo 删除备份文件...
   rd/s/q %cd%\备份\bakdir
   pause
