## run 1

FastAPI is a bit stricter - we have to provide a content-type header otherwise we get a 422

``` hey -c 4 -m POST -D data/large-file.json  -H "Content-Type: application/json" http://127.0.0.1:8000/
```

```
interactions/pydantic     
Summary:
  Total:        52.4243 secs
  Slowest:      1.1757 secs
  Fastest:      0.3445 secs
  Average:      1.0433 secs
  Requests/sec: 3.8150

  Total data:   800 bytes
  Size/request: 4 bytes

Response time histogram:
  0.345 [1]     |
  0.428 [0]     |
  0.511 [0]     |
  0.594 [0]     |
  0.677 [0]     |
  0.760 [0]     |
  0.843 [2]     |■
  0.926 [0]     |
  1.009 [20]    |■■■■■
  1.093 [156]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.176 [21]    |■■■■■


Latency distribution:
  10% in 1.0082 secs
  25% in 1.0303 secs
  50% in 1.0469 secs
  75% in 1.0663 secs
  90% in 1.0949 secs
  95% in 1.1037 secs
  99% in 1.1587 secs

Details (average, fastest, slowest):        
  DNS+dialup:   0.0000 secs, 0.3445 secs, 1.1757 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.3691 secs, 0.0834 secs, 0.8336 secs
  resp wait:    0.6055 secs, 0.2028 secs, 1.0266 secs
  resp read:    0.0686 secs, 0.0117 secs, 0.2739 secs

Status code distribution:
  [200] 200 responses
```

## run 2

```
Summary:
  Total:        51.6661 secs
  Slowest:      1.1251 secs
  Fastest:      0.6236 secs
  Average:      1.0281 secs
  Requests/sec: 3.8710

  Total data:   800 bytes
  Size/request: 4 bytes

Response time histogram:
  0.624 [1]     |
  0.674 [0]     |
  0.724 [0]     |
  0.774 [0]     |
  0.824 [2]     |■
  0.874 [1]     |
  0.924 [0]     |
  0.975 [2]     |■
  1.025 [84]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.075 [91]    |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.125 [19]    |■■■■■■■■


Latency distribution:
  10% in 0.9928 secs
  25% in 1.0119 secs
  50% in 1.0278 secs
  75% in 1.0505 secs
  90% in 1.0734 secs
  95% in 1.0908 secs
  99% in 1.1250 secs

Details (average, fastest, slowest):        
  DNS+dialup:   0.0001 secs, 0.6236 secs, 1.1251 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.3567 secs, 0.0736 secs, 0.7984 secs
  resp wait:    0.6051 secs, 0.2556 secs, 1.0170 secs
  resp read:    0.0662 secs, 0.0117 secs, 0.3075 secs

Status code distribution:
  [200] 200 responses

```

## Run 3

```
Summary:
  Total:        51.7198 secs
  Slowest:      1.1163 secs
  Fastest:      0.5927 secs
  Average:      1.0280 secs
  Requests/sec: 3.8670

  Total data:   800 bytes
  Size/request: 4 bytes

Response time histogram:
  0.593 [1]     |
  0.645 [0]     |
  0.697 [0]     |
  0.750 [0]     |
  0.802 [0]     |
  0.854 [2]     |■
  0.907 [1]     |
  0.959 [0]     |
  1.012 [57]    |■■■■■■■■■■■■■■■■■■■■■■     
  1.064 [102]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  1.116 [37]    |■■■■■■■■■■■■■■■


Latency distribution:
  10% in 0.9910 secs
  25% in 1.0049 secs
  50% in 1.0323 secs
  75% in 1.0511 secs
  90% in 1.0793 secs
  95% in 1.0949 secs
  99% in 1.1156 secs

Details (average, fastest, slowest):        
  DNS+dialup:   0.0000 secs, 0.5927 secs, 1.1163 secs
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:    0.3554 secs, 0.0711 secs, 0.8074 secs
  resp wait:    0.6059 secs, 0.2487 secs, 0.9908 secs
  resp read:    0.0665 secs, 0.0120 secs, 0.2619 secs

Status code distribution:
  [200] 200 responses



```
