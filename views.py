from django.shortcuts import render, redirect
from .models import AppUser, Jobseeker, Recruiter
from django.contrib import messages


# Register View
def register(request):
    if request.method == "POST":
        gender = request.POST.get("gender")
        u_type = request.POST.get("utype")
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpwd = request.POST.get("cpwd")
        contact_no = request.POST.get("contact")

        # Check email already exists
        exists = AppUser.objects.filter(email=email).exists()

        if exists:
            messages.error(request, "Email Already Registered.")
            return redirect("register")

        if password != cpwd:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Create User
        user = AppUser.objects.create(
            gender=gender,
            u_type=u_type,
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=password,
            contact_no=contact_no
        )

        if u_type == "jobseeker":
            Jobseeker.objects.create(
    user=user,
    expected_salary=0,
    current_salary=0,
    notice_period=0,
)

        elif u_type == "recruiter":
            Recruiter.objects.create(user=user)

        messages.success(request, "Registration Done Successfully")
        return redirect("login")

    return render(request, "accounts/register.html")


# Login View
def loginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = AppUser.objects.filter(
            email=email,
            password=password
        ).first()

        if user is None:
            messages.error(request, "Invalid Email or Password")
            return redirect("login")

        request.session["user_id"] = user.id
        request.session["user_email"] = user.email

        messages.success(request, "Logged In Successfully!")

        return redirect("home")

    return render(request, "accounts/login.html")
def logoutView(request):
    if request.method=="POST":
        request.session.flush()
        messages.success(request,"logged out successfully")
        return redirect('login')
    return redirect('login')