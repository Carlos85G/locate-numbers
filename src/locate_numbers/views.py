from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from phonenumbers import geocoder
import csv
import phonenumbers
import codecs

# Create your views here.

# Function exempt from CSRF verification for CURL access
@csrf_exempt
def index(request):
    # Field names for future use
    fieldnames = ["numbers", "valid", "origin",]

    # Callable to process the phone number line
    def evaluate_line(line):
        is_valid = False
        origin = "N/A"

        try:
            # Try to parse or raise exception
            phone_number = phonenumbers.parse(line, "US")

            if phonenumbers.is_possible_number(phone_number):
                is_valid = phonenumbers.is_valid_number(phone_number)
                if is_valid:
                    pre_origin = geocoder.description_for_number(phone_number, "en")
                    # Check that value is a non-empty string (evaluates truthy)
                    if pre_origin:
                        origin = pre_origin

        except Exception as e:
            is_valid = False
            raise Exception("Error evaluating line: {}".format(e))

        # Return dictionary of results
        return {
            "numbers":line,
            "valid": str(is_valid).lower(),
            "origin":origin
        }

    if request.method == "POST":
        contents = "(Empty file)"

        if "numbers" in request.FILES:
            # File for future use
            file = request.FILES["numbers"]

            # Build proper CSV response data
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;filename=output.csv'

            # Write to prepared response
            writer = csv.DictWriter(response, fieldnames)
            writer.writeheader()

            # Try to process the file
            try:
                # Accept CSV files only.
                # content_type will return "application/octet-stream", so it'll
                # check file extension instead
                if not file.name.endswith(".csv"):
                    raise Exception("File not valid. Will only accept files with CSV extension.")

                # Note: InMemoryUploadedFile has no chunks, as it's in memory.
                # First row has headers. Decode and read as dictionary
                lines = csv.DictReader(
                    codecs.iterdecode(file, 'utf-8')
                )

                # Build the output
                results = list(
                    map(
                        lambda line: evaluate_line(line["numbers"]),
                        lines
                    )
                )

                # Write into response
                writer.writerows(results)

                # Return the CSV
                return response

            except Exception as e:
                # Error found. Inform user
                return HttpResponseServerError("General error: {}".format(e))
        else:
            return HttpResponseBadRequest("No file in the request")

    # Default GET response
    return HttpResponse('Hello, there! This is the endpoint to check phone numbers, but the request method you used is not valid :\'(. Try sending your data through POST.')
