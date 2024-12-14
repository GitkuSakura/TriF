import abc,math
class Trifmeta(abc.ABC):
    @abc.abstractmethod
    def c(self,obj):
        """E"""
class ValueGetter:
    @staticmethod
    def process(s):
        if isinstance(s, str):
            start = s.index("(") + 1
            end = s.index(")")
            return s[start:end], s[:s.index("(")]
        return 0

class Des:
    __counter=0
    def __init__(self):
        cls=self.__class__
        prefix='des'
        index=cls.__counter
        self.storage_name=f'_{prefix}#{index}'
        cls.__counter+=1
    def __get__(self,instance,owner):
        value = getattr(instance, self.storage_name, None)
        if value is None:
            raise AttributeError(f"{self.storage_name} is not set.")
        return value
    def __set__(self,instance,value):
        s = value.strip()

        if len(s)==0:
            raise ValueError('plz no blank input')
        else:
            x,method = ValueGetter.process(s)

            if method=='sin':
                setattr(instance,self.storage_name,(x,Sin()))
            elif method == 'cos':
                setattr(instance, self.storage_name, (x, Cos()))
            elif method == 'tan':
                setattr(instance, self.storage_name, (x, Tan()))

class Sin(Trifmeta):
    def c(self,obj):
        try:
            return math.sin(float(obj.x))
        except TypeError:
            raise ValueError(r"X can't be NaN")
class Cos(Trifmeta):
    def c(self, obj):
        try:
            return math.cos(float(obj.x))
        except TypeError:
            raise ValueError(r"X can't be NaN")

class Tan(Trifmeta):
    def c(self, obj):
        try:
            return math.tan(float(obj.x))
        except TypeError:
            raise ValueError(r"X can't be NaN")

class Trif:
    des = Des()
    ds = 2
    def __init__(self, des_input):
        # print(f"Debug: des_input={type(des_input)}")
        self.des = des_input
        self.x, self.method = self.des
        self.value = self.method.c(self)

        self.value=self.method.c(self)
    def __repr__(self):
        fmt=f"<result:{{:.{Trif.ds}f}}>"
        return fmt.format(self.value)
    def __add__(self,obj):return self.value+obj.value if isinstance(obj,Trif) else self.value+obj
    def __sub__(self,obj):return self.value - obj.value if isinstance(obj,Trif) else self.value-obj
    def __mul__(self,obj):return self.value * obj.value if isinstance(obj,Trif) else self.value*obj
    def __truediv__(self,obj):return self.value * obj.value if isinstance(obj,Trif) else self.value/obj




# t = Trif
# print(t('sin(30)'))

