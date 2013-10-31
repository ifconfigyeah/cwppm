cwppm
=====

简单的跨平台WP博客发布工具

最初在Mac下面没有找到免费的wordpress远程发布工具，所以自己折腾了一个。

目前实现了的功能有：

1. 发布博客

2. 显示已发博客和页面列表

3. 双击列表中某条博客，可以自动读取博客的标题和内容，进行编辑。(暂不支持图片的发布和修改)

4. 支持针对单条博客进行状态修改，发布、草稿、待定。

是不是会继续完善看情况了，win下有很多免费的博客发布工具（像是微软的live writer、office系列等），至于Mac版本我打算回头用cocoa重写，搞一个native和powerful的版本。

总之，如果仅仅需要一个简单而且免费的跨平台的WordPress发布工具，不妨试试这个还算方便的小东西。


![sample 1](https://raw.github.com/ifconfigyeah/cwppm/master/sample1.png)
![sample 2](https://raw.github.com/ifconfigyeah/cwppm/master/sample2.png)

环境需要：

1. Python2.7 [http://www.python.org/](http://www.python.org/)
2. PyQt4 [http://www.riverbankcomputing.co.uk/software/pyqt/download](http://www.riverbankcomputing.co.uk/software/pyqt/download)
3. python-wordpress-xmlrpc  [https://pypi.python.org/pypi/python-wordpress-xmlrpc](https://pypi.python.org/pypi/python-wordpress-xmlrpc)




使用方法：
 
1. 修改cwppm.cfg配置文件，输入并保存你博客的xmlrpc地址、登陆名和密码。 
2. 在命令行下运行 `python DlgPost.py`
3. 点击connection按钮登陆，发布博客。



其他说明：

1. 任何使用问题、建议、Bug报告十分欢迎。
2. 因为对python一知半解，QT更加一无所知，几乎折腾了三个下午才实现了核心的一点功能。所以，如果有大牛和爱好者愿意帮助一起完善这个小工具，将十分高兴！
2. 这次的半成品有点对不起大家了，希望后面有机会更新，实现一些这次未能实现的想法。