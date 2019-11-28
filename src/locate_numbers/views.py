from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
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
            phone_number = phonenumbers.parse(line, "US")

            if phonenumbers.is_possible_number(phone_number):
                is_valid = phonenumbers.is_valid_number(phone_number)
                if is_valid:
                    origin = geocoder.description_for_number(phone_number, "en")

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
            # try to process the file
            try:
                file = request.FILES["numbers"]

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
                # Build proper CSV data
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment;filename=output.csv'

                # Write to response
                writer = csv.DictWriter(response, fieldnames)
                writer.writerows(results)

                # Return the CSV
                return response

            except Exception as e:
                # Error found. Inform user
                return HttpResponseServerError("General error: {}".format(e))

        # Return output as response
        return HttpResponse(contents)

    # Default GET response
    return HttpResponse('Hello, there! This is the endpoint to check phone numbers, but the request method you used is not valid :\'(. Try sending your data through POST.')
