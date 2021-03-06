
# coding: utf-8

# In[7]:


from flask import Flask, request
from flask import make_response
import requests
import os
import json

app = Flask(__name__)

@app.route('/connect')
def cf_connect():
    query = request.args.get('query')
    api_url = 'https://api.api.ai/v1/query?v=20150910&query='
    head = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    s = requests.Session()
    result = s.get(api_url + query + '&lang=en'+ '&sessionId=1234567890', headers=head)
    result = result.json()
    result = result.get('result')
    fulfil = result.get('fulfillment')
    data= fulfil.get('data')
    if data is None:
        speech= fulfil.get('speech')
        fb={"text": speech}
    else:    
        fb = data.get('facebook')
    element=[]
    element.append(fb)
    res = json.dumps(element, indent=4)
    r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')

