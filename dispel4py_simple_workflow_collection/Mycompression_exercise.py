
# coding: utf-8

# # Compress random strings

# Let's do now a simple exercise that wraps the basic knowledges that we have learnt today:
#     * Create ProducerPE, IterativePE, ConsumerPE PEs. 
#     * Give input parameters to a PE
#     * Produce 1 output stream 
#     * Produce more than one ouptut stream
#     * Create a Graph
#     * Connect PEs
#     * Run a Graph
# 
# For the next exercise, you will have to:
#     * Create a PE that generates random string which the lengh specified by a parameter.
#     * Create a PE that compresses the string by using zlib compression algorithm and produces an output stream that returns a tuple (compress_zlib and original_string ) 
#         ** zlib.compress(original_string)
#         ** self.write("output", [original_string, compress_string])
#     * Create a PE that decompresses the compressed_string and checks that it is equal to the original string.  
#         ** zlib.decompress(compress_string)
#     * Create a graph that connect the three PEs created
#     * Run the graph:
#         ** from dispel4py.new.simple_process import process as simple_process
#         ** simple_process(graph, {producer: 1})
# 

# The id_generate() function generates a random string. You could used it later in the first PE. 

# In[ ]:

import random
import string
import zlib
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# In[117]:

#from dispel4py.base import ProducerPE

#class StringProducer(ProducerPE):
#    def __init__(self, length):
       
        
#    def _process(self):

     #...
     #return random_string
     


# In[ ]:

#from dispel4py.base import IterativePE

#class ZlibCompression(IterativePE):

#    def __init__(self):
#        IterativePE.__init__(self)
     
#    def process(self, data):
         #original_string=data['input']
         # ....
         
       
    
       
        


# In[ ]:

#from dispel4py.base import ConsumerPE

#class ZlibDeCompression(ConsumerPE):

#    def __init__(self):
       

#    def process(self, data):
        #original_string=data["input"][0]
        #....
     
     
       
        
       


# In[ ]:

#from dispel4py.workflow_graph import WorkflowGraph
#create PEs



#create graph
#graph = WorkflowGraph()
#connect the PEs in the graph 






# Execute the workflow
# 
# To run this workflow you can use the sequential simple processor in the ipython notebook:
# 

# In[ ]:

from dispel4py.new.simple_process import process as simple_process
simple_process(graph, {producer: 1})


# if your run the exercise as an script comment the previous line, and write this one in your command line:
#     dispel4py simple Mycompression_example.py 
