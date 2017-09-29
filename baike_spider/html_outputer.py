#coding:utf8

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def _write_td(self, fout, title):
        if title is not None:
            fout.write('<td>')
            fout.write(title)
            fout.write('</td>')

    def output_html(self):
        fout = open('output.html', 'w')
        fout.write('<html>')
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        fout.write('<body>')
        fout.write('<table border=0.5>')

        #ascii
        for data in self.datas:
            fout.write('<tr>')
            if 'url' in data:
                self._write_td(fout, data['url'])
            if 'title' in data:
                self._write_td(fout, data['title'])
            if 'summary' in data:
                self._write_td(fout, data['summary'])
            fout.write('</tr>')
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()