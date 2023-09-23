path
######################################

获取当前exe存放文件夹


.. code-block:: python

    import os
    import sys


    def GetRunFilePath():
        application_path = ""
        if getattr(sys, "frozen", False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        return application_path


    if __name__ == "__main__":
        print(GetRunFilePath())

    
