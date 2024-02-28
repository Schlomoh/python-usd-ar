
Contains a small flask web server written in python to act as a converion service using the packaged converter tools.

Reads in binary data from requests sent to `<host>:<port=8080>/`. The binary data has to be a glb file as binary base64 encoded string. The string has to be sent in a `data` field in the json body of the request. 

```json
{
    data: 'thedatastringinbinary...'
}
```

The request also has to announce the size of the binary file data as a query paramerter called `filesize`. Set the filesize param to the byte size of the file. Any size bigger than 50MB in bytes (52428800) will be rejected.

Like this:

```js
    const searchparams = {
        filesize: 1234567
    }
```


[![Twitter: @plattarglobal](https://img.shields.io/badge/contact-@plattarglobal-blue.svg?style=flat)](https://twitter.com/plattarglobal)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat)](LICENSE)

_Python USD AR_ is a docker container that contains pre-built versions of [Pixar USD](https://github.com/PixarAnimationStudios/USD) toolchain and [Apple USDZ Schema](https://developer.apple.com/documentation/arkit/usdz_schemas_for_ar) definitions. Due to the amount of time it takes to build these tools, this container can serve as a useful base for other applications. Check out the Plattar [dockerhub](https://hub.docker.com/r/plattar/python-usd-ar) repository for the latest pre-built images.

Looking for the standard _Python USD_ images without Apple USDZ Schema Definitions? Check out the [python-usd](https://github.com/Plattar/python-usd) repository.

### Acknowledgements

This tool relies on the following open source projects.

-   [Apple AR Tools](https://developer.apple.com/augmented-reality/tools/)
-   [Apple USDZ Schemas](https://developer.apple.com/documentation/arkit/usdz_schemas_for_ar)
-   [Plattar Python USD](https://github.com/Plattar/python-usd)
