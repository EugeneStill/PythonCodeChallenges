from collections import Counter
import pprint

log = [
    '0411201800123546DTC GET /8/tickets/put 404 IOError',
    '0411201800123546DTC PUT /563/tickets/new 200 Success',
    '0411201800123546DTC GET /13/tickets/put 200 Success',
    '0411201800123546DTC GET /12323/tickets/put 404 IOError',
    '0411201800123546DTC UPDATE /12323/tickets/put 200 Success',
    '0411201800123546DTC GET /94/tickets/put 404 IOError',
    '0411201800123546DTC GET /12323/tickets/put 404 IOError',
    '0411201800123546DTC PUT /11/tickets/new 200 Success',
    '0411201800123546DTC UPDATE /12323/tickets/put 200 Success',
    '0411201800123546DTC GET /99/tickets/put 404 IOError'
]

log = [i.split() for i in log]

for i in range(len(log)):
    log[i][0] = log[i][0].replace('DTC', 'DTC/', 1)
    log[i][2] = log[i][2].replace('/', '/*', 1)
    log[i][2] = ''.join(char for char in log[i][2] if not char.isdigit())
    log[i] = ''.join(log[i])

pprint.pprint(Counter(log))