from controllers.c_reader import C_reader
from controllers.c_painter import C_painter


reader = C_reader('./examples/WinkPPT.md')  # 创建markdown文件阅读器，输入markdown文件
ppt_data = reader.compile()  # 阅读器编译markdown文件，生成m_PPT数据
painter = C_painter(ppt_data)  # 创建绘制器，输入m_PPT数据
painter.save('./examples/WinkPPT.pptx')  # 绘制器绘制PPT并输出到指定路径