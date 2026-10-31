from django.db import models


# ============================================================
# SCHOOL SETTINGS
# ============================================================

class SchoolSettings(models.Model):

    school_name = models.CharField(
        max_length=200,
        default="Lakhi Ram Memorial Public Sec. School"
    )

    logo = models.ImageField(
        upload_to="school/logo/",
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    # ========================================================
    # WHATSAPP
    # ========================================================

    whatsapp_number = models.CharField(
        max_length=30,
        default="+91 89500 25448",
        blank=True,
        help_text="WhatsApp number with country code"
    )

    # ========================================================
    # SOCIAL MEDIA
    # ========================================================

    facebook_url = models.URLField(
        blank=True
    )

    instagram_url = models.URLField(
        blank=True
    )

    youtube_url = models.URLField(
        blank=True
    )

    # ========================================================
    # GOOGLE MAPS LOCATION
    # ========================================================

    location_url = models.URLField(
        blank=True,
        help_text="Google Maps location URL"
    )

    location_embed_url = models.URLField(
        blank=True,
        help_text="Google Maps Embed URL - paste only the URL from iframe src"
    )

    # ========================================================
    # HOMEPAGE
    # ========================================================

    marquee_text = models.CharField(
        max_length=500,
        default="Welcome to Lakhi Ram Memorial Public Sec. School"
    )

    admission_open = models.BooleanField(
        default=True
    )

    admission_button_show = models.BooleanField(
        default=True
    )

    hero_video = models.FileField(
        upload_to="school/hero/",
        blank=True,
        null=True
    )

    # ========================================================
    # FOOTER
    # ========================================================

    made_by = models.CharField(
        max_length=200,
        default="Sanjay Dahiya"
    )

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = "School Settings"
        verbose_name_plural = "School Settings"


# ============================================================
# PRINCIPAL
# ============================================================

class Principal(models.Model):

    name = models.CharField(
        max_length=200,
        default="Principal"
    )

    photo = models.ImageField(
        upload_to="school/principal/",
        blank=True,
        null=True
    )

    thoughts = models.TextField(
        blank=True
    )

    designation = models.CharField(
        max_length=100,
        default="Principal"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# ============================================================
# HOME PAGE PHOTOS
# ============================================================

class HomePhoto(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="school/home/"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title or f"Home Photo {self.id}"

    class Meta:
        ordering = ["order", "-id"]


# ============================================================
# GALLERY PHOTOS
# ============================================================

class GalleryPhoto(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="school/gallery/photos/"
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title or f"Gallery Photo {self.id}"

    class Meta:
        ordering = ["order", "-created_at"]


# ============================================================
# GALLERY VIDEOS
# ============================================================

class GalleryVideo(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True
    )

    video = models.FileField(
        upload_to="school/gallery/videos/"
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title or f"Gallery Video {self.id}"

    class Meta:
        ordering = ["order", "-created_at"]


# ============================================================
# STUDENT RESULTS
# ============================================================

class Result(models.Model):

    CLASS_CHOICES = [
        ("10th", "10th"),
        ("12th", "12th"),
    ]

    student_name = models.CharField(
        max_length=200
    )

    student_photo = models.ImageField(
        upload_to="school/results/"
    )

    student_class = models.CharField(
        max_length=10,
        choices=CLASS_CHOICES
    )

    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    year = models.PositiveIntegerField(
        default=2026
    )

    rank = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student_name} - {self.student_class}"

    class Meta:
        ordering = ["student_class", "-percentage"]


# ============================================================
# ABOUT SCHOOL
# ============================================================

class AboutSchool(models.Model):

    title = models.CharField(
        max_length=200,
        default="About Our School"
    )

    content = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="school/about/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


# ============================================================
# SCHOOL FACILITIES
# ============================================================

class Facility(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="school/facilities/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fas fa-bus"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", "-id"]


# ============================================================
# ACADEMICS
# ============================================================

class Academic(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="school/academics/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fas fa-book"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Academic"
        verbose_name_plural = "Academics"


# ============================================================
# SPORTS
# ============================================================

class Sport(models.Model):

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="school/sports/",
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        default="fas fa-trophy",
        blank=True,
        help_text="Example: fas fa-futbol"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order", "-created_at"]


# ============================================================
# SPORT PHOTOS
# ============================================================

class SportPhoto(models.Model):

    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name="photos"
    )

    title = models.CharField(
        max_length=200,
        blank=True
    )

    image = models.ImageField(
        upload_to="school/sports/photos/"
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        if self.title:
            return f"{self.sport.name} - {self.title}"

        return f"{self.sport.name} - Photo {self.id}"

    class Meta:
        ordering = ["order", "-created_at"]


# ============================================================
# SPORT VIDEOS
# ============================================================

class SportVideo(models.Model):

    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name="videos"
    )

    title = models.CharField(
        max_length=200,
        blank=True
    )

    video = models.FileField(
        upload_to="school/sports/videos/"
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        if self.title:
            return f"{self.sport.name} - {self.title}"

        return f"{self.sport.name} - Video {self.id}"

    class Meta:
        ordering = ["order", "-created_at"]


# ============================================================
# ADMISSION APPLICATION
# ============================================================

class AdmissionApplication(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    # ========================================================
    # APPLICATION NUMBER
    # ========================================================

    application_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        editable=False
    )

    student_name = models.CharField(
        max_length=200
    )

    father_name = models.CharField(
        max_length=200
    )

    mother_name = models.CharField(
        max_length=200,
        blank=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True
    )

    applying_class = models.CharField(
        max_length=50
    )

    mobile = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField()

    previous_school = models.CharField(
        max_length=300,
        blank=True
    )

    message = models.TextField(
        blank=True
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="New"
    )

    # ========================================================
    # AUTOMATIC APPLICATION NUMBER
    # ========================================================

    def save(self, *args, **kwargs):

        if not self.application_number:

            last_application = (
                AdmissionApplication.objects
                .filter(
                    application_number__startswith="LRMP"
                )
                .order_by("-id")
                .first()
            )

            if last_application:

                try:
                    last_number = int(
                        last_application.application_number.replace(
                            "LRMP",
                            ""
                        )
                    )

                    next_number = last_number + 1

                except (ValueError, TypeError):
                    next_number = 1

            else:
                next_number = 1

            self.application_number = f"LRMP{next_number:06d}"

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.application_number} - "
            f"{self.student_name} - "
            f"{self.applying_class}"
        )

    class Meta:
        ordering = ["-submitted_at"]