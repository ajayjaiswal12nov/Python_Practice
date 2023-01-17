from collections import deque
import rpn_func
rpn_string = '32+5*'
rpn_func.rpn(rpn_string)

rpn_string = '56-3*5+'
rpn_func.rpn(rpn_string)

rpn_string = '56/3*5+'
rpn_func.rpn(rpn_string)