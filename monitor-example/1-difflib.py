import difflib

text1 = '''hello world.
how is your mother?'''

text1_line = text1.splitlines()

text2 = '''hi world!
how is your father?'''

text2_line = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_line, text2_line)
# print(diff)
# print(list(diff))
print '\n'.join(list(diff))


d1 = difflib.HtmlDiff()
print d1.make_file(text1_line, text2_line)
