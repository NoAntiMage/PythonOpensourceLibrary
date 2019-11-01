import filecmp

filecmp.cmp('/home/test/filecmp/f1', '/home/test/filecmp/f2')

a = '/home/test/filecmp/dir1'
b = '/home/test/filecmp/dir2'
dirobj = filecmp.dircmp(a, b)

dirobj.report()