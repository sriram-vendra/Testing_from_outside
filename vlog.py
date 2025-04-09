import logging,os,datetime
#import indexsri
import logging as log
import logging.config
import yaml
import configparser
class Logs:
    def logg(value):
        """# Gets or creates a logger
        with indexsri.app.test_request_context('/', method='POST'):
           log_path=indexsri.app.config['log_path']
            log_name=indexsri.app.config['log_name']
            #if os.stat(log_path+log_name).st_size/(1024*1024) >3:
             #   oldname=(log_path+log_name).replace("\\\","\\")
              #  newname=(log_path+log_name+str(datetime.datetime.now())).replace('\\\','\\')
               # os.rename(oldname,newname)

        global logger
        logger= logging.getLogger(__name__)
        # set log level
        logger.setLevel(logging.CRITICAL)
        # define file handler and set formatter
        #file_handler = logging.FileHandler('C:\\inetpub\\wwwroot\\testing_iis\\logfile.log')
        file_handler = logging.FileHandler(log_path+log_name)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s  :%(levelno)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        # add file handler to logger
        logger.addHandler(file_handler)
        for i in value:
            exec('logger.'+i)"""
        return 'Logged successfull'
    
    def loggers():
        config=configparser.ConfigParser()
        config.read("C:\\inetpub\\wwwroot\\testing_iis\\settings\\settings.ini")
        with open(config["D_Logger"]["LogYAMLFullPath"],'rt') as filelog:
            yamlconfig=yaml.safe_load(filelog.read())
        log.config.dictConfig(yamlconfig)
        logger=log.getLogger('Developement')
        if not config['D_Logger']['DebugLoggerLevel'].lower():
            log.disable(level=log.DEBUG)
        else:
            pass
        return logger
