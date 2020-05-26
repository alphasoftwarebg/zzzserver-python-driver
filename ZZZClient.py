"""
    ZZZClient.py

    Copyright 2017 ZZZ Ltd. - Bulgaria

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import socket, sys
 
def zzzprogram(host, port, program) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
	 
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        return
	 
    s.sendall((program + '\0').encode('utf-8'))

    result = ''
    while True :
        data = s.recv(4096)
        if not data :
            break
        result += data.decode('utf-8')
		
    s.close()
    return result
		
sys.stdout.write(
    zzzprogram('localhost', 3333,
        '#[cout;Hello World from ZZZServer!]'))
