# # def funkcja(**kwargs):
# #     for k in kwargs:
# #         print(k,kwargs[k])
# #
# # funkcja(wymyslony_argument1="wartość wymyślonego argumentu",x=10,lista=[1,2,3,4])
#
import time

def mierzczas(fun):
    def wewnetrzna(*args,**kwargs):
        start=time.time()
        fun(*args,**kwargs)
        koniec=time.time()
        print(f'funkcja {fun.__name__} trwała {koniec-start} sekund')
    return wewnetrzna


@mierzczas
def funkcja1():
    time.sleep(3)
    print('tu funkcja 1')

@mierzczas
def funkcja2(x):
    time.sleep(2)
    print(f'tu funkcja 2 x={x}')

@mierzczas
def funkcja3(x,y):
    time.sleep(2)
    print(f'tu funkcja 3 x={x}, y={y}')

@mierzczas
def funkcja4():
    return 'koza'

funkcja1()
funkcja2(3)
funkcja3(1,2)
# x=funkcja4()
# print(x)


# @mierzczas
# def czekacz(x):
#     print('czekacz...')
#     time.sleep(x)

# fun=mierzczas(czekacz)
# fun(2)

# @mierzczas
# def funkcja1():
#     time.sleep(3)
#     print('tu funkcja 1')
#
# @mierzczas
# def funkcja2(x):
#     time.sleep(2)
#     print(f'tu funkcja 2 x={x}')
#
# @mierzczas
# def funkcja3(x,y):
#     time.sleep(2)
#     print(f'tu funkcja 3 x={x}, y={y}')
#
# funkcja1()
# # funkcja2(10)
# # funkcja3(10,20)
#

# def siemator():
#     print('siema!')
#
# def odpal(fun):
#     fun()
#
# odpal(siemator)

# def opakowujaca():
#     def wewnetrzna():
#         print('wewnetrzna')
#     wewnetrzna()
#
# opakowujaca()
#
# def opakowujaca():
#     def wewnetrzna():
#         print('wewnetrzna')
#     return wewnetrzna
#
# fun=opakowujaca()
# fun()
#
# def funkcja(*args):
#     for a in args:
#         print(a)
#
# funkcja(1,2,3,'dupa')