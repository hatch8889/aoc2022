import enum
import typing


class Type(enum.Enum):
    DIRECTORY = 1,
    FILE = 2,


TFileDescriptor = typing.TypeVar("TFileDescriptor", bound="FileDescriptor")


class FileDescriptor(object):
    type: Type
    size: int = 0
    name: str
    contents: typing.List[TFileDescriptor]
    parent: TFileDescriptor = None

    def __init__(self, type: Type, name: str, size: typing.Optional[int] = 0, parent: typing.Optional[TFileDescriptor] = None):
        self.type = type
        self.name = name
        self.size = size or 0
        self.parent = parent
        self.contents = []

    def __str__(self):
        if self.parent:
            return self.parent + self.name
        return self.name + '/' if self.type == Type.DIRECTORY else ''

    def add_content(self, line: str):
        parts = line.split()
        if parts[0] == 'dir':
            new_file = FileDescriptor(type=Type.DIRECTORY, name=parts[1], parent=self)
        else:
            new_file = FileDescriptor(type=Type.FILE, name=parts[1], size=int(parts[0]), parent=self)
        self.contents.append(new_file)

    def get_by_name(self, name: str):
        for c in self.contents:
            if c.name == name:
                return c

    def get_size_sum(self) -> int:
        size_sum = 0
        for c in self.contents:
            if c.type == Type.DIRECTORY:
                size_sum += c.get_size_sum()
            else:
                size_sum += c.size
        return size_sum

    def get_all_directories(self) -> typing.List[TFileDescriptor]:
        dir_list = []
        for c in self.contents:
            if c.type == Type.DIRECTORY:
                dir_list.append(c)
                for j in c.get_all_directories():
                    dir_list.append(j)
        return dir_list


root = FileDescriptor(type=Type.DIRECTORY, name='')
currentDirectory = root


def change_directory(line: str):
    global currentDirectory
    parts = line.split()
    if parts[2] == '/':
        currentDirectory = root
        return

    if parts[2] == '..':
        currentDirectory = currentDirectory.parent
        return

    currentDirectory = currentDirectory.get_by_name(parts[2])


def part1():
    all_dirs = root.get_all_directories()
    sum_of_dirs = 0
    for d in all_dirs:
        full_size = d.get_size_sum()
        if full_size < 100000:
            sum_of_dirs += full_size
    print(sum_of_dirs)


def part2():
    print('part2: ')
    total_disk_size = 70000000
    used_disk_size = root.get_size_sum()
    free_space = total_disk_size - used_disk_size
    additional_free_space_required = 30000000 - free_space

    all_dirs = root.get_all_directories()
    dir_lengths = []
    for d in all_dirs:
        full_size = d.get_size_sum()
        if full_size > additional_free_space_required:
            dir_lengths.append(full_size)

    print(sorted(dir_lengths)[0])


def main():
    with open('day7.txt') as data:
        lines = data.read().splitlines()
        for line in lines:
            if line.startswith('$ cd'):
                change_directory(line)
            elif line.startswith('$ ls'):
                pass
            else:
                currentDirectory.add_content(line)

    part1()
    part2()


if __name__ == '__main__':
    main()
