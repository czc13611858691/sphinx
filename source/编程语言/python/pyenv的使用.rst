pyenv的使用
######################################

`windows下pyenv最简单安装教程 <https://baijiahao.baidu.com/s?id=1742653008854467791&wfr=spider&for=pc>`__

| pyenv使用
| 1、查看所有pyenv可以安装的版本：pyenv install --list
| 2、安装之前修改源：
| ①.pyenv文件下的.versions_cache.xml
| ②将想要下载的版本对应的url改为对应的https://npm.taobao.org/mirrors/python/3.8.0/python-3.8.0-amd64-webinstall.exe，只替换到python位置即可，后面的还按照原本的，不要动
| 3、改完后安装使用命令：pyenv install 3.9.0–对应版本
| 4、查看pyenv下所有的python安装版本：pyenv versions
| 5、跳转到对应版本：pyenv local 3.9.0
| ：pyenv install 3.9.0–对应版本
| 4、查看pyenv下所有的python安装版本：pyenv versions
| 5、跳转到对应版本：pyenv local 3.9.0
| 5、查看当前对应版本：pyenv version

安装scons

.. code:: 

   pip install scons==3.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
