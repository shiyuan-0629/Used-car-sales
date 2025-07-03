import re
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 定义排除的路径
        self.excluded_paths = [
            reverse("system:login"),
            reverse("system:register"),
        ]

    def __call__(self, request):
        current_path = request.path_info

        if self.is_path_excluded(current_path):
            return self.get_response(request)

        if not request.session.get('userid', False):
            return redirect(reverse('system:login'))
        return self.get_response(request)

    def is_path_excluded(self, current_path):
        for path in self.excluded_paths:
            if re.match(re.escape(path) + '$', current_path):
                return True
        return False