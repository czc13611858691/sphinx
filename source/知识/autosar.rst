autosar
######################################

arxml解析
*********************************************

文章参考
=============================================

`python解析arxml--Apple的学习笔记 <https://www.jianshu.com/p/8039cb2b54d3>`_ 

开源库
=============================================

autosarfactory


xml文件格式python解析
=============================================

.. code-block:: python

    from lxml import etree
    if etree.QName(tree_root).localname == "AUTOSAR":
        shortNameNode = tree_root.findall("{*}AR-PACKAGES")
        for i in shortNameNode:
            for j in i:
                for k in j:
                    print("1")