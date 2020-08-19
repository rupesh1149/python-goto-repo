# opening the files
stream = open(file_name,mode,buffer_size)
stream.readable() #can we read?
stream.readline() #Read the line
stream.close() #closes the line
stream.write('H') #writes a single string
stream.writelines(['ello',' ','world']) #write multiple strings
stream.write('\n') #write a new lines
stream.close() #close the stream and flush data

# Cleaning with with 
# always use 
with open('output.txt', 'wt') as stream:
    stream.write('LOreum ipsum')
# Or
try:
    stream = open('output.txt', 'wt')
    stream.write('lorem ipsum')
finally:
    stream.close()
