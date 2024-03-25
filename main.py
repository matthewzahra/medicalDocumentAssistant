def analyse(event, context):

    file = event

    source_bucket_name = file['bucket']

    blob_name = file['name']

    gcs_uri = f"gs://{source_bucket_name}/{blob_name}"

    print(gcs_uri)

 
    import vertexai
    from vertexai.generative_models import GenerativeModel, ChatSession, Image

    from google.cloud import storage

    # Set up GCS client
    storage_client = storage.Client()

    # Download image bytes from GCS
    bucket = storage_client.bucket(source_bucket_name)
    blob = bucket.blob(blob_name)
    image_bytes = blob.download_as_bytes()


    # Create Image instance from the downloaded bytes
    image = Image.from_bytes(image_bytes)

    project_id = "direct-link-417814"
    location = "us-central1"
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel("gemini-1.0-pro")
    multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    #prompt = "Describe this image to an indivdual with no medical knowledge. Summarise the important bits of information in a simple manner, and do not give any medical advice that is not stated in the image."
    #prompt = "Summarise the important information to the patient. Assume they have no medical knowledge. Make sure to capture all the medical information in a simple manner, explaining technical terms or values in simple English. English characters only in the response. Interpret the results but do not give a diagnosis that is not explicitly derived from what is provided, explaining what they mean and what their significance is."

    prompt = '''Summarise the important information to the patient.
                Assume they have no medical knowledge. 
                Make sure to capture all the medical information in a simple manner, explaining technical terms or values in simple English. 
                English characters only in the response. 
                Interpret the results, explain what they mean and what their significance is.. 
                Explain what the results mean and what their significance is. 
                English only please.'''


    contents = [image, prompt]

    responses = multimodal_model.generate_content(contents, stream=True)
    text = ""
    for response in responses:
        text += response.text
    print(text)
