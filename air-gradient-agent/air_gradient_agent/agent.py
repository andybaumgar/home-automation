from http.server import BaseHTTPRequestHandler, HTTPServer
from influxdb import InfluxDBClient
from datetime import datetime
import json

influx_client = InfluxDBClient('192.168.0.153', 8086, 'admin', 'admin', 'apartment')

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

class MyServer(BaseHTTPRequestHandler):

    def create_influx_post(self, measurements):
        json_body = []
        current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
        measurements['temp_fahrenheit'] = celsius_to_fahrenheit(measurements['atmp']) 

        for key, value in measurements.items():
            json_part = {
                "measurement": key,
                "time": current_time,
                "fields": {
                    "value": value
                }
            }
    
            json_body.append(json_part)
    
        return json_body
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        print(data)
        
        post = self.create_influx_post(data)
        influx_client.write_points(post)
        
        self.send_response(200)
        self.end_headers()

def run():
    server_address = ('', 9926)
    httpd = HTTPServer(server_address, MyServer)
    print('Starting server on port 9926...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()