# 导出到 csv 文件，
# 用excel 可打开，
# 但需将原文件以编码为 ANSI 另存。

s = '{0},{1},{2},{3},{4}'.format('one', 'two', 'three', 'four', 'five')
# 每项间加逗号，可以实现放在两个单元格，否则在同一个单元格里
with open('csvv.csv', 'w', encoding='utf-8') as f:
	f.write(s)
