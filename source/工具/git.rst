git
===


列出远端地址和名称
------------------

使用以下命令列出所有Git远程仓库的列表：

.. code:: shell

   git remote -v

这将显示每个远程仓库的名称和URL。


设置代理
------------------------------------------------

.. code-block:: bash

   git config --global http.proxy 127.0.0.1:7890
   git config --global https.proxy 127.0.0.1:7890