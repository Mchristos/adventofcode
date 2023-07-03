

def parse(s):
    if s[0] == '[':
        openstack = 1
        s_ = list(s[1:])
        list = []
        while openstack > 0:
            next = s_.pop(0)
            try:
                val = int(next)
            except:
                pass
            
            list.append(val)
    





with open('2022/inputs/day13_.txt','r') as f:
    pairs = f.read().split('\n\n')
    for pair in pairs:
        left, right = [x[1:-1] for x in pair.split('\n')]
        print(left, right)