# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\asus\eric4_workspaces\DlgPost.ui'
#
# Created: Tue Oct 29 17:07:03 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wp_post(object):
    def setupUi(self, wp_post):
        wp_post.setObjectName(_fromUtf8("wp_post"))
        wp_post.resize(840, 599)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wp_post.sizePolicy().hasHeightForWidth())
        wp_post.setSizePolicy(sizePolicy)
        wp_post.setMinimumSize(QtCore.QSize(840, 599))
        wp_post.setMaximumSize(QtCore.QSize(840, 599))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("blog.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        wp_post.setWindowIcon(icon)
        self.post_btn = QtGui.QPushButton(wp_post)
        self.post_btn.setGeometry(QtCore.QRect(420, 560, 75, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.post_btn.sizePolicy().hasHeightForWidth())
        self.post_btn.setSizePolicy(sizePolicy)
        self.post_btn.setObjectName(_fromUtf8("post_btn"))
        self.exit_btn = QtGui.QPushButton(wp_post)
        self.exit_btn.setGeometry(QtCore.QRect(530, 560, 75, 23))
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.lblSiteTitle = QtGui.QLabel(wp_post)
        self.lblSiteTitle.setGeometry(QtCore.QRect(10, 10, 741, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSiteTitle.sizePolicy().hasHeightForWidth())
        self.lblSiteTitle.setSizePolicy(sizePolicy)
        self.lblSiteTitle.setText(_fromUtf8(""))
        self.lblSiteTitle.setTextFormat(QtCore.Qt.AutoText)
        self.lblSiteTitle.setScaledContents(True)
        self.lblSiteTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblSiteTitle.setWordWrap(False)
        self.lblSiteTitle.setObjectName(_fromUtf8("lblSiteTitle"))
        self.lnEdit_PostTitle = QtGui.QLineEdit(wp_post)
        self.lnEdit_PostTitle.setGeometry(QtCore.QRect(250, 40, 501, 21))
        self.lnEdit_PostTitle.setObjectName(_fromUtf8("lnEdit_PostTitle"))
        self.lblPostTitle = QtGui.QLabel(wp_post)
        self.lblPostTitle.setGeometry(QtCore.QRect(200, 40, 54, 12))
        self.lblPostTitle.setScaledContents(True)
        self.lblPostTitle.setObjectName(_fromUtf8("lblPostTitle"))
        self.lblPostTitle_2 = QtGui.QLabel(wp_post)
        self.lblPostTitle_2.setGeometry(QtCore.QRect(200, 70, 54, 12))
        self.lblPostTitle_2.setScaledContents(True)
        self.lblPostTitle_2.setObjectName(_fromUtf8("lblPostTitle_2"))
        self.txtEdit_PostContent = QtGui.QTextEdit(wp_post)
        self.txtEdit_PostContent.setGeometry(QtCore.QRect(250, 70, 571, 391))
        self.txtEdit_PostContent.setDocumentTitle(_fromUtf8(""))
        self.txtEdit_PostContent.setObjectName(_fromUtf8("txtEdit_PostContent"))
        self.lblPostTags = QtGui.QLabel(wp_post)
        self.lblPostTags.setGeometry(QtCore.QRect(210, 480, 54, 21))
        self.lblPostTags.setScaledContents(True)
        self.lblPostTags.setObjectName(_fromUtf8("lblPostTags"))
        self.lnEditPostTags = QtGui.QLineEdit(wp_post)
        self.lnEditPostTags.setGeometry(QtCore.QRect(250, 480, 161, 21))
        self.lnEditPostTags.setObjectName(_fromUtf8("lnEditPostTags"))
        self.lblPostCategories = QtGui.QLabel(wp_post)
        self.lblPostCategories.setGeometry(QtCore.QRect(570, 480, 71, 21))
        self.lblPostCategories.setScaledContents(True)
        self.lblPostCategories.setObjectName(_fromUtf8("lblPostCategories"))
        self.lnEditPostCategories = QtGui.QLineEdit(wp_post)
        self.lnEditPostCategories.setGeometry(QtCore.QRect(650, 480, 171, 21))
        self.lnEditPostCategories.setText(_fromUtf8(""))
        self.lnEditPostCategories.setObjectName(_fromUtf8("lnEditPostCategories"))
        self.lbl_Pages = QtGui.QLabel(wp_post)
        self.lbl_Pages.setGeometry(QtCore.QRect(10, 340, 54, 12))
        self.lbl_Pages.setScaledContents(True)
        self.lbl_Pages.setObjectName(_fromUtf8("lbl_Pages"))
        self.lbl_Posts = QtGui.QLabel(wp_post)
        self.lbl_Posts.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.lbl_Posts.setScaledContents(True)
        self.lbl_Posts.setObjectName(_fromUtf8("lbl_Posts"))
        self.lblPostTags_2 = QtGui.QLabel(wp_post)
        self.lblPostTags_2.setGeometry(QtCore.QRect(420, 480, 131, 21))
        self.lblPostTags_2.setScaledContents(True)
        self.lblPostTags_2.setObjectName(_fromUtf8("lblPostTags_2"))
        self.conn_btn = QtGui.QPushButton(wp_post)
        self.conn_btn.setGeometry(QtCore.QRect(750, 560, 75, 23))
        self.conn_btn.setObjectName(_fromUtf8("conn_btn"))
        self.tv_posts = QtGui.QTreeView(wp_post)
        self.tv_posts.setGeometry(QtCore.QRect(10, 60, 181, 271))
        self.tv_posts.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tv_posts.setAnimated(True)
        self.tv_posts.setHeaderHidden(True)
        self.tv_posts.setObjectName(_fromUtf8("tv_posts"))
        self.tv_pages = QtGui.QTreeView(wp_post)
        self.tv_pages.setGeometry(QtCore.QRect(10, 360, 181, 221))
        self.tv_pages.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tv_pages.setAnimated(True)
        self.tv_pages.setHeaderHidden(True)
        self.tv_pages.setObjectName(_fromUtf8("tv_pages"))

        self.retranslateUi(wp_post)
        QtCore.QObject.connect(self.exit_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), wp_post.close)
        QtCore.QMetaObject.connectSlotsByName(wp_post)

    def retranslateUi(self, wp_post):
        wp_post.setWindowTitle(_translate("wp_post", "cwppm", None))
        self.post_btn.setText(_translate("wp_post", "Publish", None))
        self.exit_btn.setText(_translate("wp_post", "Exit", None))
        self.lblPostTitle.setText(_translate("wp_post", "Title", None))
        self.lblPostTitle_2.setText(_translate("wp_post", "Content", None))
        self.lblPostTags.setText(_translate("wp_post", "Tags:", None))
        self.lblPostCategories.setText(_translate("wp_post", "Categories:", None))
        self.lbl_Pages.setText(_translate("wp_post", "Pages", None))
        self.lbl_Posts.setText(_translate("wp_post", "Posts", None))
        self.lblPostTags_2.setText(_translate("wp_post", "(muti use \',\' sep)", None))
        self.conn_btn.setText(_translate("wp_post", "connection", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    wp_post = QtGui.QDialog()
    ui = Ui_wp_post()
    ui.setupUi(wp_post)
    wp_post.show()
    sys.exit(app.exec_())

