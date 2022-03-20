class PPT_slide:
    def __init__(self, section, title = None) -> None:
        '''
        初始化PPT_slide
        :param section: 所属的section
        :param title: 页面标题
        '''
        self.section = section
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
        self.title = title

        self.slides = []
        self.now_slide = None
    
    def next_slide(self, title = None) -> PPT_slide:
        self.now_slide = PPT_slide(self, title)
        self.slides.append(self.now_slide)
        return self.now_slide
    

class M_PPT:
    def __init__(self, title='默认标题', sub_title='', template='normal') -> None:
        self.title = title
        self.template = template
        self.sub_title = sub_title

        self.sections = []
        self.now_section = None
    
    def set_title(self, title):
        self.title = title
    
    def set_sub_title(self, sub_title):
        self.sub_title = sub_title

    def next_section(self, title):
        self.now_section = PPT_section(title)
        self.sections.append(self.now_section)
        return self.now_section



