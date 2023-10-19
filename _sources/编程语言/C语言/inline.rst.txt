inline
######################################

https://blog.csdn.net/m0_37616597/article/details/104138980

``inline`` 只是建议内联，并不会强制内联

可以给函数增加 ``__attribute__((always_inline))`` 属性让inline函数可以强制展开，但是仅限于ARM，因为attribute是GNU C特色之一。