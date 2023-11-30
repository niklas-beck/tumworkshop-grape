import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="http-trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. But who are you?",
             status_code=200
        )


# Add a new function here

# TODO
@app.route(route="http-sum")
def http_sum(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python sum function processed a request.')

    a = req.params.get('a')
    b = req.params.get('b')

    if a and b:
        try:
            a = int(a)
            b = int(b)
            result = a + b
            return func.HttpResponse(f"The sum of {a} and {b} is: {result}")
        except ValueError:
            return func.HttpResponse("Invalid input. Please provide valid integers for 'a' and 'b'.", status_code=400)
    else:
        return func.HttpResponse("Please provide values for 'a' and 'b' parameters.", status_code=200)

