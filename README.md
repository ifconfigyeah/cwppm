cwppm
=====

免费的跨平台WP博客发布工具

最初在Mac下面没有找到免费的wordpress远程发布工具，所以自己折腾了一个。基本上，目前只有最简单、最核心的功能 -- 发布博客。

Python不是强项，PyQt4就更加是了。在sourceforge又无缘无故被墙后，一整个下午的时间几乎是看着诺基亚的C++版本的API搞了一点。加上eric4的APIs设置了却无法保存，这个原因倒是知道，多半和win7的权限有关系，Python装在C盘。

是不是会继续完善看情况了，windows下有很多免费的博客发布工具（像是微软的live writer、office系列等），至于Mac版本我打算回头用cocoa重写，搞一个native和powerful的版本，不过时间暂定。总之，如果仅仅需要一个简单而且免费的跨平台的WordPress发布工具，不妨试试这个还算方便的小东西。


![sample 1](https://raw.github.com/ifconfigyeah/cwppm/sample.png)

环境需要：

1. Python2.7 [http://www.python.org/](http://www.python.org/)
2. PyQt4 [http://www.riverbankcomputing.co.uk/software/pyqt/download](http://www.riverbankcomputing.co.uk/software/pyqt/download)
3. python-wordpress-xmlrpc  [https://pypi.python.org/pypi/python-wordpress-xmlrpc](https://pypi.python.org/pypi/python-wordpress-xmlrpc)




使用方法：
 
1. 修改cwppm.cfg配置文件，填入你博客的xmlrpc地址、登陆用户名、密码。 
2. `python DlgPost.py
3. 点击connection连接按钮，登陆，发布博客。



其他说明：

1. 任何问题、建议、Bug报告十分欢迎。
2. 这次的半成品有点对不起大家了，希望后面有机会更新，实现一些这次未能实现的想法。