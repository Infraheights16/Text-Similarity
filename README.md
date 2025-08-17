# Semantic Textual Similarity between two texts
This API will take two texts as input and give the degree to which two sentences are 
semantically equivalent to each other.

1 means highly similar 

0 means highly dissimilar

Request body: {“text1”: ”nuclear body seeks new tech .......”, ”text2”: ”terror suspects face arrest ......”} 
Response body: {“similarity score”: 0.2 }

A brief description about the project: 

• Used distil Roberta model from sentence transformers to create the embeddings of textual 
data.

• This model is very suitable for semantic analysis

• After getting the embeddings we can apply cosine similarity to check the similarity between 
two pairs of text vectors.

Some examples of how this API works : 


![Screenshot 2024-04-17 231827](https://github.com/saneh12/dataNeuronTask/assets/142069452/ade3ae8e-350f-43fd-9f6a-40c4363a70ca)

![Screenshot 2024-04-17 231901](https://github.com/saneh12/dataNeuronTask/assets/142069452/68a260a2-be7b-4303-aed2-70743ed4e624)

