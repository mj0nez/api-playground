## roundtrip

```
Summary:
  Total:        36.4388 secs
  Slowest:      0.8379 secs
  Fastest:      0.2890 secs
  Average:      0.7248 secs
  Requests/sec: 5.4887

  Total data:   58018600 bytes
  Size/request: 290093 bytes

Response time histogram:
  0.289 [1]     |
  0.344 [0]     |
  0.399 [0]     |
  0.454 [1]     |
  0.509 [0]     |
  0.563 [1]     |
  0.618 [0]     |
  0.673 [0]     |
  0.728 [117]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
  0.783 [59]    |■■■■■■■■■■■■■■■■■■■■
  0.838 [21]    |■■■■■■■


Latency distribution:
  10% in 0.6896 secs
  25% in 0.7054 secs
  50% in 0.7241 secs
  75% in 0.7420 secs
  90% in 0.7839 secs
  95% in 0.8085 secs
  99% in 0.8285 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0000 secs, 0.2890 secs, 0.8379 secs        
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs        
  req write:    0.3151 secs, 0.0893 secs, 0.5771 secs        
  resp wait:    0.4076 secs, 0.1589 secs, 0.7133 secs        
  resp read:    0.0020 secs, 0.0003 secs, 0.0173 secs        

Status code distribution:
  [201] 200 responses
```
