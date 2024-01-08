## roundtrip

```
Summary:
  Total:        46.6176 secs
  Slowest:      1.0006 secs
  Fastest:      0.5454 secs
  Average:      0.9282 secs
  Requests/sec: 4.2902

  Total data:   58018600 bytes
  Size/request: 290093 bytes

Response time histogram:
  0.545 [1]     |
  0.591 [0]     |
  0.636 [0]     |
  0.682 [0]     |
  0.727 [2]     |■
  0.773 [1]     |
  0.818 [0]     |
  0.864 [0]     |
  0.910 [32]    |■■■■■■■■■■
  0.955 [130]   |■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■    
  1.001 [34]    |■■■■■■■■■■


Latency distribution:
  10% in 0.9011 secs
  25% in 0.9145 secs
  50% in 0.9328 secs
  75% in 0.9510 secs
  90% in 0.9632 secs
  95% in 0.9740 secs
  99% in 0.9946 secs

Details (average, fastest, slowest):
  DNS+dialup:   0.0000 secs, 0.5454 secs, 1.0006 secs        
  DNS-lookup:   0.0000 secs, 0.0000 secs, 0.0000 secs        
  req write:    0.3276 secs, 0.0836 secs, 0.7076 secs        
  resp wait:    0.5492 secs, 0.1991 secs, 0.8518 secs        
  resp read:    0.0512 secs, 0.0007 secs, 0.2179 secs        

Status code distribution:
  [201] 200 responses
```
