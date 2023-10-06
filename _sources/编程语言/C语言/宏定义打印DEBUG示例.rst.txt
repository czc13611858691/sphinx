宏定义打印DEBUG示例
######################################

.. code-block:: C

    #ifdef ON_LOG_XCP_CMD_PARSE
    #define LOG_XCP_CMD_PARSE(format, ...) myPrint(format,##__VA_ARGS__)
    #else
    #define LOG_XCP_CMD_PARSE(format, ...)
    #endif