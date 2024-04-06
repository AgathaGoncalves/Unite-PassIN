# pylint: disable-all
from src.http_types.http_response import HttpResponse
from src.erros.erros_types.http_conflict import HttpConflictserror
from src.erros.erros_types.http_not_found import HttpNotFound

def handle_error(error: Exception)-> HttpResponse:
    if isinstance(error,(HttpConflictserror,HttpNotFound )):
        return HttpResponse(
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            status_code= error.status_code
        )
    return HttpResponse(
        body={
            "errors":[{
                "title": "error",
                "detail": str(error)
            }]
        }
    )

