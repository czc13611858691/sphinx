pcan
######################################

python-can库的注意事项
*********************************************

python can 库 3.3.4 版本可以正常使用pcan，但是4.2.0会有问题，经过排查发现是软件bug。


**bug解决方案如下:**

.. figure:: pcan/example.png
    :align: center
    :figwidth: 550px

    源代码

**改为如下:**

.. code-block:: python

    if uptime.boottime() is None:
        boottimeEpoch = 0
    else:
        boottimeEpoch = (datetime.now()-datetime(1970, 1, 1)).total_seconds()


脚本收发示例
*********************************************
.. code-block:: python

    import can
    can0 = can.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)
    # msg = can.Message(arbitration_id=0x123,data=[0, 25, 0, 1, 3, 1, 4, 1])
    can0.flash(True)
    msg=can0.recv()
    can0.flash(False)
    try:
        can0.send(msg)
        print("Message sent on {}".format(can0.channel_info))
    except can.CanError:
        print("Message NOT sent")

灯的控制
*********************************************
.. code-block:: python

    can0.flash(True)
    #亮红灯

    False
    #亮绿灯

log文件的写入
*********************************************
.. code-block:: python

    import can
    import time
    can0 = can.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=500000)
    msg = can.Message(arbitration_id=0x123,data=[0, 25, 0, 1, 3, 1, 4, 1])
    logger = can.Logger('bus_log.asc')
    for i in range(1000):
        try:
            can0.send(msg)
            msg.is_rx=False
            logger.on_message_received(msg)
            time.sleep(0.001)
        except can.CanError:
            print("Message NOT sent")
    can0.shutdown()
    logger.stop()

消息打印示例
*********************************************
.. code-block:: python

    import can
    from can import Notifier, SizedRotatingLogger
    import time, datetime
    can0 = can.Bus(bustype="pcan", channel="PCAN_USBBUS1", bitrate=500000)
    msg = can.Message(arbitration_id=0x123, data=[0, 25, 0, 1, 3, 1, 4, 1])
    for i in range(1000):
        try:
            can0.send(msg)
            msg.is_rx = False
            print(datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3], end="\t")
            print("RX\t", end="\t")
            print("id:%#x" % msg.arbitration_id, end="\t")
            print("data:", end="")
            for i in msg.data:
                print("%#.2x" % i, end=" ")
            print("")
            time.sleep(0.001)
        except can.CanError:
            print("Message NOT sent")
    can0.shutdown()

logging文件示例
*********************************************
.. code-block:: python

    import can
    from can import Notifier, SizedRotatingLogger
    import time, datetime
    import logging
    logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    datefmt='%S',
                    filename='can.log',
                    filemode='w')
    can0 = can.Bus(bustype="pcan", channel="PCAN_USBBUS1", bitrate=500000)
    msg = can.Message(arbitration_id=0x123, data=[0, 25, 0, 1, 3, 1, 4, 1])
    for i in range(1000):
        try:
            can0.send(msg)
            msg.is_rx = False
            logMsg=''
            logMsg+=datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]+"\t"
            logMsg+= "TX\t"
            logMsg+= "id:%#x" % msg.arbitration_id +"\t"
            logMsg+= "data:"
            for i in msg.data:
                logMsg+= "%#.2x" % i +" "
            logging.info(logMsg)
            time.sleep(0.001)
        except can.CanError:
            logging.debug("Message NOT sent")
    can0.shutdown()


过滤器设置示例
*********************************************
.. code-block:: python

    can0.set_filters([{"can_id": 0x582, "can_mask": 0x582, "extended": False}])

