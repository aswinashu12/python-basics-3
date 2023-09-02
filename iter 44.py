class num:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
my_num=num()
m_iter=iter(my_num)
for y in m_iter:
    print(y)

