from enum import Enum
import configparser
from collections import namedtuple


class Settings:
    CONFIG_FILE_NAME = "config.ini"

    @staticmethod
    def get_database_settings():
        section = "database"
        parameters = ['host', 'user', 'password', 'schema']
        config = configparser.ConfigParser()
        settings = namedtuple("DatabaseSettings", parameters)

        if Settings.CONFIG_FILE_NAME is None:
            raise ValueError("Config file name cannot be None")

        config.read(Settings.CONFIG_FILE_NAME)

        if section not in config.sections():
            raise ValueError(f"Section {section} not found in config file")

        for parameter in parameters:
            if config[section][parameter] is None:
                raise ValueError(f"Parameter {parameter} not found in section {section} in config file")

            setattr(settings, parameter, config[section][parameter])

        return settings
