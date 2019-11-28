# API to evaluate phone numbers and locate them

By: Carlos Eduardo González López (Carlos85G) {carlos85g at gmail dot com}

## Assumptions
- The running server is able to call `docker-compose` and has a working internet connection to download the required _Docker_ images.
- Provided numbers represent valid or invalid phone numbers in the United States of NorthAmerica.
- Files will only be uploaded through the `/locate_numbers` endpoint, using the POST method.
- Requests will only be served through port 9000.
- The specified command:
```sh
curl -i -X POST -F "numbers=@numbers.csv" -H "Content-Type: multipart/form-data" http://localhost:9000/locate_numbers
```
will make a POST request with a form which includes a CSV file in the "numbers" fiels and will output the response headers (`-i` flag) and body to the console.
- The command specified above will _NOT_ output the requested output file ("output.csv") by itself, as there's no specified output file parameter and the printed headers will make one unreadable.
- The requested output file will be generated using the following command:
```sh
curl -o output.csv -X POST -F "numbers=@numbers.csv" -H "Content-Type: multipart/form-data" http://localhost:9000/locate_numbers
```
where the headers flag has been ommited and there's a new paramenter (`-o` flag) specifying the file to which the result should be dumped to.

## Running

- Inside a properly set-up command line, navigate into the project's directory and run
```sh
docker-compose up
```
- Grab a cup of coffee while the system downloads and sets up the dependencies.
- Run the cURL command.

_Protip_: run this command
```sh
docker-compose up -d
```
instead to re-use the same command line.

## Dependencies used
- _Docker_ (including `docker-compose`)
- _NginX_
- _Python_ 3
- _Django_ 2.2
- _PhoneNumbers_

## Notes about development

While _PhoneNumbers_ inputs a lot of metadata, it'll be better to wait until all the phone numbers are validated and only make the `GeoCoder` request with those data which have already been deemed as valid.

## License
This software does not provide a license and its use is limited to users which have the creator's express consent
