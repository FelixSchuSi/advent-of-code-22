from typing import Dict


lines = open("07/input", "r").read().splitlines()


def parse_line(tree: Dict, cwd: str, line: str):
    if line.startswith("$") and "ls" in line:
        return tree, cwd
    if line.startswith("$") and "cd" in line:
        _, _, path = line.split()
        if path == "/":
            cwd = "/"
        elif path == "..":
            cwd = "/".join(cwd.split("/")[:-1])
        else:
            cwd = f"{cwd}/{path}" if cwd != "/" else f"/{path}"
    if line[0].isnumeric():
        size, filename = line.split(" ")
        tree[f"{cwd}/{filename}" if cwd != "/" else f"/{filename}"] = size
    return tree, cwd


def calc_dir_size(tree: Dict) -> Dict:
    dir_tree = {}

    def add_item_to_dir_tree(dir_tree: Dict, dir_path: str, size: str):
        if dir_path in dir_tree:
            dir_tree[dir_path] = dir_tree[dir_path] + int(size)
        else:
            dir_tree[dir_path] = int(size)
        return dir_tree

    for path, size in tree.items():
        dir_path = "/".join(path.split("/")[:-1])
        dir_path = "/" if dir_path == "" else dir_path
        dir_tree = add_item_to_dir_tree(dir_tree, dir_path, size)
        sub_dir_path = dir_path
        while True:
            if len(path.split("/")) <= 2:
                break
            sub_dir_path = "/".join(sub_dir_path.split("/")[:-1])
            sub_dir_path = "/" if sub_dir_path == "" else sub_dir_path
            dir_tree = add_item_to_dir_tree(dir_tree, sub_dir_path, size)
            if sub_dir_path == "/":
                break

    return dir_tree


TOTAL_DISK_SIZE = 70000000
REQUIRED_REMAINING_DISK_SIZE = 30000000

tree = {}
cwd = "/"

for line in lines:
    tree, cwd = parse_line(tree, cwd, line)

dir_tree = calc_dir_size(tree)
actual_remaining_disk_size = TOTAL_DISK_SIZE - dir_tree["/"]
disk_size_missing = REQUIRED_REMAINING_DISK_SIZE - actual_remaining_disk_size

print(
    sorted(
        [num for num in dir_tree.items() if num[1] >= disk_size_missing],
        key=lambda x: x[1],
    )
)
