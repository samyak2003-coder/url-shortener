from flask import Flask, request, jsonify, redirect
import redis
import hashlib

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

BASE_URL = "http://localhost:5000/"

def generate_short_url(long_url):
    hash_object = hashlib.md5(long_url.encode())
    return hash_object.hexdigest()[:6]  

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("long_url")
    
    if not long_url:
        return jsonify({"error": "Missing URL"}), 400
    
    short_url = generate_short_url(long_url)
    redis_client.set(short_url, long_url)
    
    return jsonify({"short_url": BASE_URL + short_url})

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
    long_url = redis_client.get(short_url)
    
    if long_url:
        return redirect(long_url)
    
    return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
