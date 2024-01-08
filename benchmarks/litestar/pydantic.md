```
hey -c 4 -m POST -D data/large-file.json  http://127.0.0.1:8000/pydantic
```

## Run 1

```Summary:
  Total:        43.6534 secs
  Slowest:      1.0351 secs
  Fastest:      0.3642 secs
  Average:      0.8683 secs
  Requests/sec: 4.5815
  
  Total data:   400 bytes
  Size/request: 2 bytes

Response time histogram:
  0.364 [1]     |
  0.431 [0]     |
  0.498 [0]     |
  0.565 [0]     |
  0.633 [0]     |
  0.700 [1]     |
  0.767 [0]     |
  0.834 [45]    |■■■■■■■■■■■■■■■■■■
  0.901 [98]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.968 [52]    |■■■■■■■■■■■■■■■■■■■■■
  1.035 [3]     |■


Latency distribution:
  10% in 0.8142 secs
  25% in 0.8371 secs
  50% in 0.8683 secs
  75% in 0.9068 secs
  90% in 0.9360 secs
  95% in 0.9493 secs
  99% in 0.9727 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0000 secs, 0.3642 secs, 1.0351 secs      
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs      
  req write:    0.3479 secs, 0.0972 secs, 0.7042 secs      
  resp wait:    0.5175 secs, 0.2153 secs, 0.8630 secs      
  resp read:    0.0028 secs, 0.0001 secs, 0.0144 secs      

Status code distribution:
  [201] 200 responses
```

## Run 2

```Summary:
  Total:        42.4593 secs
  Slowest:      1.0788 secs
  Fastest:      0.3958 secs
  Average:      0.8442 secs
  Requests/sec: 4.7104
  
  Total data:   400 bytes
  Size/request: 2 bytes

Response time histogram:
  0.396 [1]     |
  0.464 [0]     |
  0.532 [0]     |
  0.601 [0]     |
  0.669 [1]     |
  0.737 [0]     |
  0.806 [16]    |■■■■
  0.874 [150]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.942 [23]    |■■■■■■
  1.011 [8]     |■■
  1.079 [1]     |


Latency distribution:
  10% in 0.8066 secs
  25% in 0.8185 secs
  50% in 0.8394 secs
  75% in 0.8604 secs
  90% in 0.8988 secs
  95% in 0.9407 secs
  99% in 1.0075 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0000 secs, 0.3958 secs, 1.0788 secs      
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs      
  req write:    0.3458 secs, 0.0967 secs, 0.7356 secs      
  resp wait:    0.4966 secs, 0.2322 secs, 0.8473 secs      
  resp read:    0.0016 secs, 0.0001 secs, 0.0145 secs      

Status code distribution:
  [201] 200 responses
```

## Run 3

```
Summary:
  Total:        44.1290 secs
  Slowest:      1.0799 secs
  Fastest:      0.5218 secs
  Average:      0.8789 secs
  Requests/sec: 4.5322

  Total data:   400 bytes
  Size/request: 2 bytes

Response time histogram:
  0.522 [1]     |■
  0.578 [1]     |■
  0.633 [0]     |
  0.689 [1]     |■
  0.745 [0]     |
  0.801 [1]     |■
  0.857 [70]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.912 [75]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.968 [35]    |■■■■■■■■■■■■■■■■■■■        
  1.024 [11]    |■■■■■■
  1.080 [5]     |■■■


Latency distribution:
  10% in 0.8273 secs
  25% in 0.8453 secs
  50% in 0.8695 secs
  75% in 0.9126 secs
  90% in 0.9473 secs
  95% in 0.9960 secs
  99% in 1.0694 secs
0000 secs
  req write:    0.3117 secs, 0.0957 secs, 0.4868 secs        
  resp wait:    0.5264 secs, 0.2176 secs, 0.8946 secs        
  resp read:    0.0407 secs, 0.0003 secs, 0.2379 secs        

Status code distribution:
  [201] 200 responses
```

cl