# medicalDocumentAssistant
Work done at Go Reply internship March 2024

This is a proof of concept for a jargon buster and was presented to the rest of the team.

The idea is that when presented with a medical document, it explains its significance/meaning in simple terms WITHOUT making a diagnosis.

This was completed on the Google Cloud Platform (GCP).

First created a bucket (with Google Cloud Storage) where the medical documents (in the form of .jpg files) were to be deposited for analysis. 

The created a Google Cloud Function which contained main.py and requirements.txt. It exectured main.py on a storage event (so wehn the above bucket had a new item added to it).

requirements.txt specified what to import.

# Logic for main.py
gcs_uri was the url (location) of the image to be analysed. 
Note, the event is an object corresponding to the image that has just been added to the bucket.

Use vertexai to query the LLM  (here used a version of Gemini specialised in looking at images).

Since the image is stored at a known url, rather than a known file location, I download the image as a series of bytes, and then reconstruct the iamge to pass into the LLM.

I initilaise the model and then pass the image and the prompt to it - the use of "English" many times is due to the model's tendancy to respond in Chinese for some unknown reason.

The print statements (output here) execute into the logs on GCP of the function.
