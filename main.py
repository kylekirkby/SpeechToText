import urllib2, os, json, requests

#Globals
access_token_url = "https://api.att.com/oauth/token"
api_url = "https://api.att.com/oauth/token"

#Path to Wav File
wav_path = "png\\01.png"


##
##length = os.path.getsize(image_path)
##
##png_data = open(image_path, "rb")
##
##request = urllib2.Request(url, data=png_data)
##
##request.add_header('Cache-Control', 'no-cache')
##
##request.add_header('Content-Length', '%d' % length)
##
##request.add_header('Content-Type', 'image/png')
##
##res = urllib2.urlopen(request).read().strip()
##
##return res


def get_token():

   url = 'https://api.att.com/oauth/token'

   payload = {'client_id': '9bncobuoqblxoanqmm44vdxtjs4d8rs5',
              'client_secret':'g9tqrffri9ljen8ujzwijqxiw1gyzund',
              'scope':'SPEECH, TTS',
              'grant_type':'client_credentials'}

   headers = {'Content-Type': 'application/x-www-form-urlencoded',
              'Accept':'application/json'}

   r = requests.post(url, data=json.dumps(payload), headers=headers)

   res = r.read().strip()
   
   return res

def get_access_token():

   data_file = "access.txt"
   access_details = open(data_file, mode="rb")
   length = os.path.getsize(data_file)
   request = urllib2.Request(access_token_url)
   request.add_header('Accept','application/json')
   request.add_header('Content-Type','application/x-www-form-urlencoded')
   request.add_header('Accept','application/json')
   request.add_header('Content-Length', '%d' % length)
   request.post(access_token_url)
   res = urllib2.urlopen(request).read().strip()

   return res   



if __name__ == "__main__":

   token = get_token()

   print token
