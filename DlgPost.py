# -*- coding: utf-8 -*-

"""
Module implementing PostMain.
"""

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Ui_DlgPost import Ui_wp_post
from wordpress_xmlrpc import Client, WordPressPost, WordPressBlog, WordPressPage
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo, GetUsersBlogs
from wordpress_xmlrpc.compat import xmlrpc_client
import PyQt4
import sys
import os
import re
import time
import ConfigParser
import codecs
import mimetypes
from pprint import pprint
from wordpress_xmlrpc import XmlrpcMethod


class PostMain(QMainWindow, Ui_wp_post):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.txtEdit_PostContent.setAcceptRichText(0)
        self.txtEdit_PostContent.setUndoRedoEnabled(0)
        self.connect(self.exit_btn, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.conn_btn, QtCore.SIGNAL('clicked()'), self.loginWP)
        # show no login tip...
        self.lblSiteTitle.setText("<font color=red> No Login! Click conn button.</font>")
    

    @pyqtSignature("")
    def on_post_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.doPost()
        
    
    @pyqtSignature("")
    def on_exit_btn_clicked(self):
        """
        Slot documentation goes here.
        """
        
        
    def closeEvent(self, event):
        if (len(self.lnEdit_PostTitle.text()) > 0 or len(self.txtEdit_PostContent.toPlainText()) > 0):
            reply = QtGui.QMessageBox.question(self, 'Message', 'Do you want to drop current post and close cwppm?', \
                QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
    
    def wp_data(self):
        pass
        
        
    def loginWP(self):
        
        self.isWin = False
        if sys.platform.startswith('win'):
            self.isWin = True

        # reading configuration file...
        try:
            cfg = "cwppm.cfg"
            config = ConfigParser.ConfigParser()
            if not self.isWin:
                config.read(cfg)
            else:
                config.readfp(codecs.open(cfg, "r", "utf-8-sig"))
                
            xmlrpc_addr = config.get("global", "xmlrpc_addr")
            username = config.get("global", "username")
            passwd = config.get("global", "passwd")
            
        except Exception, e:
            err = 'Read config file failed, Error at %s by %s' %(cfg, e)
            QtGui.QMessageBox.information(self, 'err', err, QtGui.QMessageBox.Ok)
            
        try:
            self.wp = Client(xmlrpc_addr, username, passwd)
            print 'login...'
            WPUser = self.wp.call(GetUserInfo())
            WPBlog = self.wp.call(GetUsersBlogs())
            self.setWindowTitle('cwppm - ' + WPBlog[0].name)
            self.lblSiteTitle.setText("<font color=green><b>Welcome back, " + WPUser.username + "!</b></font>")
            
            # fill posts and pages tree view
            self.getPosts()
            self.getPages()
            
        except Exception, ex:
            err = 'Connection failed! ' + str(ex) + ', click [conn] button to try again!'
            self.conn_btn.setFocus()
            QtGui.QMessageBox.information(self, 'info', err, QtGui.QMessageBox.Ok)
            self.lblSiteTitle.setText("<font color=red> No Login.</font>")
            self.clearWithException()
            
    
    def doPost(self):
        post = WordPressPost()
        post.title = str(unicode(self.lnEdit_PostTitle.text()))
        post.content = str(unicode(self.txtEdit_PostContent.toPlainText()))
        tag = unicode(self.lnEditPostTags.text())
        category = unicode(self.lnEditPostCategories.text())
        # use ',' split multi-tag or category
        if ',' in tag: tag = tag.split(',')
        if ',' in category: category = category.split(',')
        post.terms_names = {
            'post_tag': tag,
            'category': category
        }
        post.post_status = 'publish'		# 'draft'
        
        try:
            post.id = self.wp.call(NewPost(post))
            self.clearWidget()
            QtGui.QMessageBox.information(self, 'cwppm', "Post success! " + "id: " + post.id, QtGui.QMessageBox.Ok)
            self.getPosts()
        except Exception, e:
             QtGui.QMessageBox.information(self, 'err', str(e), QtGui.QMessageBox.Ok)
            
        
    def clearWidget(self):
        self.lnEdit_PostTitle.setText("")
        self.lnEditPostTags.setText("")
        self.lnEditPostCategories.setText("")
        self.txtEdit_PostContent.setText("")
        
        
    def clearWithException(self):
        self.setWindowTitle('cwppm')
        self.tv_posts.reset()
        self.tv_pages.reset()

    
    def getPosts(self):
        self.wp_posts = self.wp.call(GetPosts({'number':'100000'}))
        postModel = QStandardItemModel(len(self.wp_posts), 1, parent=self.tv_posts)
        for i, post in enumerate(self.wp_posts):
            item = QStandardItem(QString(post.title))
            postModel.setItem(i, item)
        self.tv_posts.setModel(postModel)
        
        # hidden empty rows
        # TODO: use
        

    def getPages(self):
        self.wp_pages = self.wp.call(GetPosts({'post_type': 'page'}, results_class=WordPressPage))
        pageModel = QStandardItemModel(len(self.wp_pages), 1, parent=self.tv_pages)
        for i, page in enumerate(self.wp_pages):
            item = QStandardItem(QString(page.title))
            pageModel.setItem(i, item)      # TODO int(page.id), send clicked sign(rowId) to SLOT, then load a post by rowId(post.id) for quick look or edit
        self.tv_pages.setModel(pageModel)
    
    
if __name__ == "__main__":
    
    app = PyQt4.QtGui.QApplication(sys.argv)
    dlgPost = PostMain()
    dlgPost.show()
    sys.exit(app.exec_())
        
