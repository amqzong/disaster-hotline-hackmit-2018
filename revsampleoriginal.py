import requests
import json
import time

API_KEY = "Bearer 01XIo4EqB4Kzyj2UkXtgqWvatQbkCsux4xW386TloJtxL2kvwQ40T2vnWiZQtRBfcDIES9xLv35NU8tomLaysPqEy8f90"
HEADERS = {'Authorization': API_KEY}

def submit_job_url(media_url):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    payload = {'media_url': media_url,
               'metadata': "Test"}
    request = requests.post(url, headers=HEADERS, json=payload)

    if request.status_code != 200:
        raise Exception("something's wrong in submit_job_url")

    response_body = request.json()
    return response_body['id']

def submit_job_file(file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    files = { 'media': (file, open(file, 'rb'), 'audio/mp3') }
    request = requests.post(url, headers=HEADERS, files=files)
    if request.status_code != 200:
        raise Exception("something's wrong in submit_job_file")

    response_body = request.json()
    return response_body['id']

def view_job(id=59594172):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)

    if request.status_code != 200:
        raise Exception("wrong view_job")

    response_body = request.json()
    return response_body

def get_transcript(id='59594172'):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    # headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    headers['Accept'] = 'text/plain'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        raise Exception("wrong get_transcript")

    # response_body = request.json()
    response_body = request.text
    return response_body

def test_workflow_with_url(url):
    print ("Submitting job with URL")
    id = submit_job_url(url)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise Exception("something's wrong is test_workflow_with_url")

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def test_workflow_with_file(file):
    print ("Submitting job with file")
    id = submit_job_file(file)
    print ("Job created")
    view_job(id)
    print(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise Exception("something's wrong in test_workflow_with_file")

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def main():
    # Testing with URL
    #media_url = "https://www.youtube.com/watch?v=U5nl29l-zv0"
    #test_workflow_with_url(media_url)

    # Testing with file upload
    file = "hurricanecoming.mp3"
    transcript = test_workflow_with_file(file)

    textFile = open('transcript.txt','w')
    textFile.write(transcript)
    textFile.close()

if __name__ == "__main__":
    main()