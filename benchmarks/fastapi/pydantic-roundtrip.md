## run 1

```
hey -c 4 -m POST -D data/large-file.json  -H "Content-Type: application/json" http://127.0.0.1:8000/interactions/pydantic/roundtrip
```

```
Summary:
  Total:        58.6744 secs
  Slowest:      1.5036 secs
  Fastest:      0.5936 secs
  Average:      1.1680 secs
  Requests/sec: 3.4086

  Total data:   58018600 bytes
  Size/request: 290093 bytes

Response time histogram:
  0.594 [1]     |■
  0.685 [0]     |
  0.776 [0]     |
  0.867 [2]     |■
  0.958 [1]     |■
  1.049 [1]     |■
  1.140 [79]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.231 [79]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.322 [27]    |■■■■■■■■■■■■■■
  1.413 [6]     |■■■
  1.504 [4]     |■■


Latency distribution:
  10% in 1.0900 secs
  25% in 1.1202 secs
  50% in 1.1559 secs
  75% in 1.2131 secs
  90% in 1.2821 secs
  95% in 1.3281 secs
  99% in 1.5035 secs
0000 secs
  req write:    0.4075 secs, 0.0727 secs, 1.0412 secs        
  resp wait:    0.6851 secs, 0.2453 secs, 1.3448 secs        
  resp read:    0.0754 secs, 0.0127 secs, 0.3651 secs        

Status code distribution:
  [200] 200 responses

```

## Run 2

```
Summary:
  Total:        56.0887 secs
  Slowest:      1.2551 secs
  Fastest:      0.8795 secs
  Average:      1.1172 secs
  Requests/sec: 3.5658

  Total data:   58018600 bytes
  Size/request: 290093 bytes

Response time histogram:
  0.879 [1]     |■
  0.917 [3]     |■■
  0.955 [0]     |
  0.992 [0]     |
  1.030 [0]     |
  1.067 [14]    |■■■■■■■■
  1.105 [68]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
  1.142 [68]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
  1.180 [20]    |■■■■■■■■■■■■
  1.217 [14]    |■■■■■■■■
  1.255 [12]    |■■■■■■■


Latency distribution:
  10% in 1.0712 secs
  25% in 1.0822 secs
  50% in 1.1154 secs
  75% in 1.1414 secs
  90% in 1.1996 secs
  95% in 1.2320 secs
  99% in 1.2548 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0001 secs, 0.8795 secs, 1.2551 secs        
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs        
  req write:    0.3345 secs, 0.0818 secs, 0.6538 secs        
  resp wait:    0.6523 secs, 0.2820 secs, 1.1397 secs        
  resp read:    0.1302 secs, 0.0127 secs, 0.4606 secs        

Status code distribution:
  [200] 200 responses

```

## Run 3

```

Summary:
  Total:        58.2395 secs
  Slowest:      1.4228 secs
  Fastest:      0.6067 secs
  Average:      1.1580 secs
  Requests/sec: 3.4341

  Total data:   58018600 bytes
  Size/request: 290093 bytes

Response time histogram:
  0.607 [1]     |
  0.688 [0]     |
  0.770 [0]     |
  0.852 [2]     |■
  0.933 [1]     |
  1.015 [0]     |
  1.096 [15]    |■■■■■
  1.178 [118]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
  1.260 [48]    |■■■■■■■■■■■■■■■■
  1.341 [10]    |■■■
  1.423 [5]     |■■


Latency distribution:
  10% in 1.0970 secs
  25% in 1.1217 secs
  50% in 1.1519 secs
  75% in 1.1920 secs
  90% in 1.2432 secs
  95% in 1.2737 secs
  99% in 1.4228 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0000 secs, 0.6067 secs, 1.4228 secs        
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs        
  req write:    0.3960 secs, 0.0862 secs, 0.9854 secs        
  resp wait:    0.6852 secs, 0.2006 secs, 1.2174 secs        
  resp read:    0.0767 secs, 0.0131 secs, 0.3785 secs        

Status code distribution:
  [200] 200 responses

```
