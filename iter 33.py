class num:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        x=self.a
        self.a+=1
        return x
my_num=num()
m_iter=iter(my_num)
print(next(m_iter))
print(next(m_iter))
print(next(m_iter))
print(next(m_iter))
print(next(m_iter))