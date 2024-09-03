import sys
import logging
import logger

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error_message = "Error Occured in Python Script Name [{0}] Line Number [{1}] Error Message [{2}]".format(
        file_name, lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message
    