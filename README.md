pytrace
=======

Python wrote script analyzes asterisk log.
Changed: 2016-03-03
It's so long time since last changed.

#
Changed: 2016-03-07
Write something.

#
Changed: 2016-03-18

使用说明：

    ./pytrace 电话号码 full日志

例如：

    ./pytrace 12345678 /var/log/asterisk/full

使用该程序可以根据提供的客户号码搜索出其呼叫流程，前提条件是在流程中需要出现客户号码，例如在dialplan中包含类似NoOp(~~${customer_number}~~)等相关输出。

这样就能快速查找问题。