"""
Module for getting value of certain parameter in certain section in cfg. file
"""
import ConfigParser


def get_setting(cfg_file, section,  parameter):
    """
    cfg_file - name or path and name of cfg file for parsing
    section - name of section of parameter
    parameter - name of parameter of value has to be received
    """
    config = ConfigParser.ConfigParser()
    config.read(cfg_file)
    return config.get(section, parameter)
