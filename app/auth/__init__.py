# -*- coding: utf-8 -*-
from flask import Blueprint

auth = Blueprint('auth', __name__)  # 创建认证蓝本，此蓝本中定义用户认证系统相关的路由

from . import views