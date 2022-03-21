class PPT_slide:
    def __init__(self, par_section, title = None) -> None:
        '''
        初始化PPT_slide
        :param section: 所属的章节
        :param title: 页标题
        '''
        self.par_section = par_section
        self.title = title
        self.texts = []

    def add_text(self, text):
        '''
        添加文字信息
        :param text: 待添加文字信息
        '''
        self.texts.append(text)


class PPT_section:
    def __init__(self, title) -> None:
        '''
        初始化PPT_section
        :param title: 章节标题
        '''
        self.title = title

        self.slides = []
        self.now_slide = None
    
    def next_slide(self, title = None) -> PPT_slide:
        '''
        进入下一页
        :param title: 下一页标题
        '''
        self.now_slide = PPT_slide(self, title)
        self.slides.append(self.now_slide)
        return self.now_slide
    

class M_PPT:
    def __init__(self, title='默认标题', sub_title='', template='normal') -> None:
        '''
        初始化 class M_PPT
        :param title: PPT标题
        :param sub_title: PPT副标题
        :param template: PPT模板
        '''
        self.title = title
        self.template = template
        self.sub_title = sub_title

        self.sections = []
        self.now_section = None
    
    def set_title(self, title):
        '''
        设置标题
        :param title: 标题
        '''
        self.title = title
    
    def set_sub_title(self, sub_title):
        '''
        设置副标题
        :param sub_title: 副标题
        '''
        self.sub_title = sub_title

    def next_section(self, title):
        '''
        进入下一章节
        :param sub_title: 章节标题
        '''
        self.now_section = PPT_section(title)
        self.sections.append(self.now_section)
        return self.now_section



