import os 

class Dir:
    def __init__(self, parent = None, name = None):
        self.parent = parent
        self.subdirs = []
        self.files = []
        self.name = name
        if name and parent:
            self.path = os.path.join(self.parent.path, name)
        else:
            self.path = "/" 
        # cache for dirsize 
        self._dirsize = None
    
    def __repr__(self):
        return self.path

    def get_size(self):
        """
        Return the size of the directory, i.e. the sum of all the files 
        and directories contained in the directory. 
        """
        if self._dirsize:
            return self._dirsize
        size = 0
        for file in self.files:
            size += int(file[0])
        for dir in self.subdirs:
            size += dir.get_size()
        self._dirsize = size
        return size

    def r_get_sizes(self, sizes=[]):
        """
        Get the size of the directory and all subdirectories recursively

        Returns a list of sizes tupled with the dir path 
        """
        sizes = sizes + [(self.path, self.get_size())]
        for dir in self.subdirs:
            sizes = dir.r_get_sizes(sizes)
        return sizes

    def r_get_subdirs(self, result=[]):
        """
        Recursively get all subdirectories under this directory
        """
        for dir in self.subdirs:
            result = result + [dir]
            result = dir.r_get_subdirs(result)
        return result




with open("2022/inputs/day7.txt", "r") as f:
    line = f.readline().strip()
    assert line == '$ cd /'
    root = Dir()
    current = root
    line = f.readline().strip()
    while line:
        # Implement ls 
        if line == '$ ls':
            line = f.readline().strip()
            while line and line[0] != '$':
                tokens = line.split(' ')
                if tokens[0] == 'dir':
                    subdir = Dir(parent=current, name=tokens[1])
                    current.subdirs.append(subdir)
                else:
                    current.files.append((tokens[0], tokens[1]))
                line = f.readline().strip()
        # Implement cd
        if line.startswith('$ cd'):
            tokens = line.split(' ')
            target = tokens[-1] 
            if target == '..':
                current = current.parent
            else:
                matching = [d for d in current.subdirs if d.name == target]
                assert len(matching) == 1
                current = matching[0]

        line = f.readline().strip()

    result = 0
    sizes = root.r_get_sizes()
    for path, size in sizes:
        # print(path, size)
        if size <= 100000:
            result += size
    print("part 1")
    print(result)

    total_space = 70000000
    required_free = 30000000

    free = total_space - root.get_size()
    candidates = []
    for dir in root.r_get_subdirs():
        size = dir.get_size()
        if free + size > required_free:
            candidates.append(size)
    print("\npart 2")
    print(min(candidates))




