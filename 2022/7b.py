from bisect import bisect_left

DEBUG = False

command = input()
output = []

availableSpace = 70000000

usedSpace = 0
targetSpace = 30000000


class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def __repr__(self):
    return f'({self.size})'


class Folder:
  def __init__(self, name, folders, files, parent=None):
    self.name = name
    self.folders = folders
    self.files = files
    self.parent = parent

  def __repr__(self):
    return f'{self.folders}, files: {self.files}'

  def addNestedFolder(self, name):
    if name not in self.folders:
      self.folders[name] = Folder(name, {}, {}, self)

    return self.folders[name]

  def addFile(self, name, size):
    if name not in self.files:
      self.files[name] = File(name, size)

    return self.files[name]


currentFolder = Folder('/', {}, {})
startingFolder = currentFolder


def indexFiles(outputLines):
  for line in outputLines:
    sizeOrDir, name = line.split()

    if sizeOrDir == 'dir':
      currentFolder.addNestedFolder(name)
    else:
      currentFolder.addFile(name, int(sizeOrDir))


def processCommand(rawInput, outputLines):
  global currentFolder

  tokens = rawInput.split()
  assert tokens.pop(0) == '$'

  command = tokens.pop(0)

  if command == 'ls':
    indexFiles(outputLines)
  elif command == 'cd':
    path = tokens.pop(0)

    if path == '..':
      currentFolder = currentFolder.parent
    elif path == '/':
      currentFolder = startingFolder
    else:
      currentFolder = currentFolder.addNestedFolder(path)


# Read command
while True:
  try:
    nextLine = input()

    if nextLine.startswith('$'):
      processCommand(command, output)
      command = nextLine
      output = []
    else:
      output.append(nextLine)

  except EOFError:
    processCommand(command, output)
    break

# Scan folders saving all sizes
folderSizes = []

def calcFolderSize(folder, depth=0):
  folders = folder.folders.values()
  files = folder.files.values()

  if DEBUG:
    print('  ' * depth + f'- {folder.name}')
    for file in files:
      print('  ' * (depth + 1) + f'- {file.name} ({file.size})')

  fileSize = sum(file.size for file in files)
  folderSize = sum(calcFolderSize(nested, depth + 1) for nested in folders)
  totalSize = fileSize + folderSize

  folderSizes.append(totalSize)

  return totalSize


usedSpace = calcFolderSize(startingFolder)
freeSpace = availableSpace - usedSpace
remaining = targetSpace - freeSpace

# Binary search to find first element at least as big as the
# size that needs to be freed
folderSizes.sort()
bestCandidate = bisect_left(folderSizes, remaining)

print(folderSizes[bestCandidate])
