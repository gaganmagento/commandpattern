from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .commands import CreateUserCommand, DeleteUserCommand
from .invoker import UserCommandInvoker
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

@require_http_methods(["GET", "POST", "DELETE"])
def user_management_view(request):
    invoker = UserCommandInvoker()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Create a new user
        command = CreateUserCommand(username, password)
        result = command.execute()
        return JsonResponse(result)

    if request.method == "DELETE":
        user_id = request.GET.get("id")  # Get user ID from query parameters

        if user_id:
            command = DeleteUserCommand(user_id)
            result = command.execute()
            return JsonResponse({'result': result})
        else:
            return JsonResponse({'error': 'User ID is required for deletion.'}, status=400)

    # Handle GET requests or other scenarios if needed
    return JsonResponse({'message': 'Welcome to the user management endpoint.'})
