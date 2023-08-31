class father:
    def f_name(self):
        print("john")
class mother:
    def m_name(self):
        print("isabella")
class son(father,mother):
    def s_name(self):
        print("david")
object=son()
object.s_name()
object.f_name()
object.m_name()
