import re

from models.m_PPT import M_PPT

class C_reader:
    def __init__(self, file_path):
        '''
        初始化C_reader
        :param file_path: 待阅读文件的路径
        '''
        self.file_path = file_path
        self.__ppt_data = M_PPT()

    def compile(self) -> M_PPT:
        '''
        编译markdown文件
        :return: 编译结果
        '''
        mode = 1 # 1:开头部分 2:内容部分
        # 遍历文件行，逐行编译
        for line in open(self.file_path, 'r', encoding='utf8'):
            # 若为空行，跳过
            if re.match('\S', line) == None:
                continue
            # 编译开头部分
            elif mode == 1:
                if(not self.__compile_head(line)):
                    mode = 2
                    self.__compile_body(line)
            # 编译内容部分
            elif mode == 2:
                self.__compile_body(line)
        # 返回ppt_data
        return self.__ppt_data
    
    def __compile_head(self, line) -> bool:
        '''
        编译开头部分
        :param line: 待编译的内容
        :return: 是否可识别
        '''
        ppt_data = self.__ppt_data
        match_title = re.match(r'# (.*)', line)
        if match_title != None:
            ppt_data.set_title(match_title[1])
            return True
        match_sub_title = re.match(r'\* (.*)', line)
        if match_sub_title != None:
            sub_title =  match_sub_title[1] if ppt_data.sub_title == '' else ppt_data.sub_title + '\t' + match_sub_title[1]
            ppt_data.set_sub_title(sub_title)
            return True
        return False
    
    def __compile_body(self, line):
        '''
        编译主体部分
        :param line: 待编译的内容
        '''
        ppt_data = self.__ppt_data

        match_title = re.match(r'## (.*)', line)
        if match_title != None:
            ppt_data.next_section(match_title[1])

        match_title = re.match(r'### (.*)', line)
        if match_title != None:
            ppt_data.now_section.next_slide(match_title[1])

        match_text = re.match(r'\* (.*)', line)
        if match_text != None:
            ppt_data.now_section.now_slide.add_text(match_text[1])
