import sys
import logging
from logging import getLogger

from umodbus.utils import (log_to_stream, unpack_mbap, pack_mbap,
                           pack_exception_pdu,
                           get_function_code_from_request_pdu)


def test_log_to_stream():
    """ Test if handler is added correctly. """
    log = getLogger('uModbus')

    # NullHandler is attached.
    assert len(log.handlers) == 1
    log_to_stream()
    assert len(log.handlers) == 2

    handler = log.handlers[1]
    assert handler.stream == sys.stderr
    assert handler.level == logging.NOTSET


def test_unpack_mbap():
    """ MBAP should contain correct values for Transaction identifier, Protocol
    identifier, Length and Unit identifer.
    """
    assert unpack_mbap(b'\x00\x08\x00\x00\x00\x06\x01') == (8, 0, 6, 1)


def test_pack_mbap():
    """ Byte array should contain correct encoding of Transaction identifier,
    Protocol identifier, Length and Unit identifier.
    """
    assert pack_mbap(8, 0, 6, 1) == b'\x00\x08\x00\x00\x00\x06\x01'


def test_pack_exception_pdu():
    """ Exception PDU should correct encoding of error code and function code.
    """
    assert pack_exception_pdu(1, 1) == b'\x81\x01'


def test_get_function_code_from_request_pdu():
    """ Get correct function code from PDU. """
    assert get_function_code_from_request_pdu(b'\x01\x00d\x00\x03') == 1
