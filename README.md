# Playground

This repository provides a playground to evaluate different API-frameworks. Implementing the same functionality with different libs should show meaningful differences in concepts, implementation and performance.

## The App

...

## Benchmarks

>[!NOTE]  
>
> Requirements:
>
> * [hey](https://github.com/rakyll/hey): HTTP load generator, ApacheBench (ab) replacement

WIP

### Upload of ~ 13.5 MB JSON

* Litestar
  * msgspec DTO
  * pydantic DTO

* FastAPI
  * pydantic

### Upload of ~ 13.5 MB JSON with serialized Response of 283.29 KB

For a quick test the implemented data model is small. I suspect that the difference between the frameworks will increase with the response size.

* Litestar
  * msgspec DTO
  * pydantic DTO

* FastAPI
  * pydantic

## Disclaimer

The JSON data was taken from [here](https://github.com/json-iterator/test-data/blob/master/large-file.json) and shortened while the idea originated from following this [podcast](https://www.youtube.com/live/9Qq2q-9HHqs?si=W6z3LEbj5WLN86JC) and reading the referenced [article](https://pythonspeed.com/articles/faster-python-json-parsing/).
