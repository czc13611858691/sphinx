sphinx_rtd_theme 主题
######################################
.. code-block:: bash

    pip install sphinx_rtd_theme

**主题配置选项**

conf.py 中添加如下选项，修改sidebar侧边栏最大深度为不限

.. code-block:: python

    html_theme_options = {
        'navigation_depth': -1,
    }



`配置官方文档 <https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html>`_ 

`参考文章 <https://doclikecode.readthedocs.io/zh_CN/latest/4_theming/rtd-theme.html>`_ 