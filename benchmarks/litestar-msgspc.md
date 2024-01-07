```
hey -c 4 -m POST -D data/large-file.json  http://127.0.0.1:8000/msgspec
```
## Run 1

Summary:
  Total:        29.6975 secs
  Slowest:      0.7466 secs
  Fastest:      0.2901 secs
  Average:      0.5908 secs
  Requests/sec: 6.7346

  Total data:   400 bytes
  Size/request: 2 bytes

Response time histogram:
  0.290 [1]     |
  0.336 [0]     |
  0.381 [0]     |
  0.427 [1]     |
  0.473 [0]     |
  0.518 [1]     |
  0.564 [40]    |■■■■■■■■■■■■■■■
  0.610 [110]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.655 [27]    |■■■■■■■■■■
  0.701 [12]    |■■■■
  0.747 [8]     |■■■

Latency distribution:
  10% in 0.5503 secs
  25% in 0.5659 secs
  50% in 0.5844 secs
  75% in 0.6087 secs
  90% in 0.6581 secs
  95% in 0.6800 secs
  99% in 0.7465 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0001 secs, 0.2901 secs, 0.7466 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.2590 secs, 0.0884 secs, 0.5247 secs
  resp wait:    0.3308 secs, 0.1520 secs, 0.6217 secs
  resp read:    0.0009 secs, 0.0004 secs, 0.0134 secs

Status code distribution:
  [201] 200 responses


## Run 2 

Summary:
  Total:        29.4436 secs
  Slowest:      0.7066 secs
  Fastest:      0.2992 secs
  Average:      0.5861 secs
  Requests/sec: 6.7927
  
  Total data:   400 bytes
  Size/request: 2 bytes

Response time histogram:
  0.299 [1]     |
  0.340 [0]     |
  0.381 [0]     |
  0.421 [1]     |
  0.462 [0]     |
  0.503 [0]     |
  0.544 [10]    |■■■■
  0.584 [89]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■  
  0.625 [79]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■      
  0.666 [14]    |■■■■■■
  0.707 [6]     |■■■


Latency distribution:
  10% in 0.5504 secs
  25% in 0.5690 secs
  50% in 0.5841 secs
  75% in 0.6020 secs
  90% in 0.6262 secs
  95% in 0.6554 secs
  99% in 0.6990 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0001 secs, 0.2992 secs, 0.7066 secs      
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs      
  req write:    0.2571 secs, 0.0924 secs, 0.4818 secs      
  resp wait:    0.3259 secs, 0.1669 secs, 0.5790 secs      
  resp read:    0.0030 secs, 0.0003 secs, 0.0154 secs      

Status code distribution:
  [201] 200 responses



