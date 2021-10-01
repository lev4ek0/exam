from math import log

array = ['access article denver dept lines matthew mz nyx organization public unix zenkar',
'article bbs caronni caronni germano provider public question writes',
'bombarded gop home house mount news outlets pressure public seeking senator senators start white wsj',
'auction corvallis cs dept dragon final lines magazine oregon oregon organization public state university update',
'access files found look new public system',
'another cars cars experiences info people public recently requested responses seen user',
'archie c code cryptography distributable freely key know public rsa searches tried various',
'article astronomy datadec domain kevin map marcus programs public shareware writes',
'basics cryptography cryptography faq key part public rsa summary',
'ask asked bernstein bits chip clipper dan exchange key keys public question wanting',
'anybody appreciate around bitmap color editor find folks hi information know public sites',
'allocate anyone appreciate based colormaps correct domain example know need program program public shading xlib',
'brigham domain kun looking organization provo public qiao qiaok university usa ut viewer young',
'april events house immediate march office president press public release schedule secretary thursday white',
'anyone currently domain knows mac netland pov povray public skip step using utilities wondering',
'allocated building building costing create geared infrastructure infrastructure jobs kol money palestinians public reports territories works yisrael',
'anyone domain favorite light list lists maintaining msdos public really several shareware software stuff windows windows',
'commit honor humanity japanese like offenses officials public salvage tatters tradition truly unfortunate',
'access ado article buz denver dept lines nyx organization owen public unix',
'administration encryption encryption illegal key made public question safety saying since threatens whether']


def count(w1, w2):
    count = 0
    for i in array:
        if w1 in i and w2 in i:
            count += 1
    return count


def count1(w):
    count = 0
    for i in array:
        if w in i:
            count += 1
    return count


w0 = 'public'
w1 = 'access'
ppmi = max(log(len(array) * count(w0, w1) / count1(w0) / count1(w1), 2), 0)
print(ppmi)
