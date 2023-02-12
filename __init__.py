import configparser
class cfg_rw:
    def __init__ (self,file,encode = 'utf-8'):
        self.file = file
        self.encode = encode
        cfg_obj = configparser.ConfigParser()
        cfg_obj.read(self.file,encoding=self.encode)
        self.cfg_obj = cfg_obj
        
    def cfg_dict (self):
        cfg = {}
        for sec in self.cfg_obj.sections():
            for opt in self.cfg_obj.options(sec):
                cfg[sec] = {opt:self.cfg_obj.get(sec,opt)}
        self.cfg = cfg
        return cfg

    def read (self,section,option,type = 'str',hide_comment = False):
        # return self.cfg_obj.get
        self.value = ''
        if type == 'str':
            self.value = self.cfg_obj.get(section,option)
            if hide_comment == True:
                # raise Exception("The Hide Comment function is only available in string")
                self.value = self.value.split('#')[0]
            return self.value
        elif type == 'int':
            if hide_comment == True:
                raise Exception("The Hide Comment function is only available in string")
            return self.cfg_obj.getint(section,option)
        elif type == 'float':
            if hide_comment == True:
                raise Exception("The Hide Comment function is only available in string")
            return self.cfg_obj.getfloat(section,option)
        elif type == 'bool':
            if hide_comment == True:
                raise Exception("The Hide Comment function is only available in string")
            return self.cfg_obj.getboolean(section,option)
        else:
            raise TypeError('Unknown Type')
    def edit (self,section,option,value):
        self.cfg[section][option] = value
        self.cfg_obj.set(section,option,value)

    def save (self):
        self.cfg_obj.write(open(self.file,'w'))
    
    def del_sec (self,section):
        self.cfg_obj.remove_section(section)
    
    def del_opt (self,option):
        self.cfg_obj.remove_option(option)