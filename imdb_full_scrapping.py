
# coding: utf-8

# In[ ]:

# creating a proper web scrapper from scrach 
# after importing statements we will have 

# we will break into two process , first we will set for only class

soupari = soup.find('div' , {'class' : 'name of the class'})

title = soupari.find('div').a.text
links = soupari.find('div').div(find_all('div')[0]).text

## in times of confusion always print the output you will get the pattern.


# In[ ]:

# finaaly we will loop through it 

soupari = soup.find('div' , {'class' : 'name of class'})
for i in soupari:
#just replace every soup.find with i and you good to go .
    title = i.find('div').a.text
    links = i..div(find_all('div')[0]).text
    
    print(soupari)
    print(links)
    
    

