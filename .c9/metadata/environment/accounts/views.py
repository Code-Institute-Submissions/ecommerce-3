{"changed":true,"filter":false,"title":"views.py","tooltip":"/accounts/views.py","value":"from django.shortcuts import render, redirect, HttpResponseRedirect\nfrom django.contrib import messages, auth\nfrom django.core.urlresolvers import reverse\nfrom .forms import UserLoginForm, UserRegistrationForm\nfrom django.template.context_processors import csrf\nfrom django.contrib.auth.decorators import login_required\n\n\n# Create your views here.\ndef index(request):\n    \"\"\"A view that displays the index page\"\"\"\n    return render(request, \"index.html\")\n    \ndef home(request):\n    \"\"\"A view that displays the home page\"\"\"\n    return render(request, \"home.html\")\n\ndef logout(request):\n    \"\"\"A view that logs the user out and redirects back to the index page\"\"\"\n    auth.logout(request)\n    messages.success(request, 'You have successfully logged out')\n    return redirect(reverse('index'))\n\n\ndef login(request):\n    \"\"\"A view that manages the login form\"\"\"\n    if request.method == 'POST':\n        user_form = UserLoginForm(request.POST)\n        if user_form.is_valid():\n            user = auth.authenticate(request.POST['username_or_email'],\n                                     password=request.POST['password'])\n\n            if user:\n                auth.login(request, user)\n                messages.error(request, \"You have successfully logged in\")\n\n                if request.GET and request.GET['next'] !='':\n                    next = request.GET['next']\n                    return HttpResponseRedirect(next)\n                else:\n                    return redirect(reverse('index'))\n            else:\n                user_form.add_error(None, \"Your username or password are incorrect\")\n    else:\n        user_form = UserLoginForm()\n\n    args = {'user_form': user_form, 'next': request.GET.get('next', '')}\n    return render(request, 'login.html', args)\n\n\n@login_required\ndef profile(request):\n    \"\"\"A view that displays the profile page of a logged in user\"\"\"\n    return render(request, 'profile.html')\n\n\ndef register(request):\n    \"\"\"A view that manages the registration form\"\"\"\n    if request.method == 'POST':\n        user_form = UserRegistrationForm(request.POST)\n        if user_form.is_valid():\n            user_form.save()\n\n            user = auth.authenticate(request.POST.get('email'),\n                                     password=request.POST.get('password1'))\n\n            if user:\n                auth.login(request, user)\n                messages.success(request, \"You have successfully registered\")\n                return redirect(reverse('index'))\n\n            else:\n                messages.error(request, \"unable to log you in at this time!\")\n    else:\n        user_form = UserRegistrationForm()\n\n    args = {'user_form': user_form}\n    return render(request, 'register.html', args)\n\n","undoManager":{"mark":9,"position":11,"stack":[[{"start":{"row":11,"column":40},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":13,"column":0},"end":{"row":15,"column":40},"action":"insert","lines":["def index(request):","    \"\"\"A view that displays the index page\"\"\"","    return render(request, \"index.html\")"],"id":4}],[{"start":{"row":15,"column":40},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["x"],"id":6},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["e"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["d"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["n"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["h"],"id":7},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["o"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["m"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"remove","lines":["x"],"id":8},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["e"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["d"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["n"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["i"]}],[{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"insert","lines":["h"],"id":9},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"insert","lines":["o"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"insert","lines":["m"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":33},"action":"remove","lines":["x"],"id":10},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"remove","lines":["e"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"remove","lines":["d"]},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"remove","lines":["n"]},{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"remove","lines":["i"]}],[{"start":{"row":15,"column":28},"end":{"row":15,"column":29},"action":"insert","lines":["h"],"id":11},{"start":{"row":15,"column":29},"end":{"row":15,"column":30},"action":"insert","lines":["o"]},{"start":{"row":15,"column":30},"end":{"row":15,"column":31},"action":"insert","lines":["m"]},{"start":{"row":15,"column":31},"end":{"row":15,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["e"],"id":12},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["m"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["o"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["h"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"insert","lines":["h"],"id":13},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"insert","lines":["o"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"insert","lines":["m"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":8},"end":{"row":13,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":26,"state":"start","mode":"ace/mode/python"}},"timestamp":1567895721311}