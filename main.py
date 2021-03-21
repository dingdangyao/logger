import configparser
from logger import Logger

def readConf(section, option):
    """
        根据传入的section获取对应的value
        :param section: ini配置文件中用[]标识的内容
        :return:
        """
    config = configparser.ConfigParser()
    configFilePath = 'logs/conf.ini'#配置文件路径
    config.read(configFilePath,encoding='utf-8')
    return config.get(section=section, option=option)

if __name__ == '__main__':

    logPath = readConf('LogParam', 'logPath')
    logFileName = readConf('LogParam', 'logFileName')
    logMaxFileNum = int(readConf('LogParam', 'logMaxFileNum'))
    logMaxFileSize = int(readConf('LogParam', 'logMaxFileSize'))
    logOutType = readConf('LogParam', 'logOutType')
    logLevel = readConf('LogParam', 'logLevel')

    logger = Logger(logPath, logFileName, logMaxFileSize, logMaxFileNum, logOutType, logLevel).getLogger()
    """
        当前日志等级有5种，logLevel = 'CRITICAL','ERROR','WARNING','INFO','DEBUG'
        五种日志等级信息的输出方式
    """
    print('*' * 25 + '数据处理分析报告' + '*' * 25)
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
