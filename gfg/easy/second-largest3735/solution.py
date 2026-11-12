class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest= -1
        secondlargest= -1 
        
        for i in arr:
          if i>largest:
              secondlargest=largest
              largest=i
              
          elif (i>secondlargest and i!=largest):
              secondlargest= i
               
        return(secondlargest) 
              
         
      
          
        
        