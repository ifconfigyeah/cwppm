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
        # set default is new post
        self._newPost_ = True
        self._postId_ = None
        # show no login tip...
        self.lblSiteTitle.setText("<font color=red> No Login!</font>")
        # fill post-status combobox
        self.initPostStatus()
        # some event
        self.connect(self.exit_btn, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.conn_btn, QtCore.SIGNAL('clicked()'), self.loginWP)
        self.lw_posts.itemDoubleClicked.connect(self.posts_and_pages_slot)
        self.lw_pages.itemDoubleClicked.connect(self.posts_and_pages_slot)
        self.cb_isNewPost.toggled.connect(self.handlePostType)


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
            cfg = "cwppm.cfg"   # TODO
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
            
            # fill posts info in ListWidget
            self.getPosts()
            self.getPages()
            
        except Exception, ex:
            err = 'Connection your blog failed! ' + str(ex) + ', Pls try again!'
            self.conn_btn.setFocus()
            QtGui.QMessageBox.information(self, 'info', err, QtGui.QMessageBox.Ok)
            self.lblSiteTitle.setText("<font color=red> No Login.</font>")
            self.clearWithException()
            
    
    def doPost(self):
        post = WordPressPost()
        
        # get all post properties
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
        post.post_status = str(self.cb_post_status.currentText())
        
        try:
            # new post or page-type post
            if (self._newPost_):
                post.id = self.wp.call(posts.NewPost(post))
                QtGui.QMessageBox.information(self, 'info', "Post success!", QtGui.QMessageBox.Ok)
            else:
                print 'edit...'
                # edit a post
                if self._postId_ != None:
                    self.wp.call(posts.EditPost(self._postId_, post))
                    QtGui.QMessageBox.information(self, 'info', "Edit success!", QtGui.QMessageBox.Ok)
        except Exception, e:
            QtGui.QMessageBox.information(self, 'err', str(e), QtGui.QMessageBox.Ok)
        finally:
            self.clearWidget()
            self.getPosts()
            
    def initPostStatus(self):
        statusList = ['publish', 'draft', 'pending']
        self.cb_post_status.addItems(statusList)
        
        
    def changePostStatusIndex(self, status):
        if status == 'publish':
            self.cb_post_status.setCurrentIndex(0)
        if status == 'draft':
            self.cb_post_status.setCurrentIndex(1)
        if status == 'pending':
            self.cb_post_status.setCurrentIndex(2)

            
    def handlePostType(self):
        if self.cb_isNewPost.isChecked:
            self._newPost_ = True
        else: self._newPost_ = False
             

    def clearWidget(self):
        self.lnEdit_PostTitle.setText("")
        self.lnEditPostTags.setText("")
        self.lnEditPostCategories.setText("")
        self.txtEdit_PostContent.setText("")
        self._newPost_ = True
        self._postId_ = None
        
        
    def clearWithException(self):
        self.setWindowTitle('cwppm')
        self.lw_posts.clear()

    
    def getPosts(self):
        self.lw_posts.clear()
        self.wp_posts = self.wp.call(GetPosts({'number':'100000'}))
        for p in self.wp_posts:
            item = QString(p.title + ',' + p.id)
            self.lw_posts.insertItem(int(p.id), item)

    def getPages(self):
        self.lw_pages.clear()
        self.wp_pages = self.wp.call(GetPosts({'post_type': 'page'}, results_class=WordPressPage))
        for p in self.wp_pages:
            item = QString(p.title + ',' + p.id)
            self.lw_pages.insertItem(int(p.id), item) 
    
    
    def posts_and_pages_slot(self, item):
        self.cb_isNewPost.setChecked(False)
        self._postId_ = str(item.text()).split(',')[1]
        if self._postId_ != None and self._postId_.strip() != '':
            try:
                post = self.wp.call(posts.GetPost(self._postId_))
                self.lnEdit_PostTitle.setText(post.title)
                self.txtEdit_PostContent.setText(post.content)
                self.changePostStatusIndex(post.post_status)
                self._newPost_ = False
            except Exception, e:
                QtGui.QMessageBox.information(self, 'err', str(e), QtGui.QMessageBox.Ok)
        else:
            mes = 'posts is not exists, pls click connection button to refresh!'
            QtGui.QMessageBox.information(self, 'info', mes, QtGui.QMessageBox.Ok)
            
    
if __name__ == "__main__":
    
    app = PyQt4.QtGui.QApplication(sys.argv)
    dlgPost = PostMain()
    dlgPost.show()
    sys.exit(app.exec_())
        
