from managedfile import ManagedFile
from indenter import Indenter

#with ManagedFile('testfile.txt') as mf:
#    pass

with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('Hello')
        with indent:
            indent.print('bonjour')
        indent.print('hey')
    