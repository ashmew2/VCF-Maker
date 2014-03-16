'''
This script was actually used in a real life scenario where a large group (150+) people wanted to receive text messages. Since adding them on a phone would be a tedious job, this method was devised in order to just grab the phone numbers from an XL sheet and dump in this array. Later the VCFs were generated and could be exported with a single click on the phone and "Add to group" and BAM! 150 Messages Sent.
'''
#Array of numbers from XL Sheeet. (Changed to Hypothetical numbers)
num=[88888888, 99999999, 99999 , 912319239123, 19231293123, 12931923, 12391923]

p1='BEGIN:VCARD\nVERSION:2.1\nN:;'#fe123
p2=';;;\nFN:'#fe123
p3='\nTEL;CELL;PREF:'#950-333-4239
p4='\nEND:VCARD'

for i in range(0,len(num)):
    name='Member'+str(i)
    fp=open(name+'.vcf','w')
    fp.write(p1+name+p2+name+p3+str(num[i])+p4)
    fp.close()

#Copyright Ashish Gupta 2012. 
#Feel free to use it and extend in meaningful ways.
#In case a License is required, GPL is the one relevant to this piece of code

