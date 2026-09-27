from django.db import models


class AppUser(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("pns", "Preferred Not to Say"),
    )

    USER_TYPE = (
        ("recruiter", "Recruiter"),
        ("jobseeker", "Jobseeker"),
        ("admin", "Admin"),
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default="pns",
        blank=True
    )

    u_type = models.CharField(
        max_length=20,
        choices=USER_TYPE,
        default="jobseeker"
    )

    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact_no = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    skill = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.skill


class Jobseeker(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name="jobseeker"
    )

    # Address
    locality = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=128, blank=True)
    district = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=128, default="India")
    pin_code = models.CharField(max_length=20, blank=True)

    # Files
    pictures = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    cover_letter = models.FileField(upload_to="cover_letters/", blank=True, null=True)

    skills = models.ManyToManyField(Skill, related_name="jobseeker", blank=True)

    expected_salary = models.IntegerField(default=0)
    current_salary = models.IntegerField(default=0)
    notice_period = models.IntegerField(default=0)

    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    is_open_to_work = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Recruiter(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        related_name="recruiter"
    )

    company_name = models.CharField(max_length=200, blank=True)
    designation = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(upload_to="recruiter_profiles/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"