# -*- encoding=UTF-8 -*-

def demo_string():
    stra = 'hello world'
    strb = '1 2 \n\rhello nowcoder\r\n'
    print stra.capitalize()
    print strb
    print strb.lstrip()
    print strb.startswith('hel')
    print strb.find('hel')


if __name__ == '__main__':
    demo_string()