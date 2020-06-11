# 导包
import os
import unittest

import HTMLTestRunner_PY3
from HTMLTestRunner_PY3 import HTMLTestRunner
from script.tpshop_test_parameterized import TpshopTest
import time
# 实例化测试套件
suite = unittest.TestSuite()
# 添加测试用例
suite.addTest(unittest.makeSuite(TpshopTest))
# 设置测试报告的路径和名称
report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm人力资源管理",
                                               description="测试登陆接口和员工管理模块")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)