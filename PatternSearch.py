import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#This statement to find the count the non alphanumeric characters
#in the string assigned to 'lorem_ipsum'
#set the pattern in the string
results = re.findall("[^a-zA-Z0-9]", lorem_ipsum)
print(len(results)) #output results
#This function check the string contains the 'sit-amet' or 'sit:amet'
#characters in the string assigned to 'lorem_ipsum'
#set the pattern in the string
occurences_sit_amet = re.findall(r"sit[-:]amet", lorem_ipsum)
print(len(occurences_sit_amet)) #print the length of the characters using len() function
#Replace sit:amet and sit-amet with sit amet using the sub function
#Store the output to a variable named 'replace_results'
replace_results = re.sub(r"sit[-:]amet", "sit amet", lorem_ipsum)
#find the pattern in the string
#Store the output to a variable named 'occurrance_sit_amet'
occurences_sit_amet = re.findall("sit amet", replace_results)
print(len(occurences_sit_amet))
#print the lenth of the characters using len() function