import logging

from custom_mmpkg.custom_mmcv.utils import get_logger


def get_root_logger(log_file=None, log_level=logging.INFO):
    return get_logger('mogen', log_file, log_level)