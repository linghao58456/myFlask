"""
@author: hao.ling
@Date: 2020/7/24 10:48 下午
@Annotation: 服务运行主程序
"""
from config.server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9990, debug="debug")
