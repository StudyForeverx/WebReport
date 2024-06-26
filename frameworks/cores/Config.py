import configparser
import os
import socket
import platform

class Config:
    conf = ""

    def __init__(self):
        sys_platform = platform.platform().lower()
        print(sys_platform)
        if "windows" in sys_platform:
            cfgpath = "D:\\WebReport\\configs\\machine.ini"
        else:
            cfgpath = "/root/python/code/config/userserver_config.ini"

        # 创建管理对象
        self.conf = configparser.ConfigParser()

        # 读ini文件
        self.conf.read(cfgpath, encoding="utf-8")  # python3

    def getDB(self):
        return [self.conf.get("userserver", "host"),
                self.conf.get("userserver", "user"),
                self.conf.get("userserver", "pass"),
                self.conf.getint("userserver", "port"),
                self.conf.get("userserver", "dbname")
                ]

    def getOcsOnline(self):
        return [self.conf.get("ocs_online","host"),
                self.conf.get("ocs_online","user"),
                self.conf.get("ocs_online","pass"),
                self.conf.getint("ocs_online","port"),
                self.conf.get("ocs_online","dbname")
                ]