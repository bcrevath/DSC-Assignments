#!/usr/bin/env python
# coding: utf-8

# In[9]:


#assignment 1
mov = str(input("Enter movie name:"))
Mov = mov.lower()
if Mov in ["dark","mindhunter","parasite","inception","insidious","interstellar","prison Break","money heist","war","jack ryan"]:
    print("It is a Thriller" )
elif Mov in ["friends","3 idiots","brooklyn 99","how i met your mother","rick and morty","the big bang theory","the office","space force"]:
    print("It is a Comedy")
else:
    print("It is neither Comedy not Thriller")


# In[10]:


def gloves(arr, n) :  
  
    count = 0;  
  
   
    arr.sort(); 
    i = 0; 
    while i < (n-1) :  
  
        
        if (arr[i] == arr[i + 1]) : 
            count += 1;  
  
            i = i + 2;  
  
     
        else : 
            i += 1;  
  
    return count;  
  

if __name__ == "__main__" :  

    arr = []
N = int(input("Enter number of elements : ")) 
  
arr = list(map(int,input("\nEnter all the Colour Codes corresponding to Gloves : ").strip().split()))[:N] 
  

n = len(arr);  
print(gloves(arr, n),"pairs of gloves found")


# In[ ]:




