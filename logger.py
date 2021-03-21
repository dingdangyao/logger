import logging
import os
from logging import handlers

class Logger(object):

    def __init__(self, logPath, logFileName, logMaxFileSize=30, logMaxFileNum=10,
                 logOutType="terminal", logLevel="debug"):
        self.logMaxFileSize = int(logMaxFileSize)* 10*1024   #最大的日志文件个数，超过这个值，最早的日志文件自动被删除
        self.logMaxFileNum = int(logMaxFileNum) #每个日志文件的最大字节数，单位为M，超过这个大小自动新生成一个日志文件
        self.PutMode = logOutType
        self.logger = logging.getLogger()
        self.logger.setLevel(logLevel)  #设置日志级别

        self.logFileName = os.path.join(logPath, logFileName +'.log')   #日志文件路径

    def getLogger(self):
        logFormatter = logging.Formatter('%(asctime)s,%(filename)s[%(lineno)d] [%(levelname)s] %(message)s ')   #设置日志文件格式

        def Terminal():
            logStreamHandler = logging.StreamHandler()
            logStreamHandler.setFormatter(logFormatter)
            self.logger.addHandler(logStreamHandler)
            return self.logger

        def File():
            logFileHandler = handlers.RotatingFileHandler(filename=self.logFileName, maxBytes=self.logMaxFileSize,
                                     encoding='utf8', backupCount=self.logMaxFileNum)
            logFileHandler.setFormatter(logFormatter)
            self.logger.addHandler(logFileHandler)
            return self.logger

        def FileAndTerminal():
            File()
            Terminal()
            return self.logger

        """
            日志输出类型有三种值，all表示把日志输出到日志文件和屏幕上，file表示只输出到日志文件，terminal表示只输出到命令行 
        """
        choosePutMode = {
            "terminal": Terminal,
            "file": File,
            "all": FileAndTerminal,
        }

        if choosePutMode.get(self.PutMode):
            return choosePutMode.get(self.PutMode)()
